import sqlite3
import datetime

conn = sqlite3.connect('neptune_session.db')
c = conn.cursor()
# c.execute('''CREATE TABLE session \
#           (id             INTEGER        PRIMARY KEY  AUTOINCREMENT, \
#           session_key     VARCHAR(25)    NOT NULL, \
#           session_data    TEXT           NOT NULL, \
#           expire_date     DATETIME       NOT NULL);''')


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
        self.used = False
        self.curr_sess_id = 0
        self.key = 'session_id'

    def initialize_session(self, key, data, date=datetime.datetime.now()):
        #TODO check requests headers for set cookie
        self.used = True
        date = date + datetime.timedelta(days=10)
        print (date)
        c.execute("INSERT INTO session (session_key, session_data, expire_date) VALUES (?, ?, ?)", (key, data, date))
        print (c.lastrowid)
        self.curr_sess_id = c.lastrowid
        conn.commit()
        conn.close()

    def get_se():
        pass

    def clear_curr_sess(self):
        self.used = False
        self.curr_sess_id = 0