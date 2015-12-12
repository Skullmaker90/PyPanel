#!/usr/bin/python
import MySQLdb as mdb
import sys

class MySQLQuery(object):
	"""This class allows you to query a db server to get info, mainly the accId of an email address."""
	global accId
	accId = None
	def __init__(self): pass

	def idQuery(self, email):
		self.email =  email
		try:
			con = mdb.connect(host="71.6.132.43", port=3306, user="PyPanel", passwd="carinet", db="pypanel")
			q = con.cursor()
			q.execute("SELECT accId FROM usrData WHERE accEmail = '%s'" % (email,))
			global accId
			self.accId = q.fetchall()
			self.accId = self.accId[0][0]

		except mdb.Error, e:

			print "Error %d: %s" % (e.args[0], e.args[1])
			sys.exit(1)

		finally:
			if con:
				con.close()
