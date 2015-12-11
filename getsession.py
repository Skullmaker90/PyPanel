from sys import exit
import requests
import json
requests.packages.urllib3.disable_warnings()


backendUrl = 'https://backend.ibizapi.com:8888/JSON/AccountManager/AAA?action=Authenticate'
loginRequest = {'account_id': 'xxxxx', 'email': 'xxxxx', 'password': 'xxxxx'}
	
def loginPOST():
	r = requests.post(backendUrl, data=json.dumps(loginRequest), verify=False)
	return r.json

def __init__():
    print loginPOST()
	exit(0)
	
__init__()