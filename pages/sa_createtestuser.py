from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
#from .s3_handler import S3Handler
#from openpyxl import load_workbook, Workbook
import requests
import os
import time
import json
import random
#from .models import mtd_tokens,posted ,testuser, apps_ids, log1
from urllib.parse import urlparse
import logging

#from django.shortcuts import render,redirect
#import requests
#import json
#from mtd.models import List_mtd,posted ,testuser, apps_ids, log1

#

#import pd
#console py file used testing
#import pdb 
#pdb.set_trace()

#obj=apps_ids.objects.get(id=5)

endpoint='https://test-api.service.hmrc.gov.uk/create-test-user/organisations'		
#endpoint='https://test-api.service.hmrc.gov.uk/create-test-user/agents'		

post_Data2={
 
	  "serviceNames": 
    ["mtd-income-tax"] 
    
		}
headers ={
			'Authorization': 'Bearer '+ '98918245c5488ac09cf5a55955c5e1cd' , #bts1-test #ae52e145fe25f0c7248e49e8d8fdcafd',
			'Content-Type':'application/json',
			'Accept' :'application/vnd.hmrc.1.0+json'
					
		}
		
r = requests.post(endpoint,data=json.dumps(post_Data2), headers=headers)
		
rj=r.json()

    
print(r)
print('--------')
print('--------')
print('--------')
print(rj)
print('--------')