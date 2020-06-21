import cv2
import os
import sys
from models.user import User
from constants.constants import Constants

class Dataset:

    def __init__(self, webcamPos):
        con = Constants()
        self.webcamPos = webcamPos
        self.lengthSample = con.lengthSample
        self.datasetPath = con.datasetPath
        self.cascPath = con.cascPath
    
    def make(self, userID, username):

        cam = cv2.VideoCapture(self.webcamPos)

        cam.set(3, 640)  # set video width
        cam.set(4, 480)  # set video height
        faceDetector = cv2.CascadeClassifier(self.cascPath)
        # For each person, enter one numeric face id

        # Handle user here:
        user = User()
        if user.getByID(userID) is None:
            return "User is not available in database"
            print("User is not available in database")
            savedUser = user.insertToDB(userID, username)
        
        print("\n [INFO] Initializing face capture. Look the camera and wait ...")

        # Initialize individual sampling face count
        count = 0
        while(True):
            ret, img = cam.read()
            # img = cv2.flip(img, -1) # flip video image vertically
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = faceDetector.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
                count += 1
                # Save the captured image into the datasets folder
                cv2.imwrite(self.datasetPath + "user." + str(userID) + '.' +
                            str(count) + ".jpg", gray[y:y+h, x:x+w])
                cv2.imshow('image', img)
            k = cv2.waitKey(100) & 0xff  # Press 'ESC' for exiting video
            if k == 27:
                break
            elif count >= self.lengthSample:  # Take lengthSample face sample and stop video
                break

        # Do a bit of cleanup
        cam.release()
        cv2.destroyAllWindows()
        print("\n Finish making dataset process")
        return