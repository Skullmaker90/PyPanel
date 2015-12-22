#!/usr/bin/python

# I basically rewrote all of this code to implement more OO-Python
# and to store and manipulate key_session as a variable. This class
# is purely for retrieving an popping the session keys. If there are
# any questions come see Anthony..

import json, requests
requests.packages.urllib3.disable_warnings()

class keyauth(object):
	def __init__(self, url):
		self.key = None
		self.usr_acc_id = None
		self.backend_url = url
	
	def login (self, user, password):
		self.user, self.password = user, password
		acc_host = str('admin.ibizpanel.net')
		request_data = {'account_host': acc_host, 'email': user, 'password': password}
		request_url = self.backend_url + 'AccountManager/AAA?action=Authenticate'
		a = requests.post(request_url, data=json.dumps(request_data), verify=False)
		response_json = a.json()
		try:
			self.key = response_json['session_key']
			self.usr_acc_id = respons_json['account_id']
		except: 
			print("Session key not set.")

	def logout (self):
		request_data = {'session_key': self.key}
		request_url = self.backend_url + 'AccountManager/AAA?action=Logout'
		l = requests.post(request_url, data=json.dumps(request_data), verify=False)
		response_json = l.json()
		if response_json['success']  == unicode('1'):
			print "Success!"
			self.key = None
			return
		else:
			print "Something failed to log you out!"
			return
