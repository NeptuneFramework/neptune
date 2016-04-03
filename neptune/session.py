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

	def __init__(self, id, ):
		super(NSession, self).__init__()
		self.arg = arg
