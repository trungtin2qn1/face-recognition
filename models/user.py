from db.db import DbConnector
import json

class User:

    def __init__(self,):
        return
    
    def insertToDB(self, id, name):
        dbConnector = DbConnector()
        self.id = id
        self.name = name
        dbConnector.getInstance().put(self.id, self)
        return

    def getByID(self, id):
        dbConnector = DbConnector()
        val = dbConnector.getInstance().get(id)
        user = User()
        return user.decode(val)

    def updateToDB(self, data):
        return

    def encode(self):
        return bytes(self.toJSON(), "utf-8")
    
    def toJSON(self):
        return json.dumps(self.__dict__)

    def decode(self, data):
        json = self.fromJSON(data)
        return json

    def fromJSON(self, jsonObject):
        return json.loads(jsonObject)

    def getAllUsers(self):
        users = {}
        dbConnector = DbConnector()
        for key, value in dbConnector.getInstance().conn:
            user = User()
            users[str(key, 'utf-8')] = user.decode(value)
        return users