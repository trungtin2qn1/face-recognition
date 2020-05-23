import cv2
import os
import sys
# For each person, enter one numeric face id

class Dataset:
    def __init__(self, imagePath, cascPath):
        self.imagePath = imagePath
        self.cascPath = cascPath

    def make(self):
        faceDetector = cv2.CascadeClassifier()

        faceID = input('\n enter user id end press <return> ==>  ')
        print("\n [INFO] Initializing face capture. Look the camera and wait ...")

        count = 0
        while(True):

        imagePath = self.imagePath + "tin.jpg"

        img = cv2.imread(imagePath)

        # ret, img = cam.read()
        # img = cv2.flip(img, -1) # flip video image vertically
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceDetector.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
            count += 1
            # Save the captured image into the datasets folder
            cv2.imwrite("dataset/User." + str(faceID) + '.' +  
                        str(count) + ".jpg", gray[y:y+h,x:x+w])
            cv2.imshow('image', img)
    print("\n [INFO] Exiting Program and cleanup stuff")
    

    # k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
    # if k == 27:
    #     break
    # elif count >= 100: # Take 30 face sample and stop video
    #     break
# Do a bit of cleanup

# cam.release()
# cv2.destroyAllWindows()        

