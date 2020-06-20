import grpc
import face_recognition_pb2
import face_recognition_pb2_grpc

# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')


stub = face_recognition_pb2_grpc.FaceRecognizeServiceStub(channel)

# # create a stub (client)
# stub = calculator_pb2_grpc.CalculatorStub(channel)

# Should be:
# webcamPos = 0

request = face_recognition_pb2.MakeDataSetRequest()

# # create a valid request message
# number = calculator_pb2.Number(value=16)

response = stub.makeDataset(request)

# # make the call
# response = stub.SquareRoot(number)

print(response)