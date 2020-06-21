import sys
import os
import json

from config.config import Config
from db.db import DbConnector
from services.video import Video
from server import Server
from constants.constants import Constants
from utils.video import Video

class Main:
    def __init__(self):
        return

    def execute(self):
        # Declare Config:
        c = Config()
        c.load()

        # Start server
        server = Server()
        server.serve(c.serverPort)

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