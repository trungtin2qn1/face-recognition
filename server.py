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
        dataset = Dataset(request.webcamPos)
        dataset.make(request.userID, request.username)
        response = face_recognition_pb2.MakeDataSetResponse(msg="RPC Call is ok")
        return response

    def train(self, request, context):
        trainer = Trainer()
        trainer.train()
        response = face_recognition_pb2.TrainResponse(msg="RPC Call is ok")
        return response

    def faceRecognize(self, request, context):
        recognition = Recognition(request.webcamPos, request.subWebcamPos)
        recognition.recognize()
        response = face_recognition_pb2.FaceRecognizeResponse(msg="RPC Call is ok")
        return response

    def serve(self, port):
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

        face_recognition_pb2_grpc.add_FaceRecognizeServiceServicer_to_server(Server(), server)

        # listen on port 50051
        print('Starting server. Listening on port ' + port)
        server.add_insecure_port('[::]:' + port)
        server.start()

        while True:
            
            print("Serving face recognition service")
            time.sleep(5)

        return