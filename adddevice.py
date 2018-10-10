#!/bin/env python

import requests
import json
import hashlib
import base64
import time
import hmac

#Account Info
AccessId ='25TcJtV3y8wdtHr4iV2I'
AccessKey ='K_D!)R-{bYx(f8yi9zw3))GGq$5jz_3n2-z]pT99'
Company = 'lookingpoint'

#Open spreadsheet
import xlrd
workbook = xlrd.open_workbook('LP-Test-Devices.xlsx')
worksheet = workbook.sheet_by_index(0)

#Pull data from spreadsheet
if sheet.cell(0, 0).value == xlrd.empty_cell.value:
#What do we do if the first cell is blank?

#to get a specific cell data
sheet.cell(0, 0).value

#to iterate through a group of cells (all rows & columns)
for row_cells in worksheet.iter_rows():
    for cell in row_cells:
        print('%s: cell.value=%s' % (cell, cell.value) )

#to iterate through a group of cells (all columns of one row)
#for row_cells in worksheet.iter_rows(min_row=2, max_row=2)
#    for cell in row_cells:
#        print('%s: cell.value=%s' % (cell, cell.value) )

#to iterate through a group of rows in a columng
#for col_cells in worksheet.iter_cols(min_col=2, max_col=2):
#    for cell in col_cells:
#        print('%s: cell.value=%s' % (cell, cell.value))

#Request Info
httpVerb ='POST'
resourcePath = '/device/devices'
data = '{"name":"172.16.19.171",
"displayName":"ProdServer25",
"preferredCollectorId":171,
"hostGroupIds":2,
"customProperties":[{"name":"snmp.version","value":"v3"},{"name":"location","value":"Santa Barbara,CA"}]}'

#Construct URL
url = 'https://'+ Company +'.logicmonitor.com/santaba/rest' + resourcePath

#Get current time in milliseconds
epoch = str(int(time.time() * 1000))

#Concatenate Request details
requestVars = httpVerb + epoch + data + resourcePath

#Construct signature
signature = base64.b64encode(hmac.new(AccessKey,msg=requestVars,digestmod=hashlib.sha256).hexdigest())

#Construct headers
auth = 'LMv1 ' + AccessId + ':' + signature + ':' + epoch
headers = {'Content-Type':'application/json','Authorization':auth}

#Make request
response = requests.post(url, data=data, headers=headers)

#Print status and body of response
print 'Response Status:',response.status_code
print 'Response Body:',response.content

