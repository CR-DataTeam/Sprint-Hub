
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
    ".ag-root.ag-unselectable.ag-layout-normal": {"font-size": "10px !important",}}
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


############################################################
sprintDropDown=('not prioritized',
                'Sprint TBD',
                'Sprint 00 (ends 12/30)',
                'Sprint 01 (ends 01/13)',
                'Sprint 02 (ends 01/27)')

teamList=('Joshua McDonald','Zimean Vickers','Ian Stewart','Michael Gallemore')

taskStatus=('Open','Closed','Blocked','On Hold')


############################################################

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
gb.configure_column('Project',width=400,rowDrag=False) 
gb.configure_column('Status',width=80,cellEditor='agSelectCellEditor',cellEditorParams={'values':taskStatus},rowDrag=False) 
gb.configure_column('ReceivedDate',width=90,rowDrag=False) 
gb.configure_column('Analyst',width=90,cellEditor='agSelectCellEditor',cellEditorParams={'values':teamList},rowDrag=False)
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
        height=500, 
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
    

ucdfa = dfgo[dfgo['Sprint']=='Sprint 00 (ends 12/30)']
ucdfj = ucdfa[ucdfa['Analyst']=='Joshua McDonald']
ucdfz = ucdfa[ucdfa['Analyst']=='Zimean Vickers']
ucdfi = ucdfa[ucdfa['Analyst']=='Ian Stewart']
ucdfm = ucdfa[ucdfa['Analyst']=='Michael Gallemore']

ucdfah = ucdfa['Effort'].astype(int).sum()
ucdfjh = ucdfj['Effort'].astype(int).sum()
ucdfzh = ucdfz['Effort'].astype(int).sum()
ucdfih = ucdfi['Effort'].astype(int).sum()
ucdfmh = ucdfm['Effort'].astype(int).sum()

if ucdfjh < 8:      
    joshStatus = "Healthy Capacity" 
    joshSC = 'green'
elif ucdfjh == 8:   
    joshStatus = "At Capacity" 
    joshSC = 'yellow'
else:               
    joshStatus = "Over-Capacity"
    joshSC = 'red'
    
if ucdfzh < 8:      
    zimeanStatus = "Healthy Capacity" 
    zimeanSC = 'green'
elif ucdfzh == 8:   
    zimeanStatus = "At Capacity" 
    zimeanSC = 'yellow'
else:               
    zimeanStatus = "Over-Capacity"
    zimeanSC = 'red'
    
if ucdfih < 8:      
    ianStatus = "Healthy Capacity" 
    ianSC = 'green'
elif ucdfih == 8:   
    ianStatus = "At Capacity" 
    ianSC = 'yellow'
else:               
    ianStatus = "Over-Capacity"
    ianSC = 'red'
    
if ucdfmh < 8:      
    michaelStatus = "Healthy Capacity" 
    michaelSC = 'green'
elif ucdfmh == 8:   
    michaelStatus = "At Capacity" 
    michaelSC = 'yellow'
else:               
    michaelStatus = "Over-Capacity"
    michaelSC = 'red'

with st.sidebar:
    st.markdown(body='**Sprint 00**<br>',unsafe_allow_html=True)
    st.markdown(body='**Josh**<br><span style="color:'+joshSC+'">'+joshStatus+'</span><br><sup>('+str(ucdfjh)+')</sup>',unsafe_allow_html=True)
    st.markdown(body='**Zimean**<br><span style="color:'+zimeanSC+'">'+zimeanStatus+'</span><br><sup>('+str(ucdfzh)+')</sup>',unsafe_allow_html=True)
    st.markdown(body='**Ian**<br><span style="color:'+ianSC+'">'+ianStatus+'</span><br><sup>('+str(ucdfih)+')</sup>',unsafe_allow_html=True)
    st.markdown(body='**Michael**<br><span style="color:'+michaelSC+'">'+michaelStatus+'</span><br><sup>('+str(ucdfmh)+')</sup>',unsafe_allow_html=True)
    
    # st.metric('Josh ----------',value=ucdfjh,delta=8-int(ucdfjh),)
    # st.metric('Zimean --------',value=ucdfzh,delta=8-int(ucdfzh),)
    # st.metric('Ian -----------',value=ucdfih,delta=8-int(ucdfih),)
    # st.metric('Michael -------',value=ucdfmh,delta=8-int(ucdfmh),)
    # st.metric('TEAM TOTAL ----',value=ucdfah,delta=32-int(ucdfah),)

    
with st.form("newtask"):
   st.write("Add New Project")
   formName = st.text_input("Project")
   formAnalyst = st.text_input("Analyst")

   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   definecols = ['Sprint','Project','Status','ReceivedDate','Analyst','Effort']
   if submitted:
       st.write("Thanks!")
       formdf = pd.DataFrame(['not prioritized', formName, 'Open', '2022-12-15', formAnalyst, 0]).T
       formdf.columns = definecols
       goog = formdf.values.tolist()
       body = { 'values': goog }
       service.spreadsheets().values().append(
                                               spreadsheetId=spreadsheetId, 
                                               range='PrimaryTable!A2:F',
                                               valueInputOption='USER_ENTERED', 
                                               body=body).execute() 
       st.experimental_rerun()
    
    
    