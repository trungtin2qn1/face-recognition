import cv2
import numpy as np
import os
import sys
from models.user import User
from services.video import Video
from datetime import datetime
from constants.constants import Constants
from datetime import date

class Recognition:

    def __init__(self, webcamPos, subWebcamPos):
        con = Constants()
        self.trainerPath = con.trainerFile
        self.cascPath = con.cascPath
        self.webcamPos = webcamPos
        self.subWebcamPos = subWebcamPos

    def recognize(self):
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read(self.trainerPath)
        faceCascade = cv2.CascadeClassifier(self.cascPath)
        font = cv2.FONT_HERSHEY_SIMPLEX

        #iniciate id counter
        id = 0
        user = User()
        users = user.getAllUsers()
        names = {}
        for v in users:
            names[v["id"]] = v["name"]

        # Initialize and start realtime video capture
        cam = cv2.VideoCapture(self.webcamPos)
        cam.set(3, 640) # set video widht
        cam.set(4, 480) # set video height
        # Define min window size to be recognized as a face
        minW = 0.1*cam.get(3)
        minH = 0.1*cam.get(4)

        count = 0

        while True:
            ret, img = cam.read()
            # img = cv2.flip(img, -1) # Flip vertically
            gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
            faces = faceCascade.detectMultiScale( 
                gray,
                scaleFactor = 1.2,
                minNeighbors = 5,
                minSize = (int(minW), int(minH)),
            )
            
            numb = 0
            name = ""

            for(x,y,w,h) in faces:
                cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

                id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
        
                # If confidence is less them 100 ==> "0" : perfect match 
                if (confidence < 100):
                    # name = names[id]
                    numb = round(100 - confidence)
                    confidence = "  {0}%".format(round(100 - confidence))
                    name = names[str(id)]
                    if numb > 60:
                        count = count + 1
                else:
                    name = "unknown"
                    confidence = "  {0}%".format(round(100 - confidence))
                    

                cv2.putText(img, name, (x+5,y-5), font, 1, (255,255,255), 2)
                cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)  
    
            cv2.imshow('camera',img) 
            k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
            if k == 27:
                break
            if (count >= 5):
                # Do a bit of cleanup
                print("\n [INFO] Exiting Program and cleanup stuff")
                cam.release()
                cv2.destroyAllWindows()

                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                today = date.today()
                day = today.strftime("%m-%d-%Y")
                videoName = "./static/" + name + "_" + str(today) + "_" + current_time + ".mp4"
                video = Video(videoName)
                video.make(self.subWebcamPos)
                break