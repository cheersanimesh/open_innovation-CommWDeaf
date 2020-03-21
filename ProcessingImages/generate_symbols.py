import cv2
import numpy as np 
import os
vid=cv2.VideoCapture(0)
ctr=0
try:
    directory=input('Enter label for the sign Language')
    parent_dir = "/self_generated/"
    path = os.path.join(parent_dir, directory) 
    os.makedirs(path)
    while(ctr!=1001):
        print(ctr)
        success,image=vid.read()
        cv2.imwrite("/self_generated/"+directory
                +"/%d.jpg" % ctr, image)
        ctr+=1
    vid.release()
    cv2.destroyAllWindows()
except OSError as error:
    print('directory cannot be created.')
