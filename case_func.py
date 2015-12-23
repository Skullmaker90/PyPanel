#!/usr/bin/python

import requests, json, time

class case_func(object):
	def __init__(self, key, usr_acc_id, backend_url):
		self.key = key
		self.usr_acc_id = usr_acc_id
		self.backend_url = backend_url

	def case_add(self):
		dest_acc = int(raw_input("Account to open under: "))
		desc = str(raw_input("Case description: "))
		request_data = {'account_id': '%s', 'case_spec':{'assigned_id': '1000', 'description': '%s', 'type': "PROBLEM"} , 'session_key': '%s'} % (dest_acc, description, self.key)
		choice1 = str(raw_input("Internal note?: "))
		loop = True
		while loop == True:
			if (choice1 == str("yes") or choice1 == str("y")):
				inter_note = str(raw_input("Note: "))
				request_data['case_spec']['internal_notes'] = inter_note
				loop = False
			elif (choice1 == str("no") or choice1 == str("n")):
				inter_note = ""
				loop = False
				pass
			else:
				choice1 = str(raw_input("Yes or no please: "))
		choice2  = int(raw_input("Send off or stay on the board? (1 for go, 2 for stay): "))
		loop = True
		while loop == True:
			if choice2 == '1':
				request_data['case_spec']['status'] = str("CUSTOMER")
				req_time = True
				loop = False
			elif choice == '2':
				pass
				loop = False
			else:
				choice2 = int(raw_input("1 or 2 please: "))
		choice3 = str(raw_input("Set to close? (Default is YES): "))
		if choice3 == str(""):
			pass
		elif (choice3 == str("no") or choice3 == str("n")):
			request_data['case_spec']['auto_close'] = str("NO")
			req_time = True
		if req_time == True:
			req_time_string = str("Yes")
		loop = True
		while req_time == True:
			try:
				while loop == True:
					choice4 = raw_input("Time in hours to come back: ")
					if choice4 > '0':
						request_data['case_spec']['return_hours'] = int(choice4)
						loop = False
					elif choice4 <= '0':
						print("Please choose a positive int.")
			except ValueError:
				print("Please choose an Int.")
			req_time = False
		string = ("\nAccount case will be open under: " + request_data['account_id'] + "\n"
				"Auto Close: " + request_data['case_spec']['auto_close'] + "\n"
				"Description: " + request_data['case_spec']['description'] + "\n"
				"Status: " + request_data['case_spec']['status'] + "\n")
		if request_data['case_spec']['status'] == "CUSTOMER":
			string = string + ("Hours to return in: " + request_data['case_spec']['return_hours'] + "\n")
		if inter_note != "":
			string = string + ("Internal note: " + request_data['case_spec']['internal_notes'] + "\n")
		print(string)
		final = True
		while final == True:
			final_choice = raw_input("Are these settings correct?: ")
			if (final_choice == "yes" or final_choice == "y"):
				print("Creating case.")
				final = False
			elif (final_choice == "no" or final_choice == "n"):
				print("Well doesn't that suck.")
				final = False
				return case_add()
			else:
				print("Yes or No please.")
		# Commenting here to show end of questions.
		request_url = backend_url + 'Case?action=Add'
		try:
			r = requests.post(request_url, data=json.dumps(request_data), verify=False)
			a = r.json()
			result = a[u'new_id']
			print("Success!: ") + result
		except:
			print("Something went wrong.")
			return

	def case_close(self):
		pass

	def case_edit(self):
		pass

	def case_list(self):
		request_data = {'limit':{'OR1':{'OR1':{'status':"RESPONSE"},'OR2':{'status':"PENDING"},'OR3':{'status':"NEW"},'OR4':{'status':"UPSTREAM"}}}, 'account_id': '2277', 'session_key': self.key}
        	request_url = self.backend_url + 'Case?action=List'
        	r = requests.post(request_url, data=json.dumps(request_data), verify=False)
        	board = r.json()
        	list = board[u'LIST']
        	for row in list:
                	string = ("\nCase Number: " + row[u'case_id'] + "\n"
                        	"Account Number: " + row[u'account_id'] + "\n"
                        	"Open Date: " + time.strftime('%m/%d/%Y %H:%M:%S', time.localtime(int(row[u'creation_date']))) + "\n"
                        	"Last Update: " + time.strftime('%m/%d/%Y %H:%M:%S',  time.localtime(int(row[u'last_update'])))  + "\n"
                        	"Status: " + row[u'status'] + "\n"
                        	"Description: " + row[u'description'] + "\n")
                	print(string)

	def case_view(self):
		pass
