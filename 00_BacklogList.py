
import pandas as pd
import streamlit as st
import calendar
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode, JsCode
import datetime
from google.oauth2 import service_account
from googleapiclient.discovery import build
import strConstants as sc

FACNAME = 'Summary'
FACBEG  =  306
FACEND  = 321

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
rangeName = 'PrimaryTable!A:H'

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
    
    testbuild = {
    # enable Master / Detail
    "enableRangeSelection": True,
    "pagination": False,
    # the first Column is configured to use agGroupCellRenderer
    "columnDefs": [
        {'field': 'Sprint', 'editable':True,'sort':'asc'},
        {'field': 'Title',  'editable':True,},
        {'field': 'Status', 'width':125, 'editable':True,}, # 'pinned':'left',
        {'field': 'ReceivedDate', 'width':175, 'editable':False,},
        {'field': 'Analyst','editable':True,},
        {'field': 'Points', 'editable':True,},
        """
        {   'headerName': 'Extra',
             'field': 'groupExtra',
             'openByDefault':False,
             'children': [
                 {'field': 'Jan19', 'columnGroupShow':'open', 'editable':False, 'resizable':False, 'suppressSizeToFit':True, 'suppressAutoSize':True, 'filter':False, 'width':75, 'cellStyle':{'background-color':'lightblue'}},
                 {'field': 'Feb19', 'columnGroupShow':'open', 'editable':False, 'resizable':False, 'suppressSizeToFit':True, 'suppressAutoSize':True, 'filter':False, 'width':75, 'cellStyle':{'background-color':'lightblue'}},
                      'cellRenderer':'agAnimateShowChangeCellRenderer',},
                 ],
        },      
        """
    ],
    "defaultColDef": {
        "minColumnWidth": 75,
        'filterable': False,
        'sortable': False,
        'editable': True,
        'suppressMenu': True,
    },
    
    "onCellValueChanged":"--x_x--0_0-- function(e) { let api = e.api; let rowIndex = e.rowIndex; let col = e.column.colId; let rowNode = api.getDisplayedRowAtIndex(rowIndex); api.flashCells({ rowNodes: [rowNode], columns: [col], flashDelay: 10000000000 }); }; --x_x--0_0--"
    }
    
    return AgGrid(
        data=dfall,
        editable=True,
        gridOptions=testbuild,
        data_return_mode=DataReturnMode.AS_INPUT,
        update_mode=GridUpdateMode.VALUE_CHANGED|GridUpdateMode.FILTERING_CHANGED,
        fit_columns_on_grid_load=True,
        theme='light', 
        height=525, 
        allow_unsafe_jscode=True,
        enable_enterprise_modules=True,
        key='sprintBoardTableKey',
        )      

grid_response = displayTable(dfall)
dfgo = grid_response['data']

if dfall.equals(dfgo) == False:
        dfall = dfgo
        goog = dfgo.values.tolist()
        body = { 'values': goog }
        outputStart = FACBEG
        outputEnd   = FACEND
        service.spreadsheets().values().update(
                                        spreadsheetId=spreadsheetId, 
                                        range=rangeName,
                                        valueInputOption='USER_ENTERED', 
                                        body=body).execute()

def f(dat, c='lightblue'):
    return [f'background-color: {c}' for i in dat]

"""
#import xlsxwriter
from io import BytesIO

@st.cache
def convert_df():
    output = BytesIO()
    writer = pd.ExcelWriter(output, 
                            engine='xlsxwriter', 
                            engine_kwargs={'options':{'strings_to_numbers':True, 'in_memory': True}})
    for i in range(len(XLfacilityList)):
        dfall[dfall['FacilityName']==XLfacilityList[i]].style.apply(f, axis=0, subset=lockedMonths).to_excel(writer,
                                                                 sheet_name=XLfacilityList[i],
                                                                 index=False)
    writer.save()
    return output.getvalue() 


#### Populating the various bottom sections
col1, col2, col3, col4 = st.columns([1,1,1,1])
with col1:
    st.download_button(
        label="Download Excel workbook",
        data=convert_df(),
        file_name="Mamm2023Budget_export.xlsx",
        mime="application/vnd.ms-excel"
    )
#with col2:
#    st.markdown('Jan19-Aug22: Actuals')
#    st.markdown('Sep22-Dec22: Forecast')
#    st.markdown('Jan23-Dec23: Budget')

"""
    
    
    
    
    
    