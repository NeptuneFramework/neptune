import sqlite3
import datetime

conn = sqlite3.connect('neptune_session.db')
c = conn.cursor()
# c.execute('''CREATE TABLE session \
#           (id             INTEGER        PRIMARY KEY  AUTOINCREMENT, \
#           session_key     VARCHAR(25)    NOT NULL, \
#           session_data    TEXT           NOT NULL, \
#           expire_date     DATETIME       NOT NULL);''')

# TODO: Use SQLAlchemy for this all stuff
# TODO: Check if session_id exists or not

class NSession(object):
    """
    NSession - Class for handling Sessions

    Session table structure:

    +--------------+-------------+------+-----+---------+-------+
    | Field        | Type        | Null | Key | Default | Extra |
    +--------------+-------------+------+-----+---------+-------+
    | id           | int         | NO   | PRI | AUTO    |       |
    | session_key  | varchar(20) | NO   |     | NULL    |       |
    | session_data | longtext    | NO   |     | NULL    |       |
    | expire_date  | datetime    | NO   | MUL | NULL    |       |
    +--------------+-------------+------+-----+---------+-------+

    """

    def __init__(self):
        self.conn = sqlite3.connect('neptune_session.db')
        self.c = self.conn.cursor()
        self.used = False
        self.curr_sess_id = 0
        self.key = 'session_id'

    def set_value(self, key, value, date=datetime.datetime.now()):
        #TODO check requests headers for set cookie
        self.used = True
        date += datetime.timedelta(days=10)
        if self.curr_sess_id == 0:
            self.c.execute("INSERT INTO session (session_key, session_data, expire_date) VALUES (?, ?, ?)", (key, value, date))
            self.curr_sess_id = self.c.lastrowid
            self.conn.commit()
        else:
            self.c.execute("INSERT INTO session (id, session_key, session_data, expire_date) VALUES (?, ?, ?)", (self.curr_sess_id, key, value, date))
            self.conn.commit()

    def get_value(self, key, sess_id):
        data = self.conn.execute("Select session_data from session where session_key = %s and id = %s limit 1" % (key, sess_id))
        data = [i for i in data]
        return data[0][0]

    def clear_curr_sess(self):
        self.used = False
        self.curr_sess_id = 0
