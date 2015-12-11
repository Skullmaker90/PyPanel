from sys import exit
import requests
import json
requests.packages.urllib3.disable_warnings()


backendUrl = 'https://admin.ibizoncall.com/iBiz/Panel/Login'
loginRequest = {'account_id': '187358', 'email': 'asmith@cari.net', 'password': 'xxxxx'}
	
def loginPOST():
	r = requests.post(backendUrl, data=json.dumps(loginRequest), verify=False)
	return r.text

def __init__():
    print loginPOST()
	exit(0)
	
__init__()