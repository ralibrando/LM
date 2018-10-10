#!/bin/env python

import requests
import json
import hashlib
import base64
import time
import hmac
import objectpath

##Account Info
AccessId ='25TcJtV3y8wdtHr4iV2I'
AccessKey ='K_D!)R-{bYx(f8yi9zw3))GGq$5jz_3n2-z]pT99'
Company = 'lookingpoint'


##Request Info
httpVerb ='GET'
resourcePath = '/device/devices/'

## Search for any device where the display name contains "PUB"
queryParams ='?filter=displayName~*PUB*&fields=id,displayName'
#queryParams =''
data = ''

##Construct URL
url = 'https://'+ Company +'.logicmonitor.com/santaba/rest' + resourcePath + queryParams

##Get current time in milliseconds
epoch = str(int(time.time() * 1000))

##Concatenate Request details
requestVars = httpVerb + epoch + data + resourcePath

##Construct signature
signature = base64.b64encode(hmac.new(AccessKey,msg=requestVars,digestmod=hashlib.sha256).hexdigest())
#print signature

##Construct headers
auth = 'LMv1 ' + AccessId + ':' + signature + ':' + epoch
headers = {'Content-Type':'application/json','Authorization':auth}

#print url
#print headers

#Make GET request
response = requests.get(url, data=data, headers=headers)

#print response

#Print status and body of response
#print 'Response Status:',response.status_code
#print 'Response Body:',response.content

info = response.content
#print(json.loads(info))

##load the json results into a "dictionary"
myjson = json.loads(info)

##grab just the data/items subgroups from the json
myitems = myjson['data']['items']
#print(myjson['data']['items'])

##separate out just the ids and print them
myidlist = []
for x in myitems:
	myids = x['id']
	#print(myids)
	myidlist.append(myids)
 
##TEST
#u = 'https://'+ Company +'.logicmonitor.com/santaba/rest/device/devices/10/properties'
#d = '{"name":"cucm.drs","value":"true"}'
#rV = 'POST' + epoch + d + '/device/devices/10/properties'
#sig = base64.b64encode(hmac.new(AccessKey,msg=rV,digestmod=hashlib.sha256).hexdigest())
#authy = 'LMv1 ' + AccessId + ':' + sig + ':' + epoch
#heady = {'Content-Type':'application/json','Authorization':authy}

#responseTEST =requests.post(u, data=d, headers=heady)
#print 'Response Status:',responseTEST.status_code
#print 'Response Body:',responseTEST.content

##ADD A CUSTOM PROPERTY FOR EACH ID
for i in myidlist:
	resourcePath2 = '/device/devices/' + str(i) + '/properties'
#	print(resourcePath2)
	hV ='POST'
	d = '{"name":"cucm.drs","value":"true"}'
	u = 'https://'+ Company +'.logicmonitor.com/santaba/rest' + resourcePath2
#	print('url is ' + u)
	rV = hV + epoch + d + resourcePath2
	sig = base64.b64encode(hmac.new(AccessKey,msg=rV,digestmod=hashlib.sha256).hexdigest())
	authy = 'LMv1 ' + AccessId + ':' + sig + ':' + epoch
	heady = {'Content-Type':'application/json','Authorization':authy}

#	print('rV is ' + rV)
	response2 = requests.post(u, data=d, headers=heady)
	print 'Response Status:',response2.status_code
	print 'Response Body:',response2.content
