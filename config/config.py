from utils.env import getEnv
from constants.constants import Constants

class Config:
    def __init__(self):
        return

    def load(self):
        con = Constants()
        self.cascPath = getEnv('cascPath', con.cascPath)
        self.datasetPath = getEnv('datasetPath', con.datasetPath)
        self.lengthSample = int(getEnv('lengthSampleStr', str(con.lengthSample)), base=10)
        self.webcamPos = int(getEnv('webcamPosStr', '0'), base=10)
        self.trainerPath =  getEnv('trainerPath', con.trainerPath)
        self.serverPort = getEnv('trainerPath', con.serverPort)

    def getCascPath(self):
        return self.cascPath

    def getDatasetPath(self):
        return self.datasetPath
    
    def getLengthSample(self):
        return self.lengthSample

    def getWebcamPos(self):
        return self.webcamPos

    def setCascPath(self, cascPath):
        self.cascPath = cascPath

    def setDatasetPath(self, datasetPath):
        self.datasetPath = datasetPath
    
    def setLengthSample(self, lengthSample):
        self.lengthSample = lengthSample

    def setWebcamPos(self, webcamPos):
        self.webcamPos = webcamPos
