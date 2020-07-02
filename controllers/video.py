from utils.video import Video as VideoUtils
from models.user import User
from datetime import datetime
from datetime import date

class Video:
    def __init__(self):
        return

    def make(self, userID, nameVideo, camPos):
        if nameVideo == "":
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            today = date.today()
            day = today.strftime("%m-%d-%Y")
            user = User()
            user = user.getByID(userID)
            nameVideo = "./static/" + user["name"] + "_" + str(today) + "_" + current_time + ".mp4"
            
        video = VideoUtils(nameVideo)
        video.make(camPos)
        return