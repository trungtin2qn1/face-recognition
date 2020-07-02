from recognition.recognition import Recognition as RecognitionService

class Recognition:

    def __init__(self):
        return

    def recognize(self, webcamPos, subWebcamPos):
        recognition = RecognitionService(webcamPos, subWebcamPos)
        recognition.recognize()