#!/usr/bin/python

import keyauth, requests, json, getpass
requests.packages.urllib3.disable_warnings()

# This is the current running functions of the PyPanel. ./panelfunc.py
# will ask what you would like to do, if you request the caseboard it
# will check keyauth to see if your authenticated and if not it'll auth
# the user then return the caseboard (Still working that out) and dump
# the user back at the prompt screen. This will eventually become the
# backendfunc class with everything we would need to call for the backend.

def authcheck(a):
	if a.key == None:
		user = raw_input("Email: ")
		password = getpass.getpass("Password: ")
		a.login(user, password)
		print("Your session key is: %s") % (a.key)

def caseBoard(a, func):
	authcheck(a)
	requestData = {'account_id': '2277', 'session_key': a.key, 'MANY': '15'}
	requestURL = a.backendURL + 'Case?action=List'
	r = requests.post(requestURL, data=json.dumps(requestData), verify=False)
	casesJSON = r.json()

def menu(a):
	while True:
		print("What would you like to do? (1 for Caseboard, 2 for logout, 3 to exit)")
		choice = int(raw_input())
		if choice == 1:
			print caseBoard(a, menu)
		elif choice == 2:
			print("Logging out.")
			a.logout()
		elif choice == 3:
			exit(0)
		else:
			print("That's not an option.")

def main():
	url = 'https://backendbeta.ibizapi.com:8888/JSON/'
	a = keyauth.keyauth(url)
	menu(a)

main()
