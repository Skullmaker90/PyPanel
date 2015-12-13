import json
import requests
from mysqlclass import MySQLQuery
requests.packages.urllib3.disable_warnings()

class JSONRequest(object):
        """This class allows you to make requests to the backend server."""
        global key_session
        global backendURL
        key_session = None
        backendURL = 'https://backendbeta.ibizapi.com:8888/JSON/'
        def __init__(self): pass

        def login(self, user, password):
		# I've removed the id situation and replaced it with an expandable mysql db backend, we don't have to remember ID's.
                self.user = user
                self.password = password
		# Check mysqlclass to see what this does.
		idreq = MySQLQuery()
		idreq.idQuery(user)
		requestData = {'account_id': id, 'email': user, 'password': password}
                requestURL = backendURL + 'AccountManager/AAA?action=Authenticate'
                r = requests.post(requestURL, data=json.dumps(requestData), verify=False)
                responseJSON = r.json() # Changed this from r.text() to r.json().
		# Since it's already decoded we don't need this.
                # data = json.loads(responseJSON) 
                key_session = responseJSON['session_key']

        def caseList(self):
                requestData = {'account_id': '1000', 'session_key': key_session, 'MANY': '10'}
                requestURL = backendURL + 'Case?action=List'
                r = requests.post(requestURL, data=json.dumps(requestData), verify=False)
                casesJson = r.json()
	
        def logout(self, key_session):
		    requestData = {'session_key': key_session}
		    requestURL = backendURL + 'AccountManager/AAA?action=Logout'
		    r = requests.post(requestURL, data=json.dumps(requestData), verify=False)
		    data = r.json()
		    logoutResp = data['success']
		    if "1" not in logoutResp:
			    print "Logged out of the panel!"
		    else:
			    print "We returned an error (or otherwise did not log out!) Exiting!"
			    exit(1)