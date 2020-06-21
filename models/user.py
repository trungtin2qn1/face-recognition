from db.db import DbConnector
import json
from constants.constants import Constants

class User:

    id = ""
    name = ""

    def __init__(self):
        return
    
    def getAllUserIDs(self):
        con = Constants()
        dbConnector = DbConnector()
        userIDs = dbConnector.getInstance().get(con.usersKey)
        if userIDs is not None:
            return json.loads(userIDs)
        return []

    def insertToDB(self, id, name):
        con = Constants()
        dbConnector = DbConnector()
        self.id = id
        self.name = name
        dbConnector.getInstance().put(self.id, self)
        userIDs = self.getAllUserIDs()
        for userID in userIDs:
            if userID == id:
                return
        
        userIDs.append(id)
        data = json.dumps(userIDs)
        dbConnector.getInstance().conn.put(bytes(con.usersKey, "utf-8"), bytes(data, "utf-8"))
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
        # ReImplement here
        con = Constants()
        users = []
        dbConnector = DbConnector()
        # userIDsBytes = dbConnector.getInstance().conn.get(bytes(con.usersKey, 'utf-8'))

        userIDs = self.getAllUserIDs()
        for userID in userIDs:
            data = dbConnector.getInstance().conn.get(bytes(userID, "utf-8"))
            users.append(json.loads(data))

        return users