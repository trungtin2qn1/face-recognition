import plyvel

class DB:

    # instance = None
    # path = ''

    def __init__(self, path):
        # # print(0)
        # if self.instance != None:
        #     # print(1)
        #     raise Exception("This class is a singleton!")
        # else:
        #     # print(2)
        #     self.instance = self

        self.path = path
        return

    def open(self):
        # print('open')
        self.conn = plyvel.DB(self.path, create_if_missing=True)
        return

    def close(self):
        self.conn.close()
        return

    def Put(self, key, val):
        self.conn.put(key.encode(), val.encode())
        return

    def Get(self, key):
        return str(self.conn.get(key.encode()), 'utf-8')

    # @staticmethod
    # def getInstance():
    #     if DB.instance == None:
    #         DB(DB.path)
    #     print(DB.instance)
    #     DB.instance.open()
    #     return DB.instance

class DbConnector:
    
    instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if DbConnector.instance == None:
            DbConnector()
        return DbConnector.instance

    def __init__(self):
        if DbConnector.instance != None:
            raise Exception("This class is a singleton!")
        else:
            DbConnector.instance = self
        
        # self.open(path)
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
        return str(self.conn.get(key.encode()), 'utf-8')


class Singleton:
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if Singleton.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Singleton.__instance = self

    def print(self):
        print('Hello world')
