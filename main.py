import sys
import os

from config.config import Config
from recognition.dataset import Dataset
from recognition.trainer import Trainer
from recognition.recognition import Recognition

class Main:
    def __init__(self):
        return

    def execute(self):
        # Declare Config:
        c = Config()
        c.load()
        while True:

            cmd = input('press \n0:make dataset\n1:train \n2: face recognition \n-1:quit\n')

            if int(cmd) == -1:
                break
            elif int(cmd) == 0:
                dataset = Dataset(c.cascPath, c.datasetPath, c.lengthSample, c.webcamPos)
                dataset.make()
            elif int(cmd) == 1:
                trainer = Trainer(c.datasetPath, c.cascPath, c.trainerPath)
                trainer.train()
            elif int(cmd) == 2:
                recognition = Recognition(c.trainerPath + 'trainer.yml', c.cascPath, c.webcamPos)
                recognition.recognize()
    
    def initDB(self):
        return

# Run main here:
main = Main()
main.initDB()
# main.execute()