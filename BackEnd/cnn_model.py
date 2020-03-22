from glob import glob
import cv2
import numpy as np
import pickle
from sklearn.utils import shuffle
import numpy as np
import pickle
import cv2, os
from glob import glob
from keras import optimizers
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Flatten
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.utils import np_utils
from keras.callbacks import ModelCheckpoint
from keras.backend import common as K
from keras.layers.convolutional import ZeroPadding2D
from keras.layers.convolutional import Convolution2D

def cnn_model():
    model = Sequential()
    num_of_classes=get_num_of_classes()
    model.add(ZeroPadding2D((1, 1), input_shape=(224, 224,1)))
    model.add(Convolution2D(64, 3, 3, activation='relu'))
    model.add(ZeroPadding2D((1,1)))
    model.add(Convolution2D(64, 3, 3, activation='relu'))
    model.add(MaxPooling2D((2,2), strides=(2,2)))

    model.add(ZeroPadding2D((1,1)))
    model.add(Convolution2D(128, 3, 3, activation='relu'))
    model.add(ZeroPadding2D((1,1)))
    model.add(Convolution2D(128, 3, 3, activation='relu'))
    model.add(MaxPooling2D((2,2), strides=(2,2)))

    model.add(ZeroPadding2D((1,1)))
    model.add(Convolution2D(256, 3, 3, activation='relu'))
    model.add(ZeroPadding2D((1,1)))
    model.add(Convolution2D(256, 3, 3, activation='relu'))
    model.add(ZeroPadding2D((1,1)))
    model.add(Convolution2D(256, 3, 3, activation='relu'))
    model.add(MaxPooling2D((2,2), strides=(2,2)))
  
    model.add(ZeroPadding2D((1,1)))
    model.add(Convolution2D(512, 3, 3, activation='relu'))
    model.add(ZeroPadding2D((1,1)))
    model.add(Convolution2D(512, 3, 3, activation='relu'))
    model.add(ZeroPadding2D((1,1)))
    model.add(Convolution2D(512, 3, 3, activation='relu'))
    model.add(MaxPooling2D((2,2), strides=(2,2)))
  
    model.add(ZeroPadding2D((1,1)))
    model.add(Convolution2D(512, 3, 3, activation='relu'))
    model.add(ZeroPadding2D((1,1)))
    model.add(Convolution2D(512, 3, 3, activation='relu'))
    model.add(ZeroPadding2D((1,1)))
    model.add(Convolution2D(512, 3, 3, activation='relu'))
    model.add(MaxPooling2D((2,2), strides=(2,2)))
  
    model.add(Flatten())
    model.add(Dense(4096, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(4096, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(num_of_classes, activation='softmax'))
    sgd = optimizers.SGD(lr=1e-2)
    model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])
    filepath="vgg_model16_test1.h5"
    checkpoint1 = ModelCheckpoint(filepath, monitor='val_acc', verbose=1, save_best_only=True, mode='max')
    callbacks_list = [checkpoint1]
    return model,callbacks_list

def get_num_of_classes():
    return len(glob('IMAGE_DATA/*'))

def train():
    num_of_classes=get_num_of_classes()
    with open('/content/drive/My Drive/labels','rb') as f:       
        labels=pickle.load(f)                                           ##loading labels
    lst=[]
    for i in labels:
        lst.append(i)
    lst2=[]
    ## generating one_hot vectors for the representation of the labels
    for i in labels:      
        if(i not in lst2):
            lst2.append(i)
    one_hot= np.zeros([num_of_classes,num_of_classes])
    for i in range(num_of_classes):                
        for j in range(num_of_classes):
            if(i==j):
                one_hot[i][j]=1
    train_labels5=[]
    for i in range(len(labels)):
        train_labels5.append(one_hot[lst2.index(labels[i])])
    l1=len(labels)

    train_labels=np.array(train_labels5[:int(l1*4/6)])                  ## splitting into training data 
    val_labels= np.array(train_labels5[int(l1*4/6):int(l1*5/6)])        ## validation data and test_labels
    test_labels= np.array(train_labels5[int(l1*5/6):])                  ## in the ratio of [4:1:1]
    train_images=images[:int(l1*4/6)]
    val_images=images[int(l1*4/6):int(l1*5/6)]
    test_images= images[int(l1*5/6):]

    with open('/content/drive/My Drive/images','rb') as f:
        images=np.array(pickle.load(f))                         ## loading images into a variable for training the model

    images=np.reshape(images,(len(images),224,224,1))  ##resizing images to a size of (224,224,1) to feed into the cnn_model
    

    model,callbacks_list=cnn_model()
    model.fit(np.array(train_images), train_labels,validation_data=(val_images, val_labels), epochs=10, batch_size=5, callbacks=callbacks_list)
    scores= model.evaluate(test_images,test_labels)
    model.save('/content/drive/My Drive/cnn_test_2.h5')

train()



