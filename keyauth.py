#!/usr/bin/python

import json, requests
requests.packages.urllib3.disable_warnings()

class keyauth(object):
	def __init__(self):
		self.key = None
		self.backendURL = str('https://backendbeta.ibizapi.com:8888/JSON/')
	
	def login (self, user, password):
		self.user, self.password = user, password
		accHost = str('admin.ibizpanel.net')
		requestData = {'account_host': accHost, 'email': user, 'password': password}
		requestUrl = self.backendURL + 'AccountManager/AAA?action=Authenticate'
		a = requests.post(requestUrl, data=json.dumps(requestData), verify=False)
		responseJSON = a.json()
		self.key = responseJSON['session_key']

	def logout (self):
		requestData = {'session_key': self.key}
		requestURL = self.backendURL + 'AccountManager/AAA?action=Logout'
		l = requests.post(requestURL, data=json.dumps(requestData), verify=False)
		responseJSON = l.json()
		if responseJSON['success']  == unicode('1'):
			print "Success!"
			self.key = None
			return
		else:
			print "Something failed to log you out!"
			return
