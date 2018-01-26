import numpy as np
import os

#CAR 4WD TRUCK MOTORCYCLE
 
CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))
DATA_DIR = os.path.abspath(os.path.join(CURRENT_DIR, 'Training'))  #directory with .jpg files
TXT_DIR = os.path.abspath(os.path.join(CURRENT_DIR, ''))    #store in current directory
 
car_images = [image for image in os.listdir(DATA_DIR) if 'CAR' in image]
fwd_images = [image for image in os.listdir(DATA_DIR) if '4WD' in image]
truck_images = [image for image in os.listdir(DATA_DIR) if 'TRUCK' in image]
motorcycle_images = [image for image in os.listdir(DATA_DIR) if 'MOTORCYCLE' in image]
 
car_train = car_images[:int(len(car_images)*0.7)]
car_test = car_images[int(len(car_images)*0.7):]
 
fwd_train = fwd_images[:int(len(fwd_images)*0.7)]
fwd_test = fwd_images[int(len(fwd_images)*0.7):]

truck_train = truck_images[:int(len(truck_images)*0.7)]
truck_test = truck_images[int(len(truck_images)*0.7):]

motorcycle_train = motorcycle_images[:int(len(motorcycle_images)*0.7)]
motorcycle_test = motorcycle_images[int(len(motorcycle_images)*0.7):]
 
with open('{}/train.txt'.format(TXT_DIR), 'w') as f:
    for image in car_train:
        f.write('Users/drewboston/Desktop/NET/data/Training/{} 0\n'.format(image))
    for image in fwd_train:
        f.write('Users/drewboston/Desktop/NET/data/Training/{} 1\n'.format(image))
    for image in truck_train:
        f.write('Users/drewboston/Desktop/NET/data/Training/{} 2\n'.format(image))
    for image in motorcycle_train:
        f.write('Users/drewboston/Desktop/NET/data/Training/{} 3\n'.format(image))
    f.close()
 
with open('{}/test.txt'.format(TXT_DIR), 'w') as f:
    for image in car_test:
        f.write('Users/drewboston/Desktop/NET/data/Training/{} 0\n'.format(image))
    for image in fwd_test:
        f.write('Users/drewboston/Desktop/NET/data/Training/{} 1\n'.format(image))
    for image in truck_test:
        f.write('Users/drewboston/Desktop/NET/data/Training/{} 2\n'.format(image))
    for image in motorcycle_test:
        f.write('Users/drewboston/Desktop/NET/data/Training/{} 3\n'.format(image))
    f.close()
