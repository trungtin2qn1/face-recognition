import cv2
import os
import sys

def makeDatasetByCam(cascPath, datasetPath, lengthSample, webcamPos):

    # cam = cv2.VideoCapture(webcamPos)
    cam = cv2.VideoCapture(webcamPos)

    cam.set(3, 640)  # set video width
    cam.set(4, 480)  # set video height
    faceDetector = cv2.CascadeClassifier(cascPath)
    # For each person, enter one numeric face id
    faceID = input('\n enter user id end press <return> ==>  ')
    print("\n [INFO] Initializing face capture. Look the camera and wait ...")
    # Initialize individual sampling face count

    # lengthSample = int(lengthSampleStr, base=10)

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
            cv2.imwrite(datasetPath + "user." + str(faceID) + '.' +
                        str(count) + ".jpg", gray[y:y+h, x:x+w])
            cv2.imshow('image', img)
        k = cv2.waitKey(100) & 0xff  # Press 'ESC' for exiting video
        if k == 27:
            break
        elif count >= lengthSample:  # Take lengthSample face sample and stop video
            break

    # Do a bit of cleanup
    print("\n [INFO] Exiting Program and cleanup stuff")
    cam.release()
    cv2.destroyAllWindows()

