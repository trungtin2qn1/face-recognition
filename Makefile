prepare:
	pip3 install pillow
	pip3 install numpy
	pip3 install opencv-contrib-python
	mkdir dataset
	mkdir trainer

dataset-static: 
	python3 dataset-static.py image cascade/haarcascade_frontalface_default.xml

dataset-cam:
	python3 dataset-cam.py cascade/haarcascade_frontalface_default.xml dataset/ 100

train:
	python3 trainer.py dataset cascade/haarcascade_frontalface_default.xml

local-run:
	python3 main.py trainer/trainer.yml cascade/haarcascade_frontalface_default.xml