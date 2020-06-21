prepare:
	pip3 install pillow
	pip3 install numpy
	pip3 install opencv-contrib-python
	mkdir dataset
	mkdir trainer

package:
	pip3 install -r requirements.txt

list-camera:
	v4l2-ctl --list-devices

local-run:
	python3 main.py

client:
	python3 client.py