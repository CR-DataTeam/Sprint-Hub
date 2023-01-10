# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 12:10:50 2022

@author: joshua.mcdonald
"""
# Originally 165px:
sidebarWidth = """
     <style>
     [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
         width: 225px;
       }
       [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
           width: 225px;
           margin-left: -225px;
        }
        </style>
        """
# Under footer line:
#     .sidebar-text {
#         font-size: 0.75rem;
hideStreamlitStyle = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
}
</style>

"""

adjustPaddingAndFont = """
        <style>
               .css-18e3th9 {
                    padding-top: 0rem;
                    padding-bottom: 2rem;
                    padding-left: 1rem;
                    padding-right: 1rem;
                }
               .css-wldksm {
                    padding-top: 4rem;
                    font-size: 0.75rem;
                }
               .css-b7s55g {
                    padding-top: 0rem;
                    padding-right: 0rem;
                    padding-bottom: 0rem;
                    padding-left: 0rem;
                }
               .css-1ur0u7i {
                    padding-top: 0rem;
                    padding-right: 0rem;
                    padding-bottom: 0rem;
                    padding-left: 0rem;
                }
               .css-97ja1j {
                    height: 0rem;
                }
               .css-1esuaex {
                    gap: 0.5rem;
                }
               .css-1avcm0n {
                    height: 0rem;   
                }
               .css-uc76bn {
                    padding-top: 4rem;
                    font-size: 0.75rem;
                }
               .css-13eon2a {
                    font-size: 0.75rem;
                }
               .css-79elbk {
                    font-size: 0.75rem;
                }
        </style>
        """
        
jsCodeStr = """
function(e) {
    let api = e.api;
    let rowIndex = e.rowIndex;
    let col = e.column.colId;

    let rowNode = api.getDisplayedRowAtIndex(rowIndex);
    api.flashCells({
      rowNodes: [rowNode],
      columns: [col],
      flashDelay: 10000000000
    });

};
"""

def getCodeSnippet(name):
    if name == 'sidebarWidth':
        codesnippet = sidebarWidth
    elif name == 'hideStreamlitStyle':
        codesnippet = hideStreamlitStyle
    elif name == 'adjustPaddingAndFont':
        codesnippet = adjustPaddingAndFont
    elif name == 'jsCodeStr':
        codesnippet = jsCodeStr
    else:
        codesnippet = 'CODE STRING SNIPPET NOT FOUND AHHHH'
    return codesnippet
    
