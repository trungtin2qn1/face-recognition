from models.user import User as UserModel

class User:

    def __init__(self):
        return

    def insertToDB(self, id, name):
        user = UserModel()
        name = replaceStr(name)
        user.insertToDB(id, name)
        return

    def getAllUser(self):
        user = UserModel()
        users = user.getAllUsers()
        return users

    def getUserByID(self, id):
        user = UserModel()
        res = user.getByID(id)
        return res