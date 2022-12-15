# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 19:12:06 2022

@author: joshua.mcdonald
"""


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
    gb = GridOptionsBuilder.from_dataframe(dfall)
    gb.configure_default_column(rowDrag = False, rowDragManaged = True, rowDragEntireRow = False, rowDragMultiRow=True)
    gb.configure_column('Sprint', rowDrag = True, rowDragEntireRow = True)
    gb.configure_grid_options(rowDragManaged = True, onRowDragEnd = onRowDragEnd, deltaRowDataMode = True, getRowNodeId = getRowNodeId, onGridReady = onGridReady, animateRows = True, onRowDragMove = onRowDragMove)
    gridOptions = gb.build()
    return AgGrid(
        data=dfall,
        editable=True,
        gridOptions=gridOptions,
        data_return_mode=DataReturnMode.AS_INPUT,
        update_mode=GridUpdateMode.VALUE_CHANGED|GridUpdateMode.FILTERING_CHANGED,
        fit_columns_on_grid_load=True,
        theme='light', 
        height=750, 
        allow_unsafe_jscode=True,
        enable_enterprise_modules=True,
        key='sprintBoardTableKey',
        )      

grid_response = displayTable(dfall)
# st.write(grid_response['data'])
dfgo = grid_response['data']
saveButton = st.button("SAVE")

if saveButton:
        dfall = dfgo
        goog = dfgo.values.tolist()
        body = { 'values': goog }
        service.spreadsheets().values().update(
                                        spreadsheetId=spreadsheetId, 
                                        range='PrimaryTable!A2:F',
                                        valueInputOption='USER_ENTERED', 
                                        body=body).execute()


    
    
    
    
    