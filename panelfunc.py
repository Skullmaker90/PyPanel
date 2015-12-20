#!/usr/bin/python

import keyauth, requests, json, getpass
requests.packages.urllib3.disable_warnings()

a = keyauth.keyauth()

def authcheck():
	if a.key == None:
		user = raw_input("Email: ")
		password = getpass.getpass("Password: ")
		a.login(user, password)
		print("Your session key is: %s") % (a.key)
		return
	else:
		return

def callback(func):
	return func()

def caseBoard():
	callback(authcheck)
	requestData = {'account_id': '2277', 'session_key': a.key, 'MANY': '15'}
	requestURL = a.backendURL + 'Case?action=List'
	r = requests.post(requestURL, data=json.dumps(requestData), verify=False)
	casesJSON = r.json()
	return

def __main__():
	print("What would you like to do? (1 for Caseboard, 2 for logout)")
	choice = int(raw_input())
	if choice == 1:
		print caseBoard()
	elif choice == 2:
		print("Logging out.")
		a.logout()
	else:
		print("That's not an option.")
	return __main__()

__main__()
