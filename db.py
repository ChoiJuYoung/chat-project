import mysql.connector

class DB():
    def __init__(self):
        try:
            self.dbconn = mysql.connector.connect(host='localhost', user='root', passwd='root', database='chat')
            self.cursor = self.dbconn.cursor()
        except Exception as e:
            print(e)


    def select(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def execute(self, sql):
        self.cursor.execute(sql)
        return self.cursor.commit()