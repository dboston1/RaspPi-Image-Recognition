# RaspPi-Image-Recognition
This repository contains the code utilized for an image recognition project, scaled to perform reasonably well on a Raspberry Pi. The raw model (SqueezeNet v1.0) was trained on ImageNet's synset of images, following their competition rules. Despite not having as much time to train as we would have liked, this program is surprisingly accurate (typically 80% accuracy or above). 

While Caffe was used in training the net, due to recent updates in OpenCV making it capable of loading trained Caffe nets, we only utilized OpenCV on the Pi. CTest.py is a simple python script that imports the openCV library (note paths may need to be updated), and engages the various elements necessary to make this program work as a whole. It is, essentially, the entry point.

CTest.py takes several inputs, in a specific manner - to ensure correct formatting, run it first with the "-h" flag, which will display the correct way to input parameters. 
