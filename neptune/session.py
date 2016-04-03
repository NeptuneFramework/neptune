import sqlite3
import datetime

conn = sqlite3.connect('neptune_session.db')
# conn.execute('''CREATE TABLE session
# 		    (session_key 	VARCHAR(25) PRIMARY KEY     NOT NULL,
# 		    session_data    TEXT    	NOT NULL,
# 		    expire_date  	DATETIME	NOT NULL);''')


class NSession(object):
	"""
	NSession - Class for handling Sessions

	Session table structure:

	+--------------+-------------+------+-----+---------+-------+
	| Field        | Type        | Null | Key | Default | Extra |
	+--------------+-------------+------+-----+---------+-------+
	| session_key  | varchar(20) | NO   | PRI | NULL    |       |
	| session_data | longtext    | NO   |     | NULL    |       |
	| expire_date  | datetime    | NO   | MUL | NULL    |       |
	+--------------+-------------+------+-----+---------+-------+

	"""

	# def __init__(self, key, data, date=datetime.datetime.now()):
	# 	self.arg = arg

	def initialize_session(self, key, data, date=datetime.datetime.now()):
		#TODO check requests headers for set cookie
		# print (key)
		# print (data)
		# print (date)
		date = date + datetime.timedelta(days=10)
		print (date)
		conn.execute("INSERT INTO session (session_key, session_data, expire_date) VALUES (?, ?, ?)", (key, data, date))
		conn.commit()
		conn.close()