## Face recognition for safe cash service

### Environment:
- python 3
- opencv framwork
- active webcam or self camera

### Usage:
1. Run command `make prepare` for preparing data
2. run command: `make dataset-cam` for face detection and data gathering (create dataset)
3. run command `make train` for train data from dataset
4. run command `make local-run` for processing face recognition

### Roadmap:

`https://docs.google.com/document/d/1WHhv1zjqQ9R8AlJODG6ZCzdisXQ8fEWP481_iZn_4-8/edit?usp=sharing`


### Update:

Update save video

### Grpc:

**Files:**

- proto
- server.py
- client.py
- pb2.py
- pb2_grpc.py

**Blog:**

https://www.semantics3.com/blog/a-simplified-guide-to-grpc-in-python-6c4e25f0c506/

**Flow:**

1. Build file .proto
2. generate file .py with command: `python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. user-service.proto`
3. For server part:
   1. Use file `server.py`
   2. Generate a rpc like an object for clients use
4. For client part:
   1. Use file `client.py`
   2. Use object of server and use it method and properties