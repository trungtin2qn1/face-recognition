from db.db import DbConnector
import json
from constants.constants import Constants

class ClientCredential:

    fingerPrint = ''

    def __init__(self):
        return

    def insertToDB(self, key, fingerPrint):
        con = Constants()
        dbConnector = DbConnector()
        dbConnector.getInstance().put(key, fingerPrint)

        return

    def getByKey(self, key):
        dbConnector = DbConnector()
        val = dbConnector.getInstance().get(key)
        # clientCredential = ClientCredential()
        # return user.decode(val)
        print(val)
        return

    # def encode(self):
    #     return bytes(self.toJSON(), "utf-8")
    
    # def toJSON(self):
    #     return json.dumps(self.__dict__)

    # def decode(self, data):
    #     json = self.fromJSON(data)
    #     return json

    # def fromJSON(self, jsonObject):
    #     return json.loads(jsonObject)