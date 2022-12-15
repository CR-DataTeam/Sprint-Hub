
import pandas as pd
import streamlit as st
import calendar
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode, JsCode
import datetime
from google.oauth2 import service_account
from googleapiclient.discovery import build
import strConstants as sc

st.set_page_config(
     page_title="Sprint Board",
     layout="wide"
     )
padding = 0
st.markdown(f""" <style>
    .reportview-container .main .block-container{{
        padding-top: {padding}rem;
        padding-right: {padding}rem;
        padding-left: {padding}rem;
        padding-bottom: {padding}rem;
    }} </style> """, unsafe_allow_html=True)


st.markdown(sc.getCodeSnippet('sidebarWidth'), unsafe_allow_html=True)
st.markdown(sc.getCodeSnippet('hideStreamlitStyle'), unsafe_allow_html=True)
st.markdown(sc.getCodeSnippet('adjustPaddingAndFont'), unsafe_allow_html=True)
js = JsCode(sc.getCodeSnippet('jsCodeStr'))

onRowDragEnd = JsCode("""
function onRowDragEnd(e) {
    console.log('onRowDragEnd', e);
}
""")

getRowNodeId = JsCode("""
function getRowNodeId(data) {
    return data.id
}
""")

onGridReady = JsCode("""
function onGridReady() {
    immutableStore.forEach(
        function(data, index) {
            data.id = index;
            });
    gridOptions.api.setRowData(immutableStore);
    }
""")

onRowDragMove = JsCode("""
function onRowDragMove(event) {
    var movingNode = event.node;
    var overNode = event.overNode;

    var rowNeedsToMove = movingNode !== overNode;

    if (rowNeedsToMove) {
        var movingData = movingNode.data;
        var overData = overNode.data;

        immutableStore = newStore;

        var fromIndex = immutableStore.indexOf(movingData);
        var toIndex = immutableStore.indexOf(overData);

        var newStore = immutableStore.slice();
        moveInArray(newStore, fromIndex, toIndex);

        immutableStore = newStore;
        gridOptions.api.setRowData(newStore);

        gridOptions.api.clearFocusedCell();
    }

    function moveInArray(arr, fromIndex, toIndex) {
        var element = arr[fromIndex];
        arr.splice(fromIndex, 1);
        arr.splice(toIndex, 0, element);
    }
}
""")
###############################################################################
#### set-up basis for iteration
###############################################################################

creds = service_account.Credentials.from_service_account_file(
    'serviceacc.json',
    scopes=['https://www.googleapis.com/auth/spreadsheets'],
    )
    
service = build('sheets', 'v4', credentials=creds, cache_discovery=False)
spreadsheetId = '1wNYw_VE9oCJENqtUUEnrRgK0qJWL9dMSgHkLXIAtSTw'
rangeName = 'PrimaryTable!A:F'

def fetchData():
    creds = service_account.Credentials.from_service_account_file(
        'serviceacc.json',
        scopes=['https://www.googleapis.com/auth/spreadsheets'],
        )
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheetId, range=rangeName).execute()
    
    df = pd.DataFrame(result['values'])
    df.columns = df.iloc[0]
    dfpiv = df[1:]
    dfall = dfpiv
    return dfall

dfall = fetchData() 

#for i in range(len(facilityList)):
def displayTable(df: pd.DataFrame) -> AgGrid:
    i = 0
    
    # gb.configure_default_column(rowDrag = False, rowDragManaged = True, rowDragEntireRow = False, rowDragMultiRow=True)
    # gb.configure_grid_options(rowDragManaged = True, onRowDragEnd = onRowDragEnd, 
        #deltaRowDataMode = True, getRowNodeId = getRowNodeId, onGridReady = onGridReady, animateRows = True, onRowDragMove = onRowDragMove)
    # gridOptions = gb.build()
    
    testbuild = {
    # enable Master / Detail
    "enableRangeSelection": True,
    "pagination": False,
    "defaultColDef": {
        "minColumnWidth": 75,
        'filterable': True,
        'sortable': True,
        'editable': True,
        'rowDrag': True,
        'rowDragManaged': True,
        'rowDragEntireRow': False,
        'rowDragMultiRow': True,
        'suppressMenu': False,
    },
    # the first Column is configured to use agGroupCellRenderer
    "columnDefs": [
        {'field': 'Sprint', 'editable':True,'rowDrag': True,'rowDragEntireRow': True,},#'sort':'asc',
        {'field': 'Project', 'width':400, 'editable':True,},
        {'field': 'Status', 'width':125, 'editable':True,}, # 'pinned':'left',
        {'field': 'ReceivedDate', 'editable':True,},
        {'field': 'Analyst','editable':True,},
        {'field': 'Effort', 'editable':True, 'rowdrag':False},
    ],
    
    'rowDragManaged': True,
    'rowDragEntireRow': True,
    'rowDragMultiRow': True,
    'rowDrag':True,
    'onRowDragEnd': onRowDragEnd, 
    'deltaRowDataMode': True, 
    'getRowNodeId': getRowNodeId, 
    'onGridReady': onGridReady, 
    'animateRows': True, 
    'onRowDragMove': onRowDragMove,
    "onCellValueChanged":"--x_x--0_0-- function(e) { let api = e.api; let rowIndex = e.rowIndex; let col = e.column.colId; let rowNode = api.getDisplayedRowAtIndex(rowIndex); api.flashCells({ rowNodes: [rowNode], columns: [col], flashDelay: 10000000000 }); }; --x_x--0_0--"
    }
    
    return AgGrid(
        data=dfall,
        editable=True,
        gridOptions=testbuild,
        data_return_mode=DataReturnMode.AS_INPUT,
        update_mode=GridUpdateMode.MANUAL|GridUpdateMode.VALUE_CHANGED|GridUpdateMode.FILTERING_CHANGED,#|GridUpdateMode.SORTING_CHANGED|GridUpdateMode.SELECTION_CHANGED,
        # update_on=['cellValueChanged','rowDragEnd','gridReady','firstDataRendered','modelUpdated'],
        fit_columns_on_grid_load=True,
        theme='light', 
        height=750, 
        allow_unsafe_jscode=True,
        # enable_enterprise_modules=True,
        key='sprintBoardTableKey',
        )      

grid_response = displayTable(dfall)
dfgo = grid_response['data']

saveB = st.button('Save Order')

if dfall.equals(dfgo) == False or saveB:
        dfall = dfgo
        goog = dfgo.values.tolist()
        body = { 'values': goog }
        service.spreadsheets().values().update(
                                        spreadsheetId=spreadsheetId, 
                                        range='PrimaryTable!A2:F',
                                        valueInputOption='USER_ENTERED', 
                                        body=body).execute()


    
    
    
    
    