#from mysql_connetion import getMycursor
import random
import string

class Door_Structur():

    def __init__(self):
        self.createTabel()

    def createTabel(self):
        self.__mysql__ = getMycursor()
        self.__mysql__.getCurso().execute("CREATE TABEL IF NOT EXISTS doors (door_id VARCHAR(255), door_uuid VARCHAR(255))")
        self.__mysql__.getCurso().execute("CREATE TABEL IF NOT EXISTS doors_update (door_uuid VARCHAR(255), action VARCHAR(255))")

    def addDoor(self, door):

        sql = "INSERT INTO doors (door_id, door_uuid) VALUES (%s, %s)"
        letters = string.ascii_letters
        val = (door, ''.join(random.choice(letters) for i in range(10)))
        self.__mysql__.getCurso().execute(sql, val)

    def getDoorUUID(self, name):
        pass

