import json
import requests
requests.packages.urllib3.disable_warnings()

class JSONRequest(object):
        """This class allows you to make requests to the backend server."""
        global key_session
        global backendURL
        key_session = None
        backendURL = 'https://backendbeta.ibizapi.com:8888/JSON/'
        def __init__(self): pass

        def login(self, id, user, password):
                self.id = id
                self.user = user
                self.password = password
                requestData = {'account_id': id, 'email': user, 'password': password}
                requestURL = backendURL + 'AccountManager/AAA?action=Authenticate'
                r = requests.post(requestURL, data=json.dumps(requestData), verify=False)
                responseJSON = r.text()
                data = json.loads(responseJSON)
                key_session = data['session_key']

        def caseList(self):
                requestData = {'account_id': '1000', 'session_key': key_session, 'MANY': '100'}
                requestURL = backendURL + 'Case?action=List'
                r = requests.post(requestURL, data=json.dumps(requestData), verify=False)
                casesJson = r.json()