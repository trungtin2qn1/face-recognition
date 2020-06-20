import grpc
from concurrent import futures
import time
import face_recognition_pb2
import face_recognition_pb2_grpc
from recognition.dataset import Dataset
from recognition.trainer import Trainer
from recognition.recognition import Recognition

class Server(face_recognition_pb2_grpc.FaceRecognizeServiceServicer):

    def __init__(self):
        return

    def makeDataset(self, request, context):
        response = face_recognition_pb2.MakeDataSetResponse()
        webcamPos = -1
        if request.webcamPos != -1:
            webcamPos = request.webcamPos
        dataset = Dataset(webcamPos)
        response.msg = dataset.make()
        return response

    def train(self, request, context):
        trainer = Trainer()
        response.msg = trainer.train()
        return response

    def faceRecognize(self, request, context):
        recognition = Recognition(request.webcamPos)
        response.msg = recognition.recognize()
        return response

    def serve(self, port):
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

        face_recognition_pb2_grpc.add_FaceRecognizeServiceServicer_to_server(Server(), server)

        # listen on port 50051
        print('Starting server. Listening on port ' + port)
        server.add_insecure_port('[::]:' + port)
        server.start()
        while True:
            
            cmd = input('Press -1 for break: ')
            if int(cmd) == -1:
                break

        return