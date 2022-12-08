# -*- coding: utf-8 -*-

def facilityBuild():
    return {
        # enable Master / Detail
        "enableRangeSelection": True,
        "pagination": False,
        # the first Column is configured to use agGroupCellRenderer
        "columnDefs": [
            {'field': 'unid', 'hide': True,'editable':False,'sort':'asc'},
            {'field': 'FacilityName', 'hide': True,'editable':False,},
            {'field': 'AuditComment', 'hide': True,'editable':False,},
            {'field': 'ExamCategory', 'width':125, 'pinned':'left','editable':False, 'suppressSizeToFit':True},
            {'field': 'ExamType', 'width':175, 'pinned':'left','editable':False, 'suppressSizeToFit':True},
            {'field': 'SortInt', 'hide': True,'editable':False,},
            {'field': 'AuditUser', 'hide': True,'editable':False,},
            {'field': 'AuditComment', 'hide': True,'editable':False,},
            {'field': 'HistoricalVolumeFlag', 'hide':True,'editable':False,},
            
            {   'headerName': '2019',
                 'field': 'group2019',
                 'openByDefault':False,
                 'children': [
                     {'field': 'Jan19', 'columnGroupShow':'open', 'editable':False, 'resizable':False, 'suppressSizeToFit':True, 'suppressAutoSize':True, 'filter':False, 'width':75, 'cellStyle':{'background-color':'lightblue'}},
                     {'field': 'Feb19', 'columnGroupShow':'open', 'editable':False, 'resizable':False, 'suppressSizeToFit':True, 'suppressAutoSize':True, 'filter':False, 'width':75, 'cellStyle':{'background-color':'lightblue'}},
                     {'field': 'Mar19', 'columnGroupShow':'open', 'editable':False, 'resizable':False, 'suppressSizeToFit':True, 'suppressAutoSize':True, 'filter':False, 'width':75, 'cellStyle':{'background-color':'lightblue'}},
                     {'field': 'Apr19', 'columnGroupShow':'open', 'editable':False, 'resizable':False, 'suppressSizeToFit':True, 'suppressAutoSize':True, 'filter':False, 'width':75, 'cellStyle':{'background-color':'lightblue'}},
                     {'field': 'May19', 'columnGroupShow':'open', 'editable':False, 'resizable':False, 'suppressSizeToFit':True, 'suppressAutoSize':True, 'filter':False, 'width':75, 'cellStyle':{'background-color':'lightblue'}},
                     {'field': 'Jun19', 'columnGroupShow':'open', 'editable':False, 'resizable':False, 'suppressSizeToFit':True, 'suppressAutoSize':True, 'filter':False, 'width':75, 'cellStyle':{'background-color':'lightblue'}},
                     {'field': 'Jul19', 'columnGroupShow':'open', 'editable':False, 'resizable':False, 'suppressSizeToFit':True, 'suppressAutoSize':True, 'filter':False, 'width':75, 'cellStyle':{'background-color':'lightblue'}},
                     {'field': 'Aug19', 'columnGroupShow':'open', 'editable':False, 'resizable':False, 'suppressSizeToFit':True, 'suppressAutoSize':True, 'filter':False, 'width':75, 'cellStyle':{'background-color':'lightblue'}},
                     {'field': 'Sep19', 'columnGroupShow':'open', 'editable':False, 'resizable':False, 'suppressSizeToFit':True, 'suppressAutoSize':True, 'filter':False, 'width':75, 'cellStyle':{'background-color':'lightblue'}},
                     {'field': 'Oct19', 'columnGroupShow':'open', 'editable':False, 'resizable':False, 'suppressSizeToFit':True, 'suppressAutoSize':True, 'filter':False, 'width':75, 'cellStyle':{'background-color':'lightblue'}},
                     {'field': 'Nov19', 'columnGroupShow':'open', 'editable':False, 'resizable':False, 'suppressSizeToFit':True, 'suppressAutoSize':True, 'filter':False, 'width':75, 'cellStyle':{'background-color':'lightblue'}},
                     {'field': 'Dec19', 'columnGroupShow':'open', 'editable':False, 'resizable':False, 'suppressSizeToFit':True, 'suppressAutoSize':True, 'filter':False, 'width':75, 'cellStyle':{'background-color':'lightblue'}},
                     {'field': 'Total19', 'headerName':'Total', 'columnGroupShow':'closed', 'editable':False, 'resizable':False, 'suppressSizeToFit':True, 'suppressAutoSize':True, 'filter':False, 'width':100, 'cellStyle':{'background-color':'cadetblue'}, 
                          'valueGetter':'Number(data.Jan19)+Number(data.Feb19)+Number(data.Mar19)+Number(data.Apr19)+Number(data.May19)+Number(data.Jun19)+Number(data.Jul19)+Number(data.Aug19)+Number(data.Sep19)+Number(data.Oct19)+Number(data.Nov19)+Number(data.Dec19)',
                          'cellRenderer':'agAnimateShowChangeCellRenderer',},
                     ],
            },
            
            {   'headerName': '2020',
                 'field': 'group2020',
                 'openByDefault':False,
                 'children': [
                     {'field': 'Jan20', 'columnGroupShow':'open', 'editable':False, 'resizable':False, 'suppressSizeToFit':True, 'suppressAutoSize':True, 'filter':False, 'width':75, 'cellStyle':{'background-color':'lightblue'}},
                     {'field': 'Feb20', 'columnGroupShow':'open', 'editable':False, 'resizable':False, 'suppressSizeToFit':True, 'suppressAutoSize':True, 'filter':False, 'width':75, 'cellStyle':{'background-color':'lightblue'}},
                     {'field': 'Mar20', 'columnGroupShow':'open', 'editable':False, 'resizable':False, 'suppressSizeToFit':True, 'suppressAutoSize':True, 'filter':False, 'width':75, 'cellStyle':{'background-color':'lightblue'}},
                     {'field': 'Apr20', 'columnGroupShow':'open', 'editable':False, 'resizable':False, 'suppressSizeToFit':True, 'suppressAutoSize':True, 'filter':False, 'width':75, 'cellStyle':{'background-color':'lightblue'}},
                     {'field': 'May20', 'columnGroupShow':'open', 'editable':False, 'resizable':False, 'suppressSizeToFit':True, 'suppressAutoSize':True, 'filter':False, 'width':75, 'cellStyle':{'background-color':'lightblue'}},
                     {'field': 'Jun20', 'columnGroupShow':'open', 'editable':False, 'resizable':False, 'suppressSizeToFit':True, 'suppressAutoSize':True, 'filter':False, 'width':75, 'cellStyle':{'background-color':'lightblue'}},
                     {'field': 'Jul20', 'columnGroupShow':'open', 'editable':False, 'resizable':False, 'suppressSizeToFit':True, 'suppressAutoSize':True, 'filter':False, 'width':75, 'cellStyle':{'background-color':'lightblue'}},
                     {'field': 'Aug20', 'columnGroupShow':'open', 'editable':False, 'resizable':False, 'suppressSizeToFit':True, 'suppressAutoSize':True, 'filter':False, 'width':75, 'cellStyle':{'background-color':'lightblue'}},
                     {'field': 'Sep20', 'columnGroupShow':'open', 'editable':False, 'resizable':False, 'suppressSizeToFit':True, 'suppressAutoSize':True, 'filter':False, 'width':75, 'cellStyle':{'background-color':'lightblue'}},
                     {'field': 'Oct20', 'columnGroupShow':'open', 'editable':False, 'resizable':False, 'suppressSizeToFit':True, 'suppressAutoSize':True, 'filter':False, 'width':75, 'cellStyle':{'background-color':'lightblue'}},
                     {'field': 'Nov20', 'columnGroupShow':'open', 'editable':False, 'resizable':False, 'suppressSizeToFit':True, 'suppressAutoSize':True, 'filter':False, 'width':75, 'cellStyle':{'background-color':'lightblue'}},
                     {'field': 'Dec20', 'columnGroupShow':'open', 'editable':False, 'resizable':False, 'suppressSizeToFit':True, 'suppressAutoSize':True, 'filter':False, 'width':75, 'cellStyle':{'background-color':'lightblue'}},
                     {'field': 'Total20', 'headerName':'Total', 'columnGroupShow':'closed', 'editable':False, 'resizable':False, 'suppressSizeToFit':True, 'suppressAutoSize':True, 'filter':False, 'width':100, 'cellStyle':{'background-color':'cadetblue'}, 
                          'valueGetter':'Number(data.Jan20)+Number(data.Feb20)+Number(data.Mar20)+Number(data.Apr20)+Number(data.May20)+Number(data.Jun20)+Number(data.Jul20)+Number(data.Aug20)+Number(data.Sep20)+Number(data.Oct20)+Number(data.Nov20)+Number(data.Dec20)',
                          'cellRenderer':'agAnimateShowChangeCellRenderer',},
                     ],
            },
            
            {   'headerName': '2021',
                 'field': 'group2021',
                 'openByDefault':False,
                 'children': [
                     {'field': 'Jan21', 'columnGroupShow':'open', 'editable':False, 'resizable':False, 'suppressSizeToFit':True, 'suppressAutoSize':True, 'filter':False, 'width':75, 'cellStyle':{'background-color':'lightblue'}},
                     {'field': 'Feb21', 'columnGroupShow':'open', 'editable':False, 'resizable':False, 'suppressSizeToFit':True, 'suppressAutoSize':True, 'filter':False, 'width':75, 'cellStyle':{'background-color':'lightblue'}},
                     {'field': 'Mar21', 'columnGroupShow':'open', 'editable':False, 'resizable':False, 'suppressSizeToFit':True, 'suppressAutoSize':True, 'filter':False, 'width':75, 'cellStyle':{'background-color':'lightblue'}},
                     {'field': 'Apr21', 'columnGroupShow':'open', 'editable':False, 'resizable':False, 'suppressSizeToFit':True, 'suppressAutoSize':True, 'filter':False, 'width':75, 'cellStyle':{'background-color':'lightblue'}},
                     {'field': 'May21', 'columnGroupShow':'open', 'editable':False, 'resizable':False, 'suppressSizeToFit':True, 'suppressAutoSize':True, 'filter':False, 'width':75, 'cellStyle':{'background-color':'lightblue'}},
                     {'field': 'Jun21', 'columnGroupShow':'open', 'editable':False, 'resizable':False, 'suppressSizeToFit':True, 'suppressAutoSize':True, 'filter':False, 'width':75, 'cellStyle':{'background-color':'lightblue'}},
                     {'field': 'Jul21', 'columnGroupShow':'open', 'editable':False, 'resizable':False, 'suppressSizeToFit':True, 'suppressAutoSize':True, 'filter':False, 'width':75, 'cellStyle':{'background-color':'lightblue'}},
                     {'field': 'Aug21', 'columnGroupShow':'open', 'editable':False, 'resizable':False, 'suppressSizeToFit':True, 'suppressAutoSize':True, 'filter':False, 'width':75, 'cellStyle':{'background-color':'lightblue'}},
                     {'field': 'Sep21', 'columnGroupShow':'open', 'editable':False, 'resizable':False, 'suppressSizeToFit':True, 'suppressAutoSize':True, 'filter':False, 'width':75, 'cellStyle':{'background-color':'lightblue'}},
                     {'field': 'Oct21', 'columnGroupShow':'open', 'editable':False, 'resizable':False, 'suppressSizeToFit':True, 'suppressAutoSize':True, 'filter':False, 'width':75, 'cellStyle':{'background-color':'lightblue'}},
                     {'field': 'Nov21', 'columnGroupShow':'open', 'editable':False, 'resizable':False, 'suppressSizeToFit':True, 'suppressAutoSize':True, 'filter':False, 'width':75, 'cellStyle':{'background-color':'lightblue'}},
                     {'field': 'Dec21', 'columnGroupShow':'open', 'editable':False, 'resizable':False, 'suppressSizeToFit':True, 'suppressAutoSize':True, 'filter':False, 'width':75, 'cellStyle':{'background-color':'lightblue'}},
                     {'field': 'Total21', 'headerName':'Total', 'columnGroupShow':'closed', 'editable':False, 'resizable':False, 'suppressSizeToFit':True, 'suppressAutoSize':True, 'filter':False, 'width':100, 'cellStyle':{'background-color':'cadetblue'}, 
                          'valueGetter':'Number(data.Jan21)+Number(data.Feb21)+Number(data.Mar21)+Number(data.Apr21)+Number(data.May21)+Number(data.Jun21)+Number(data.Jul21)+Number(data.Aug21)+Number(data.Sep21)+Number(data.Oct21)+Number(data.Nov21)+Number(data.Dec21)',
                          'cellRenderer':'agAnimateShowChangeCellRenderer',},
                     ],
            },
            
            {   'headerName': '2022',
                 'field': 'group2022',
                 'openByDefault':True,
                 'children': [
                     {'field': 'Jan22', 'columnGroupShow':'open', 'editable':False, 'resizable':False, 'suppressSizeToFit':True, 'suppressAutoSize':True, 'filter':False, 'width':75, 'cellStyle':{'background-color':'lightblue'}},
                     {'field': 'Feb22', 'columnGroupShow':'open', 'editable':False, 'resizable':False, 'suppressSizeToFit':True, 'suppressAutoSize':True, 'filter':False, 'width':75, 'cellStyle':{'background-color':'lightblue'}},
                     {'field': 'Mar22', 'columnGroupShow':'open', 'editable':False, 'resizable':False, 'suppressSizeToFit':True, 'suppressAutoSize':True, 'filter':False, 'width':75, 'cellStyle':{'background-color':'lightblue'}},
                     {'field': 'Apr22', 'columnGroupShow':'open', 'editable':False, 'resizable':False, 'suppressSizeToFit':True, 'suppressAutoSize':True, 'filter':False, 'width':75, 'cellStyle':{'background-color':'lightblue'}},
                     {'field': 'May22', 'columnGroupShow':'open', 'editable':False, 'resizable':False, 'suppressSizeToFit':True, 'suppressAutoSize':True, 'filter':False, 'width':75, 'cellStyle':{'background-color':'lightblue'}},
                     {'field': 'Jun22', 'columnGroupShow':'open', 'editable':False, 'resizable':False, 'suppressSizeToFit':True, 'suppressAutoSize':True, 'filter':False, 'width':75, 'cellStyle':{'background-color':'lightblue'}},
                     {'field': 'Jul22', 'columnGroupShow':'open', 'editable':False, 'resizable':False, 'suppressSizeToFit':True, 'suppressAutoSize':True, 'filter':False, 'width':75, 'cellStyle':{'background-color':'lightblue'}},
                     {'field': 'Aug22', 'columnGroupShow':'open', 'editable':False, 'resizable':False, 'suppressSizeToFit':True, 'suppressAutoSize':True, 'filter':False, 'width':75, 'cellStyle':{'background-color':'lightblue'}},
                     {'field': 'Sep22', 'columnGroupShow':'open', 'editable':False, 'resizable':False, 'suppressSizeToFit':True, 'suppressAutoSize':True, 'filter':False, 'width':75, 'cellStyle':{'background-color':'lightblue'}},
                     {'field': 'Oct22', 'columnGroupShow':'open', 'editable':False, 'resizable':False, 'suppressSizeToFit':True, 'suppressAutoSize':True, 'filter':False, 'width':75, 'cellStyle':{'background-color':'lightblue'}},
                     {'field': 'Nov22', 'columnGroupShow':'open', 'editable':False, 'resizable':False, 'suppressSizeToFit':True, 'suppressAutoSize':True, 'filter':False, 'width':75, 'cellStyle':{'background-color':'lightblue'}},
                     {'field': 'Dec22', 'columnGroupShow':'open', 'editable':True, 'resizable':False, 'suppressSizeToFit':True, 'suppressAutoSize':True, 'filter':False, 'width':75},
                     {'field': 'Total22', 'headerName':'Total', 'columnGroupShow':'closed', 'editable':False, 'resizable':False, 'suppressSizeToFit':True, 'suppressAutoSize':True, 'filter':False, 'width':100, 
                          'valueGetter':'Number(data.Jan22)+Number(data.Feb22)+Number(data.Mar22)+Number(data.Apr22)+Number(data.May22)+Number(data.Jun22)+Number(data.Jul22)+Number(data.Aug22)+Number(data.Sep22)+Number(data.Oct22)+Number(data.Nov22)+Number(data.Dec22)',
                          'cellRenderer':'agAnimateShowChangeCellRenderer',},
                     ],
            },
            
            {   'headerName': '2023',
                 'field': 'group2023',
                 'openByDefault':True,
                 'children': [
                     {'field': 'Jan23', 'columnGroupShow':'open', 'editable':True, 'resizable':False, 'suppressSizeToFit':True, 'suppressAutoSize':True, 'filter':False, 'width':75},
                     {'field': 'Feb23', 'columnGroupShow':'open', 'editable':True, 'resizable':False, 'suppressSizeToFit':True, 'suppressAutoSize':True, 'filter':False, 'width':75},
                     {'field': 'Mar23', 'columnGroupShow':'open', 'editable':True, 'resizable':False, 'suppressSizeToFit':True, 'suppressAutoSize':True, 'filter':False, 'width':75},
                     {'field': 'Apr23', 'columnGroupShow':'open', 'editable':True, 'resizable':False, 'suppressSizeToFit':True, 'suppressAutoSize':True, 'filter':False, 'width':75},
                     {'field': 'May23', 'columnGroupShow':'open', 'editable':True, 'resizable':False, 'suppressSizeToFit':True, 'suppressAutoSize':True, 'filter':False, 'width':75},
                     {'field': 'Jun23', 'columnGroupShow':'open', 'editable':True, 'resizable':False, 'suppressSizeToFit':True, 'suppressAutoSize':True, 'filter':False, 'width':75},
                     {'field': 'Jul23', 'columnGroupShow':'open', 'editable':True, 'resizable':False, 'suppressSizeToFit':True, 'suppressAutoSize':True, 'filter':False, 'width':75},
                     {'field': 'Aug23', 'columnGroupShow':'open', 'editable':True, 'resizable':False, 'suppressSizeToFit':True, 'suppressAutoSize':True, 'filter':False, 'width':75},
                     {'field': 'Sep23', 'columnGroupShow':'open', 'editable':True, 'resizable':False, 'suppressSizeToFit':True, 'suppressAutoSize':True, 'filter':False, 'width':75},
                     {'field': 'Oct23', 'columnGroupShow':'open', 'editable':True, 'resizable':False, 'suppressSizeToFit':True, 'suppressAutoSize':True, 'filter':False, 'width':75},
                     {'field': 'Nov23', 'columnGroupShow':'open', 'editable':True, 'resizable':False, 'suppressSizeToFit':True, 'suppressAutoSize':True, 'filter':False, 'width':75},
                     {'field': 'Dec23', 'columnGroupShow':'open', 'editable':True, 'resizable':False, 'suppressSizeToFit':True, 'suppressAutoSize':True, 'filter':False, 'width':75},
                     {'field': 'Total23', 'headerName':'Total', 'columnGroupShow':'closed', 'editable':False, 'resizable':False, 'suppressSizeToFit':True, 'suppressAutoSize':True, 'filter':False, 'width':100, 
                          'valueGetter':'Number(data.Jan23)+Number(data.Feb23)+Number(data.Mar23)+Number(data.Apr23)+Number(data.May23)+Number(data.Jun23)+Number(data.Jul23)+Number(data.Aug23)+Number(data.Sep23)+Number(data.Oct23)+Number(data.Nov23)+Number(data.Dec23)',
                          'cellRenderer':'agAnimateShowChangeCellRenderer',},
                     ],
            },
            
            {   'headerName': 'Financials',
                 'field': 'financialscol',
                 'openByDefault':True,
                 'children': [
                     {'field': 'growth1920', 'headerName':'19A->20A', 'columnGroupShow':'open', 'editable':False, 'resizable':False, 'suppressSizeToFit':True, 'suppressAutoSize':True, 'filter':False, 'width':100,
                      'valueGetter':"""
    if ( isNaN(
      Number(data.Jan19)+Number(data.Feb19)+Number(data.Mar19)+Number(data.Apr19)+
      Number(data.May19)+Number(data.Jun19)+Number(data.Jul19)+Number(data.Aug19)+
      Number(data.Sep19)+Number(data.Oct19)+Number(data.Nov19)+Number(data.Dec19)
      ) ) { return ''; } 
    else { return (
      100*(
       (Number(data.Jan20)+Number(data.Feb20)+Number(data.Mar20)+Number(data.Apr20)+
        Number(data.May20)+Number(data.Jun20)+Number(data.Jul20)+Number(data.Aug20)+
        Number(data.Sep20)+Number(data.Oct20)+Number(data.Nov20)+Number(data.Dec20))
           /
       (Number(data.Jan19)+Number(data.Feb19)+Number(data.Mar19)+Number(data.Apr19)+
        Number(data.May19)+Number(data.Jun19)+Number(data.Jul19)+Number(data.Aug19)+
        Number(data.Sep19)+Number(data.Oct19)+Number(data.Nov19)+Number(data.Dec19))
           -1)).toFixed(1)+'%';}""" },
                     
                    {'field': 'growth2021', 'headerName':'20A->21A',  'columnGroupShow':'open', 'editable':False, 'resizable':False, 'suppressSizeToFit':True, 'suppressAutoSize':True, 'filter':False, 'width':100,
                     'valueGetter':"""
    if ( 
    isNaN(
    ((
      Number(data.Jan21)+Number(data.Feb21)+Number(data.Mar21)+Number(data.Apr21)+Number(data.May21)+Number(data.Jun21)+Number(data.Jul21)+Number(data.Aug21)+Number(data.Sep21)+Number(data.Oct21)+Number(data.Nov21)+Number(data.Dec21)
      )/(
      Number(data.Jan20)+Number(data.Feb20)+Number(data.Mar20)+Number(data.Apr20)+Number(data.May20)+Number(data.Jun20)+Number(data.Jul20)+Number(data.Aug20)+Number(data.Sep20)+Number(data.Oct20)+Number(data.Nov20)+Number(data.Dec20)
                                                                                                                                                                                                                                            )-1).toFixed(2)
    ) 
    ) { return ''; } 
    else { return (100*((
        Number(data.Jan21)+Number(data.Feb21)+Number(data.Mar21)+Number(data.Apr21)+Number(data.May21)+Number(data.Jun21)+Number(data.Jul21)+Number(data.Aug21)+Number(data.Sep21)+Number(data.Oct21)+Number(data.Nov21)+Number(data.Dec21)
        )/(
        Number(data.Jan20)+Number(data.Feb20)+Number(data.Mar20)+Number(data.Apr20)+Number(data.May20)+Number(data.Jun20)+Number(data.Jul20)+Number(data.Aug20)+Number(data.Sep20)+Number(data.Oct20)+Number(data.Nov20)+Number(data.Dec20)
    )-1)).toFixed(1)+'%';}""" },
                     {'field': 'growth2122', 'headerName':'21A->22F',  'columnGroupShow':'open', 'editable':False, 'resizable':False, 'suppressSizeToFit':True, 'suppressAutoSize':True, 'filter':False, 'width':100,
                     'valueGetter':"""
    if ( 
    isNaN(
    ((
      Number(data.Jan22)+Number(data.Feb22)+Number(data.Mar22)+Number(data.Apr22)+Number(data.May22)+Number(data.Jun22)+Number(data.Jul22)+Number(data.Aug22)+Number(data.Sep22)+Number(data.Oct22)+Number(data.Nov22)+Number(data.Dec22)
      )/(
      Number(data.Jan21)+Number(data.Feb21)+Number(data.Mar21)+Number(data.Apr21)+Number(data.May21)+Number(data.Jun21)+Number(data.Jul21)+Number(data.Aug21)+Number(data.Sep21)+Number(data.Oct21)+Number(data.Nov21)+Number(data.Dec21)
                                                                                                                                                                                                                                            )-1).toFixed(2)
    ) 
    ) { return ''; } 
    else { return (100*((
        Number(data.Jan22)+Number(data.Feb22)+Number(data.Mar22)+Number(data.Apr22)+Number(data.May22)+Number(data.Jun22)+Number(data.Jul22)+Number(data.Aug22)+Number(data.Sep22)+Number(data.Oct22)+Number(data.Nov22)+Number(data.Dec22)
        )/(
        Number(data.Jan21)+Number(data.Feb21)+Number(data.Mar21)+Number(data.Apr21)+Number(data.May21)+Number(data.Jun21)+Number(data.Jul21)+Number(data.Aug21)+Number(data.Sep21)+Number(data.Oct21)+Number(data.Nov21)+Number(data.Dec21)
        )-1)).toFixed(1)+'%';}"""},
                     {'field': 'growth2223', 'headerName':'22F->23B',  'columnGroupShow':'open', 'editable':False, 'resizable':False, 'suppressSizeToFit':True, 'suppressAutoSize':True, 'filter':False, 'width':100,
                     'valueGetter':"""
    if ( 
    isNaN(
    ((
      Number(data.Jan23)+Number(data.Feb23)+Number(data.Mar23)+Number(data.Apr23)+Number(data.May23)+Number(data.Jun23)+Number(data.Jul23)+Number(data.Aug23)+Number(data.Sep23)+Number(data.Oct23)+Number(data.Nov23)+Number(data.Dec23)
      )/(
      Number(data.Jan22)+Number(data.Feb22)+Number(data.Mar22)+Number(data.Apr22)+Number(data.May22)+Number(data.Jun22)+Number(data.Jul22)+Number(data.Aug22)+Number(data.Sep22)+Number(data.Oct22)+Number(data.Nov22)+Number(data.Dec22)
                                                                                                                                                                                                                                            )-1).toFixed(2)
    ) 
    ) { return ''; } 
    else { return (100*((
        Number(data.Jan23)+Number(data.Feb23)+Number(data.Mar23)+Number(data.Apr23)+Number(data.May23)+Number(data.Jun23)+Number(data.Jul23)+Number(data.Aug23)+Number(data.Sep23)+Number(data.Oct23)+Number(data.Nov23)+Number(data.Dec23)
        )/(
        Number(data.Jan22)+Number(data.Feb22)+Number(data.Mar22)+Number(data.Apr22)+Number(data.May22)+Number(data.Jun22)+Number(data.Jul22)+Number(data.Aug22)+Number(data.Sep22)+Number(data.Oct22)+Number(data.Nov22)+Number(data.Dec22)
        )-1)).toFixed(1)+'%';}"""},
                     {'field': 'cagr3', 'headerName':'3yr CAGR%',  'columnGroupShow':'open', 'editable':False, 'resizable':False, 'suppressSizeToFit':True, 'suppressAutoSize':True, 'filter':False, 'width':100,
                     'valueGetter':"""
    if ( 
    isNaN(
    ((
      Number(data.Jan20)+Number(data.Feb20)+Number(data.Mar20)+Number(data.Apr20)+Number(data.May20)+Number(data.Jun20)+Number(data.Jul20)+Number(data.Aug20)+Number(data.Sep20)+Number(data.Oct20)+Number(data.Nov20)+Number(data.Dec20)
      )/(
      Number(data.Jan19)+Number(data.Feb19)+Number(data.Mar19)+Number(data.Apr19)+Number(data.May19)+Number(data.Jun19)+Number(data.Jul19)+Number(data.Aug19)+Number(data.Sep19)+Number(data.Oct19)+Number(data.Nov19)+Number(data.Dec19)
                                                                                                                                                                                                                                            )-1).toFixed(2)
    ) 
    ) { return ''; } 
    else { return (100*((
        (Number(data.Jan22)+Number(data.Feb22)+Number(data.Mar22)+Number(data.Apr22)+Number(data.May22)+Number(data.Jun22)+Number(data.Jul22)+Number(data.Aug22)+Number(data.Sep22)+Number(data.Oct22)+Number(data.Nov22)+Number(data.Dec22)
        )/(
           Number(data.Jan19)+Number(data.Feb19)+Number(data.Mar19)+Number(data.Apr19)+Number(data.May19)+Number(data.Jun19)+Number(data.Jul19)+Number(data.Aug19)+Number(data.Sep19)+Number(data.Oct19)+Number(data.Nov19)+Number(data.Dec19)
    ))**(1/3)-1)).toFixed(1)+'%';}"""},
           
           
           
                     ],
            },
            
           
           {'field': 'AuditComment', 'width':700, 'editable':True, 'suppressSizeToFit':True},
            
            
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