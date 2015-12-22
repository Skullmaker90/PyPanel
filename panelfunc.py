#!/usr/bin/python

import requests, json, getpass, time
import keyauth, case_func
requests.packages.urllib3.disable_warnings()

# Author: Anthony Smith. Last update: 12/22/2015. Version: 0.1

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
		print("Your account ID is: %s") % (auth.usr_acc_id)

def case_menu(auth, url):
	casefunc = case_func.case_func(auth.key, auth.usr_acc_id, url)
	running = True
	while running == True:
		choice = int(raw_input("What would you like to do? (1 to list, 2 to add, 3 to go back): "))
		if choice == 1:
			casefunc.case_list()
		elif choice == 2:
			casefunc.case_add()
		elif choice == 3:
			running = False

def main_menu(auth, url):
	running = True
	while running == True:
		choice = int(raw_input("What would you like to do? (1 for Cases, 2 to exit): "))
		if choice == 1:
			case_menu(auth, url)
		elif choice == 2:
			print("Logging out.")
			auth.logout()
			running = False
		else:
			print("That's not an option.")

def main():
	url = 'https://backendbeta.ibizapi.com:8888/JSON/'
	auth = keyauth.keyauth(url)
	auth_check(auth)
	menu_menu(auth, url)

main()
