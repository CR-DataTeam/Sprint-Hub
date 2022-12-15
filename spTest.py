# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 18:46:53 2022

@author: joshua.mcdonald
"""

from shareplum import Site
from shareplum import Office365
from shareplum.site import Version

qwe2 = 's'
qwe3 = 'k'
qwe4 = 'Ja'
qwe5 = '22'
qwe6 = '9'
qwe1 = 'Jo'

qwe = qwe4 + qwe3 + qwe1 + qwe2 + qwe6 + qwe5
uwe = 'joshua.mcdonald@usradiology.com'

authcookie = Office365('https://usradiology.sharepoint.com', username=uwe, password=qwe).GetCookies()
site = Site('https://usradiology.sharepoint.com/sites/CRBusinessIntelligence/', version=Version.v365, authcookie=authcookie)











