
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
    
custom_css = {
    ".ag-root.ag-unselectable.ag-layout-normal": {"font-size": "9px !important",}}
    # "font-family": "Roboto, sans-serif !important;"},
    #".ag-header-cell-text": {"color": "#495057 !important;"},
    # }    

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
sprintDropDown=('not prioritized',
                'Sprint TBD',
                'Sprint 00 (ends 12/30)',
                'Sprint 01 (ends 01/13)',
                'Sprint 02 (ends 01/27)')
gb = GridOptionsBuilder.from_dataframe(dfall)
gb.configure_default_column(rowDrag = True, 
                            rowDragManaged = True, 
                            rowDragEntireRow = False, 
                            rowDragMultiRow=True,
                            minColumnWidth=50,
                            filterable=True,
                            sortable=False,
                            editable=True,
                            suppressMenu=False,)
gb.configure_column('Sprint',width=175,cellEditor='agSelectCellEditor',cellEditorParams={'values':sprintDropDown},rowDrag = True, rowDragEntireRow = True)
gb.configure_column('Project',width=400) 
gb.configure_column('Status',width=80,rowDrag=False) 
gb.configure_column('ReceivedDate',width=90,rowDrag=False) 
gb.configure_column('Analyst',width=90,rowDrag=False)
gb.configure_column('Effort',width=65,rowDrag=False)
gb.configure_side_bar()
gb.configure_selection(selection_mode="multiple", use_checkbox=True)
gb.configure_grid_options(rowDragManaged=True,
    rowDragEntireRow=True,
    rowDragMultiRow=True,
    rowDrag=True,
    onCellValueChanged="--x_x--0_0-- function(e) { let api = e.api; let rowIndex = e.rowIndex; let col = e.column.colId; let rowNode = api.getDisplayedRowAtIndex(rowIndex); api.flashCells({ rowNodes: [rowNode], columns: [col], flashDelay: 10000000000 }); }; --x_x--0_0--"
    )
gridOptions = gb.build()

grid_response = AgGrid(
        data=dfall,
        gridOptions=gridOptions,
        data_return_mode=DataReturnMode.AS_INPUT,
        update_mode=GridUpdateMode.MODEL_CHANGED,
        fit_columns_on_grid_load=True,
        enable_enterprise_modules=True,
        theme='light', 
        height=600, 
        allow_unsafe_jscode=True,
        key='sprintBoardTableKey',
        custom_css=custom_css
        )      


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
    

sidebar_track_df = dfgo[dfgo['Sprint']=='Sprint 00 (ends 12/30)']
sbEff = sidebar_track_df['Effort'].astype(int).sum()



with st.sidebar:
    st.metric('Josh - \r\nNext Sprint',value=sbEff,delta=8-int(sbEff),)#delta_color=)

    
    
    
    
    