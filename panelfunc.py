#!/usr/bin/python

import keyauth, requests, json, getpass, time
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
		try:
			auth.login(user, password)
		except:
			print("Wrong email/password. Try again.")
			auth.login(user, password)
		print("Your session key is: %s") % (auth.key)

def case_board(auth, request_data):
	auth_check(auth)
	request_url = auth.backend_url + 'Case?action=List'
	request_data['session_key'] = auth.key
	r = requests.post(request_url, data=json.dumps(request_data), verify=False)
	# return r.json()
	board = r.json()
	list = board[u'LIST']
	for row in list:
		# print(row)
		# type(row[u'creation_date']
		if (row[u'status'] == "RESPONSE" or row[u'status'] == "PENDING" or row[u'status'] == "NEW"):
			string = ("\nCase Number: " + row[u'case_id'] + "\n"
				"Account Number: " + row[u'account_id'] + "\n"
				"Open Date: " + time.strftime('%m/%d/%Y %H:%M:%S', time.localtime(int(row[u'creation_date']))) + "\n"
				"Last Update: " + time.strftime('%m/%d/%Y %H:%M:%S',  time.localtime(int(row[u'last_update'])))  + "\n"
				"Status: " + row[u'status'] + "\n"
				"Description: " + row[u'description'] + "\n")
			print(string)

def menu(auth, request_data):
	running = True
	while running == True:
		print("What would you like to do? (1 for Caseboard, 2 for logout, 3 to exit)")
		choice = int(raw_input())
		if choice == 1:
			case_board(auth, request_data)
			#list = blob[u'LIST']
			#for row in list:
			#	print(row[u'case_id'])
		elif choice == 2:
			print("Logging out.")
			auth.logout()
		elif choice == 3:
			try:
				auth.logout()
			except: pass
			running = False
		else:
			print("That's not an option.")

def main():
	request_data = {'account_id': '2277'}
	url = 'https://backendbeta.ibizapi.com:8888/JSON/'
	auth = keyauth.keyauth(url)
	menu(auth, request_data)

main()
