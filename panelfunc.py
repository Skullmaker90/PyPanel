#!/usr/bin/python

import keyauth, requests, json, getpass
requests.packages.urllib3.disable_warnings()

# This is the current running functions of the PyPanel. ./panelfunc.py
# will ask what you would like to do, if you request the caseboard it
# will check keyauth to see if your authenticated and if not it'll auth
# the user then return the caseboard (Still working that out) and dump
# the user back at the prompt screen. This will eventually become the
# backendfunc class with everything we would need to call for the backend.

def auth_check(auth):
	if auth.key == None:
		user = raw_input("Email: ")
		password = getpass.getpass("Password: ")
		auth.login(user, password)
		print("Your session key is: %s") % (auth.key)

def case_board(auth, request_data):
	auth_check(auth)
	request_url = auth.backend_url + 'Case?action=List'
	request_data['session_key'] = auth.key
	r = requests.post(request_url, data=json.dumps(request_data), verify=False)
	cases_json = r.json()

def menu(auth, request_data):
	running = True
	while running == True:
		print("What would you like to do? (1 for Caseboard, 2 for logout, 3 to exit)")
		choice = int(raw_input())
		if choice == 1:
			print case_board(auth, request_data)
		elif choice == 2:
			print("Logging out.")
			auth.logout()
		elif choice == 3:
			running = False
		else:
			print("That's not an option.")

def main():
	request_data = {'account_id': '2277', 'MANY': '15'}
	url = 'https://backendbeta.ibizapi.com:8888/JSON/'
	auth = keyauth.keyauth(url)
	menu(auth, request_data)

main()
