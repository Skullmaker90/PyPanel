import json
import requests

class JSONRequest:
	"""This class allows you to make requests to the backend server."""
	key_session = None
	backendURL = 'https://backend.ibizapi.com:8888/JSON/'
	def __init__(self): pass
	
	def login(self, id, user, pass):
		requestData = {'account_id': id, 'email': user, 'password': pass}
		requestURL = backendURL + 'AccountManager/AAA?action=Authenticate'
		r = requests.post(requestURL, data=json.dumps(requestData), verify=False)
		responseJSON = r.text()
		data = json.loads(responseJSON)
		key_session = data['session_key']
		
	def caseList(self, key_session):
		requestData = {'account_id': "1000", 'session_key': key_session}
		requestURL = backendURL + 'Case?action=List'
		r = requests.post(requestURL, data=json.dumps(requestData), verify=False)
		casesJson = r.json()