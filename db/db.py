import plyvel
# import json

class DbConnector:
    
    instance = None

    @staticmethod
    def getInstance():
        if DbConnector.instance == None:
            DbConnector()
        return DbConnector.instance

    def __init__(self):
        if DbConnector.instance == None:
            DbConnector.instance = self            
        return

    def open(self, path):
        self.conn = plyvel.DB(path, create_if_missing=True)
        return

    def close(self):
        self.conn.close()
        return

    def put(self, key, val):
        self.conn.put(key.encode(), val.encode())
        return

    def get(self, key):
        return self.conn.get(key.encode())