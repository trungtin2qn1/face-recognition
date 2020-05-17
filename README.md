## Face recognition for safe cash service

### Environment:
- python 3
- opencv framwork
- active webcam or self camera

### Usage:
1. Run command `make prepare` for preparing data
2. run command: `python3 dataset.py` for face detection and data gathering (create dataset)
3. run command `python3 trainer.py` for train data from dataset
4. run command `python3 face-recognition` for processing face recognition