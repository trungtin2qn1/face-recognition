import grpc
import time
from concurrent import futures
import user_service_pb2
import user_service_pb2_grpc
from models.user import User

class UserServer(user_service_pb2_grpc.UserServiceServicer):

    def __init__(self):
        return

    def insert(self, request, context):
        user = User()
        user.insertToDB(request.id, request.name)
        response = user_service_pb2.InsertResponse(msg="RPC Call is ok")
        return response

    def getAll(self, request, context):
        user = User()
        users = user.getAllUsers()
        response = user_service_pb2.GetAllResponse(msg="RPC Call is ok", users=users)
        return response

    def getByID(self, request, context):
        user = User()
        userRes = user.getByID(request.id)
        response = user_service_pb2.GetByIDResponse(msg="RPC Call is ok", user=userRes)
        return response

    def serve(self, port):
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

        user_service_pb2_grpc.add_UserServiceServicer_to_server(UserServer(), server)

        # listen on port
        print('Starting user server. Listening on port ' + port)
        server.add_insecure_port('[::]:' + port)
        server.start()

        while True:
            
            print("Serving user service")
            time.sleep(5)

        return