import numpy as np 
from keras.models import load_model
from glob import glob
import pyttsx3
import cv2 
from flask import Flask,jsonify,request
import json 
import csv
import time
import pickle

model= load_model('cnn_model.h5')   ##loading the keras model
app= Flask(__name__)

@app.route('/POST', methods=['POST'])
def get_frames():
    
    time.sleep(5)
    images1= glob("BackEnd/frames/*.jpg")   ##reading frames 
    images1.sort()
    images3=[]
    for image2 in images1:
        print(image2)
        img = cv2.imread(image2,0)
        images3.append(img)
    
    images=np.array(images3)       ##getting frames and storing it into a variable

    images_x=224
    images_y=224
    
    lst=[]
    for i in range(len(images)):
        lst.append(cv2.resize(images[i],(images_x,images_y)))   ##resizing the image to fit into the model
    
    images=np.array(lst)
    images=np.reshape(images,(len(images),224,224,1))
    
    predictions= model.predict(images)    ##predicting each frame 

    with open('sequence','rb') as f:          ## finding the sequence in which the labels were stored 
        lst2=pickle.load(f)
    
    predictions_fin=[]

    for i in range(len(images)):
        max1=max(predictions[i])
        for j in range(len(predictions[i])):    ## finding the max of each softmax output and thus predicting the correct output
                if(predictions[i][j]==max1):
                    index=j
        predictions_fin.append(lst2[index])
    
    stri=""
    for i in predictions_fin:
        stri= stri+str(i)
    
    print(stri)
    with open('FrontEnd/prediction.json','r') as json_file:
        old_string_dict_list=json.load(json_file)
    old_string_dict=old_string_dict_list[0]
    print(old_string_dict)
    old_string=old_string_dict['content']
    stri=old_string+" "+stri
    predictions_final=[{'content':stri}]
    with open('FrontEnd/prediction.json','w') as json_file:     ## writing results into a json file to forward the prediction to frontend..
        json.dump(predictions_final,json_file)
    return jsonify(predictions_final)
if __name__ == "__main__":
    app.run(debug=False, host= '0.0.0.0',threaded=False)
    

