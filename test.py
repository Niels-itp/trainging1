import json
import requests
import time
import datetime

#freshservice
fs_url = 'https://iteamplay.freshservice.com'
fs_apikey = 'Zg6dDtfn2I7iNTcyzNYL'
#

def fs_get_cust():
    global fs_url
    global fs_apikey

    headers = {'Content-Type': 'application/json'}
    api_url = fs_url + '/api/v2/departments'

    response = requests.get(api_url, headers=headers, auth=(fs_apikey, 'x'))

    if (response.ok):
        resp_data = json.loads(response.content)
    else:
        print(response.raise_for_status())

    return resp_data['departments']

def fs_get_ass(cid, tid):
    global fs_url
    global fs_apikey

    headers = {'Content-Type': 'application/json'}
    api_url = fs_url + '/api/v2/assets?query="department_id:' + str(cid) + '"'

    response = requests.get(api_url, headers=headers, auth=(fs_apikey, 'x'))

    if (response.ok):
        resp_data = json.loads(response.content)
    else:
        print(response.raise_for_status())

    return resp_data['assets']

def fs_get_asstypes():
    global fs_url
    global fs_apikey

    headers = {'Content-Type': 'application/json'}
    api_url = fs_url + '/api/v2/asset_types'

    response = requests.get(api_url, headers=headers, auth=(fs_apikey, 'x'))

    if (response.ok):
        resp_data = json.loads(response.content)
    else:
        print(response.raise_for_status())

    return resp_data['asset_types']

#Haal asset types op om asset id's van de managed services op te halen
ass_types = fs_get_asstypes()
for ass_type in ass_types:
    print(ass_type['name'])
    if ass_type['name'] == 'Unifi Cloud Controller':
        fs_ass_unificloud = ass_type['id']  

customers = fs_get_cust()

for customer in customers:
    assets = fs_get_ass(customer['id'])
    for asset in assets:
        if asset['asset_type_id'] == fs_ass_unificloud:
            #Unifi beheer uitvoeren
quit()
