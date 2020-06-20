import cv2
import os
import sys
import numpy as np
import multiprocessing
import time
import threading
# import thread

# For each person, enter one numeric face id

def makeVideo(cv2):
    # Press Q on keyboard to stop recording
    cv2.waitKey(1)
    # if  & 0xFF == ord('q'):

class Video:
    def __init__(self, nameVideo):
        self.nameVideo = nameVideo

    def make(self, videoPos):
        # Create a VideoCapture object
        cap = cv2.VideoCapture(videoPos)

        # Check if camera opened successfully
        if (cap.isOpened() == False): 
            print("Unable to read camera feed")

        # Default resolutions of the frame are obtained.The default resolutions are system dependent.
        # We convert the resolutions from float to integer.
        frame_width = int(cap.get(3))
        frame_height = int(cap.get(4))

        # Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.
        out = cv2.VideoWriter(self.nameVideo, cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))

        while(True):
            ret, frame = cap.read()

            if ret == True: 
    
                # Write the frame into the file 'output.avi'
                out.write(frame)

                # Display the resulting frame    
                cv2.imshow('frame',frame)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            # Break the loop
            else:
                break  

        # When everything done, release the video capture and video write objects
        cap.release()
        out.release()

        # Closes all the frames
        cv2.destroyAllWindows()

video = Video("main-cam.mp4")
subCam = Video("subcam.mp4")
x = threading.Thread(target=subCam.make, args=(2))
x.start()
# thread.start_new_thread(subCam.make, (2))
video.make(0)
# subCam.make(2) 