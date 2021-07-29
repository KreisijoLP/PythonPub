import mysql

class MySQLUtils:


    def __init__(self, host, db, user, password):
        self.host = host
        self.db = db
        self.user = user
        self.password=password

    def connect(self):

        self.__mysqldb__ = mysql.co

    def performCommand(self):
