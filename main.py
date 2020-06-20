import sys
import os

from config.config import Config
from db.db import DbConnector
from services.video import Video
from server import Server

class Main:
    def __init__(self):
        return

    def execute(self):
        # Declare Config:
        c = Config()
        c.load()

        # Start server
        server = Server()
        server.serve("2300")

        return

    def initDB(self):
        dbConnector = DbConnector()
        dbConnector.open('./leveldb')
        return

    def closeDB(self):
        dbConnector = DbConnector()
        dbConnector.getInstance().close()
        return

if __name__ == "__main__":
    # Run main here:
    main = Main()
    main.initDB()
    main.execute()
    main.closeDB()