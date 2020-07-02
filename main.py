import sys
import os
import json

from config.config import Config
from db.db import DbConnector
from constants.constants import Constants
from controllers.user import User
from controllers.video import Video
from controllers.dataset import Dataset
from controllers.trainer import Trainer
from controllers.recognize import Recognition
class Main:
    def __init__(self):
        return

    def execute(self):
        # Declare Config:
        c = Config()
        c.load()

        # # Start user service
        # userServer = UserServer()
        # thread1 = Thread(target = UserServer.serve, args = (userServer, c.userServerPort))
        # thread1.start()

        # # Start face recogntion service
        # server = Server()
        # thread2 = Thread(target = Server.serve, args = (server, c.serverPort))
        # thread2.start()

        # # thread1.join()
        # # thread2.join()

        while True:
            
            print("Press 0 for inserting user\n")
            print("Press 1 for getting all user\n")
            print("Press 2 for getting user by id\n")
            print("Press 3 for making dataset\n")
            print("Press 4 for training data\n")
            print("Press 5 for recognizing\n")
            print("Press 6 for making video\n")
            cmd = input('Press -1 for break: \n')
            
            if int(cmd) == -1:
                break
            
            if int(cmd) == 0:
                user = User()
                user.insertToDB('1', replaceStr('Tin Huynh'))

            if int(cmd) == 1:
                user = User()
                res = user.getAllUser()
                print("get all user: ", res)

            if int(cmd) == 2:
                user = User()
                res = user.getUserByID('1')
                print("get user by id: ", res)

            if int(cmd) == 3:
                dataset = Dataset()
                dataset.make(0, '1')

            if int(cmd) == 4:
                trainer = Trainer()
                trainer.train()

            if int(cmd) == 5:
                recognition = Recognition()
                recognition.recognize(0, 0)

            if int(cmd) == 6:
                video = Video()
                video.make('1', '', 0)

        return

    def initDB(self):
        # init levelDB
        con = Constants()
        dbConnector = DbConnector()
        dbConnector.open(con.dataDir)
        return

    def closeDB(self):
        dbConnector = DbConnector()
        dbConnector.getInstance().close()
        return

def replaceStr(str):
    res = str.replace(" ", "_")
    return res

if __name__ == "__main__":
    #TODO: 
    # Run main here:
    
    main = Main()
    main.initDB()
    main.execute()
    main.closeDB()