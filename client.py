import grpc
import face_recognition_pb2
import face_recognition_pb2_grpc

# open a gRPC channel
channel = grpc.insecure_channel('localhost:2300')

stub = face_recognition_pb2_grpc.FaceRecognizeServiceStub(channel)

# # create a stub (client)
# stub = calculator_pb2_grpc.CalculatorStub(channel)

# Should be:

cmd = input('0 for dataset \n1 for train \n2 for recognize')
if int(cmd) == 0:
    request = face_recognition_pb2.MakeDataSetRequest(webcamPos=0, userID='1', username='tin')
    response = stub.makeDataset(request)
if int(cmd) == 1:
    request = face_recognition_pb2.TrainRequest()
    response = stub.train(request)
if int(cmd) == 2:
    request = face_recognition_pb2.FaceRecognizeRequest(webcamPos=0, subWebcamPos=2)
    response = stub.faceRecognize(request)

print(response)
