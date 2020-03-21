import os
from glob import glob
import cv2
import numpy as np
import pickle
from sklearn.utils import shuffle

def pickle_images_labels():
    images_labels = []
    images = glob("Image Data/*/*.jpg")
    images.sort()
    for image in images:
        print(image)
        label = image[image.find(os.sep)+1: image.rfind(os.sep)]
        img = cv2.imread(image, 0)
        images_labels.append((np.array(img, dtype=np.uint8), (label)))
    return images_labels
images_labels = pickle_images_labels()
images_labels3 = shuffle(shuffle(images_labels))
images2, labels2 = zip(*images_labels3)
lst=[]
for i in range(len(images2)):
    lst.append(cv2.resize(images2[i],(224,224)))
images2=np.array(lst)
with open("C:/Users/Animesh/Desktop/pic/images9", "wb") as f:
    pickle.dump(images2, f)
with open("C:/Users/Animesh/Desktop/pic/labels9","wb") as f:
    pickle.dump(labels2,f)