#!/usr/bin/python
import backendclass
import json
import requests
from sys import argv, exit
requests.packages.urllib3.disable_warnings()

script, account_id, email, password = argv

auth = False

def caseTest():
        if auth == False:
                print "Not authenticated!"
                exit(1)
        else:
                print JSONRequest.caseList()
                exit(0)

def runAuth(id, user, password):
        print "Authenticating with ID %s, user %s and password %s" % (id, user, password)
        request = backendclass.JSONRequest()
        request.login(id, user, password)
        if backendclass.key_session != None:
                print "Success! The session_key is %s" % key_session
                auth = True
        else:
                print "Authentication failure!"
                print


def __init__():
        print "Let's test out authentication and case requests."
        runAuth(account_id, email, password)
##      caseTest()

__init__()
