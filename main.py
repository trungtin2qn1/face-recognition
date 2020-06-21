import sys
import os
import json

from config.config import Config
from db.db import DbConnector
from services.video import Video
from server import Server
from constants.constants import Constants
from utils.video import Video
from userServer import UserServer
from threading import Thread

class Main:
    def __init__(self):
        return

    def execute(self):
        # Declare Config:
        c = Config()
        c.load()

        # Start user service
        userServer = UserServer()
        thread1 = Thread(target = UserServer.serve, args = (userServer, c.userServerPort))
        thread1.start()

        # Start face recogntion service
        server = Server()
        thread2 = Thread(target = Server.serve, args = (server, c.serverPort))
        thread2.start()

        # thread1.join()
        # thread2.join()

        while True:
            
            cmd = input('Press -1 for break: ')
            if int(cmd) == -1:
                break

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

if __name__ == "__main__":
    #TODO: 
    # Run main here:
    
    main = Main()
    main.initDB()
    main.execute()
    main.closeDB()