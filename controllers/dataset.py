from constants.constants import Constants
from recognition.dataset import Dataset as DatasetModel
from models.user import User

class Dataset:

    def __init__(self):
        return

    def make(self, camPos, userID):
        dataset = DatasetModel(camPos)
        user = User()
        user = user.getByID(userID)
        dataset.make(userID, user['name'])
        return