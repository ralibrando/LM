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

#Request Info
httpVerb ='DELETE'
resourcePath = '/device/devices/294/devicedatasources/17024/instances/26890160'
#queryParameters = '?filter=stopMonitoring:true&fields=id,displayName,stopMonitoring'
data = ''

#Construct URL
url = 'https://'+ Company +'.logicmonitor.com/santaba/rest' + resourcePath # + queryParameters

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
response = requests.delete(url, data=data, headers=headers)

#Print status and body of response
print 'Response Status:',response.status_code
print 'Response Body:',response.content
