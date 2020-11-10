import mysql.connector

class DB():
    def __init__(self):
        self.dbconn = mysql.connector.connect(host='localhost', user='root', passwd='root', database='chat')
        self.cursor = self.dbconn.cursor()


    def select(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def execute(self, sql):
        self.cursor.execute(sql)
        return self.cursor.commit()