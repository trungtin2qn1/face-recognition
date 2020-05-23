import sys

from dataset import makeDatasetByCam

# Declare Prerequisites:
# imagePath = sys.argv[1] # image/
cascPath = sys.argv[1]  # cascade/haarcascade_frontalface_default.xml
datasetPath = sys.argv[2]  # dataset/
lengthSampleStr = sys.argv[3]  # 100
webcamPosStr = sys.argv[4]  # 2

print('cascPath:', cascPath)
print('datasetPath:', datasetPath)
print('lengthSampleStr:', lengthSampleStr)
print('webcamPosStr:', webcamPosStr)

lengthSample = int(lengthSampleStr, base=10)
webcamPos = int(webcamPosStr, base=10)

makeDatasetByCam(cascPath, datasetPath, lengthSample, webcamPos)