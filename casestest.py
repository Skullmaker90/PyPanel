#!/usr/bin/python
import backendclass
import json
import requests
import getpass
from sys import argv, exit
requests.packages.urllib3.disable_warnings()

# Took out this for now so we don't have to enter pass at line, added prompts
# script, email, password = argv

# Still testing this, thinking about adding a session_key validation to init.
# auth = False

# Still in testing
def caseTest():
        if auth == False:
                print "Not authenticated!"
                exit(1)
        else:
                print JSONRequest.caseList()
                exit(0)

def runAuth(user, password):
        print "Authenticating with user %s and password %s" % (user, password)
        request = backendclass.JSONRequest()
        request.login(user, password)
        if backendclass.key_session != None:
                print "Success! The session_key is %s" % backendclass.key_session
		print
		# Added this just to test the caseboard while we write out a session verification.
		# board = backendclass.JSONRequest()
		# print board.caseList()
                # auth = True
        else:
                print "Authentication failure!"
                print


def __init__():
	# Added this check so we can optionally create a new session
	# we should probably replace this with a session verification
	check = int(input("What would you like to do? (1 for auth, 2 for casetest): "))
	if check ==  1:
		# This works, just need to think about logging out.
		print "Let's test out authentication and case requests."
		email = raw_input("Email: ")
		password = getpass.getpass("Password: ")
        	runAuth(email, password)
	elif check == 2:
		print "Let's grab the caseboard."
		# Still working on this
        	caseTest()
	else:
		exit(0)
__init__()
