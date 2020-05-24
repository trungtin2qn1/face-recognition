from utils.env import getEnv

class Config:
    def __init__(self):
        return

    def load(self):
        self.cascPath = getEnv('cascPath', 'cascade/haarcascade_frontalface_default.xml')
        self.datasetPath = getEnv('datasetPath', 'dataset/')
        self.lengthSample = int(getEnv('lengthSampleStr', '1000'), base=10)
        self.webcamPos = int(getEnv('webcamPosStr', '0'), base=10)
        self.trainerPath =  getEnv('trainerPath', 'trainer/') 

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
