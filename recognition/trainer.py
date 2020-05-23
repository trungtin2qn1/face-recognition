import cv2
import numpy as np
from PIL import Image
import os
import sys

#trainer/

class Trainer:
    def __init__(self, datasetPath, cascPath, trainerPath):
        self.cascPath = cascPath
        self.datasetPath = datasetPath
        self.trainerPath = trainerPath

    # function to get the images and label data

    def getImagesAndLabels(self, path, detector):
        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
        faceSamples = []
        ids = []
        for imagePath in imagePaths:
            PIL_img = Image.open(imagePath).convert('L')  # grayscale
            img_numpy = np.array(PIL_img, 'uint8')
            id = int(os.path.split(imagePath)[-1].split(".")[1])
            faces = detector.detectMultiScale(img_numpy)
            for (x, y, w, h) in faces:
                faceSamples.append(img_numpy[y:y+h, x:x+w])
                ids.append(id)
        return faceSamples, ids

    def train(self):
        # Path for face image database
        path = self.datasetPath
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        detector = cv2.CascadeClassifier(self.cascPath)
        print("\n [INFO] Training faces. It will take a few seconds. Wait ...")
        faces, ids = self.getImagesAndLabels(path, detector)
        recognizer.train(faces, np.array(ids))
        # Save the model into trainer/trainer.yml
        recognizer.write(self.trainerPath + 'trainer.yml')
        # Print the numer of faces trained and end program
        print("\n [INFO] {0} faces trained. Exiting Program".format(
            len(np.unique(ids))))

    def getTrainerPath():
        return

