
import pandas as pd
import streamlit as st
import calendar
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode, JsCode, ColumnsAutoSizeMode
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
    
    testbuild = {
    "pagination": False,
    "defaultColDef": {
        "minColumnWidth": 75,
        'filterable': True,
        'sortable': False,
        'editable': True,
        'rowDrag': True,
        'rowDragManaged': True,
        'rowDragEntireRow': False,
        'rowDragMultiRow': True,
        'suppressMenu': False,
    },
    "columnDefs": [
        {'field': 'Sprint', 'rowDrag': True,'rowDragEntireRow': True,},
        {'field': 'Project', 'width':450},
        {'field': 'Status', 'width':125},
        {'field': 'ReceivedDate'},
        {'field': 'Analyst'},
        {'field': 'Effort'},
    ],
    'rowDragManaged': True,
    'rowDragEntireRow': True,
    'rowDragMultiRow': True,
    'rowDrag':True,
    'selection_mode':'multiple',
    'use_checkbox':True,
    "onCellValueChanged":"--x_x--0_0-- function(e) { let api = e.api; let rowIndex = e.rowIndex; let col = e.column.colId; let rowNode = api.getDisplayedRowAtIndex(rowIndex); api.flashCells({ rowNodes: [rowNode], columns: [col], flashDelay: 10000000000 }); }; --x_x--0_0--"
    }
    
    return AgGrid(
        data=dfall,
        editable=True,
        gridOptions=testbuild,
        data_return_mode=DataReturnMode.AS_INPUT,
        update_mode=GridUpdateMode.MODEL_CHANGED,
        columns_auto_size_mode=ColumnsAutoSizeMode.FIT_ALL_COLUMNS_TO_VIEW,
        enable_enterprise_modules=True,
        theme='light', 
        height=600, 
        allow_unsafe_jscode=True,
        key='sprintBoardTableKey',
        )      

grid_response = displayTable(dfall)
dfgo = grid_response['data']


if dfall.equals(dfgo) == False:
    dfall = grid_response['data']
    goog = dfgo.values.tolist()
    body = { 'values': goog }
    service.spreadsheets().values().update(
                                    spreadsheetId=spreadsheetId, 
                                    range='PrimaryTable!A2:F',
                                    valueInputOption='USER_ENTERED', 
                                    body=body).execute()

# st.sidebar.button('ye')

    
    
    
    
    