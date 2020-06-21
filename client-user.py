import grpc
import user_service_pb2
import user_service_pb2_grpc

# open a gRPC channel
channel = grpc.insecure_channel('localhost:2350')

stub = user_service_pb2_grpc.UserServiceStub(channel)

cmd = input('0 for inserting \n1 for getting all \n2 for getting by id')
if int(cmd) == 0:
    request = user_service_pb2.InsertRequest(id='2', name='tin')
    response = stub.insert(request)
if int(cmd) == 1:
    request = user_service_pb2.GetAllRequest()
    response = stub.getAll(request)
if int(cmd) == 2:
    request = user_service_pb2.GetByIDRequest(id='2')
    response = stub.getByID(request)

print(response)
