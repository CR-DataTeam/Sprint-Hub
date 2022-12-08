
def generatePage(facility_name, facility_startrow, facility_endrow):
    import pandas as pd
    import streamlit as st
    from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode, JsCode
    from datetime import datetime, timezone
    import zoneinfo 
    from google.oauth2 import service_account
    from googleapiclient.discovery import build
    import strConstants as sc
    import colDefDictionary
    
    FACNAME = facility_name
    FACBEG  =  facility_startrow
    FACEND  = facility_endrow

    st.set_page_config(
         page_title=FACNAME,
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


    ###############################################################################
    #### set-up basis for iteration
    ###############################################################################

    creds = service_account.Credentials.from_service_account_file(
        'serviceacc.json',
        scopes=['https://www.googleapis.com/auth/spreadsheets'],
        )
    service = build('sheets', 'v4', credentials=creds, cache_discovery=False)
    spreadsheetId = '1-zYgl-7ffj8cV2N80aICDHHKHfqyQX5rE3HXDcgSsfc'

    def fetchData():
        rangeName = 'CurrentFacilityValues!A1:BO305'
        result = service.spreadsheets().values().get(
            spreadsheetId=spreadsheetId, range=rangeName).execute()
        
        #### Assign GET request to dfpiv.
        df = pd.DataFrame(result['values'])
        df.columns = df.iloc[0]
        dfpiv = df[1:]
        
        #### Filter to only the current page's facility.
        dfit = dfpiv[dfpiv['FacilityName']==FACNAME]
        return dfit
        
    dfit = fetchData()
    
    def displayTable(df: pd.DataFrame) -> AgGrid:
        setGridOptions = colDefDictionary.facilityBuild()
        naming = FACNAME.replace(' ','')
        return AgGrid(
            data=dfit,
            editable=True,
            gridOptions=setGridOptions,
            data_return_mode=DataReturnMode.AS_INPUT,
            update_mode=GridUpdateMode.VALUE_CHANGED|GridUpdateMode.FILTERING_CHANGED,
            fit_columns_on_grid_load=True,
            theme='light', 
            height=525, 
            allow_unsafe_jscode=True,
            enable_enterprise_modules=True,
            key=f'aggrid_{naming}_key',
            )      

    grid_response = displayTable(dfit)
    dfgo = grid_response['data']
    
    if dfit.equals(dfgo) == False:
        dfit = dfgo
        goog = dfgo.values.tolist()
        body = { 'values': goog }
        outputStart = FACBEG
        outputEnd   = FACEND
        service.spreadsheets().values().update(
                                        spreadsheetId=spreadsheetId, 
                                        range=f'CurrentFacilityValues!A{outputStart}:BO{outputEnd}',
                                        valueInputOption='USER_ENTERED', 
                                        body=body).execute()
        
    
    
    ###############################################################################
    #### define columns for sections underneath table
    ###############################################################################    
    
    #### GET Audit Data to determine facility's latest Audit Entry Date & User.
    result = service.spreadsheets().values().get(spreadsheetId=spreadsheetId, 
                                                 range='AuditLog!A:BQ'
                                                 ).execute()
    df_fullAudit = pd.DataFrame(result['values'])
    df_fullAudit.columns = df_fullAudit.iloc[0]
    dfpiva = df_fullAudit[1:] 
    
    latestAuditDate = dfpiva[dfpiva['FacilityName']==FACNAME]['AuditDateTime'].max()
    latestAuditUser = dfpiva[dfpiva['AuditDateTime']==latestAuditDate]['AuditUser'].max()
        
    #### Populating the various bottom sections
    col1, col2, col3, col4 = st.columns([1,1,1,1])
    with col1:
        latestAuditUserText = 'Latest Audit User:    ' + str(latestAuditUser) #ALT+0160
        latestAuditDateText = 'Latest Audit Date:    ' + str(latestAuditDate)
        st.markdown(f'{latestAuditUserText}')
        st.markdown(f'{latestAuditDateText}')
    #with col2:
    #    st.markdown('Jan19-Aug22: Actuals')
    #    st.markdown('Sep22-Dec22: Forecast')
    #    st.markdown('Jan23-Dec23: Budget')
    with col3:
        auditUser = st.text_input('Enter name: (required)', value='',)
    with col4:
        st.text('')
        st.text('')
        submissionButton = st.button("Submit Budget Entry")  
        
    #### Logic for when the Submission Button is pressed!
    if submissionButton:
        if len(auditUser) >0:
            auditTime = datetime.now().replace(tzinfo=zoneinfo.ZoneInfo('US/Eastern')).strftime('%Y-%m-%d %H:%M:%S')
            dfgo['AuditUser'] = str(auditUser)
            dfgo['AuditDateTime'] = str(auditTime)
            goog = dfgo.values.tolist()
            body = { 'values': goog }
            outputStart = FACBEG
            outputEnd   = FACEND
            service.spreadsheets().values().update(
                                                    spreadsheetId=spreadsheetId, 
                                                    range=f'CurrentFacilityValues!A{outputStart}:BQ{outputEnd}',
                                                    valueInputOption='RAW', 
                                                    body=body).execute()
            service.spreadsheets().values().append(
                                                    spreadsheetId=spreadsheetId, 
                                                    range='AuditLog!A:BQ',
                                                    valueInputOption='USER_ENTERED', 
                                                    body=body).execute()
            userMessage=''
            st.balloons()
            st.experimental_rerun()
        else:
            with col3:
                userMessage = 'Please enter a name.'
                st.error(userMessage)


     