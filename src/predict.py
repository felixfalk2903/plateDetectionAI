
import matplotlib.pyplot as plt
import numpy as np
import cv2
import tensorflow as tf

def fix_dimension(img): 
  new_img = np.zeros((28,28,3))
  for i in range(3):
    new_img[:,:,i] = img
  return new_img
  
def show_results(char):
    dic = {}
    characters = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i,c in enumerate(characters):
        dic[i] = c

        
    model = tf.keras.models.load_model("./src/NumberRecognitionModel")
    output = []
    for i,ch in enumerate(char): #iterating over the characters
        img_ = cv2.resize(ch, (28,28))
        img = fix_dimension(img_)
        img = img.reshape(1,28,28,3) #preparing image for the model
        #y_ = model.predict_classes(img)[0] #predicting the class
        predict_y = model(img)#CHANGED
        classes_y = np.argmax(predict_y)
        character = dic[classes_y] #
        output.append(character) #storing the result in a list
        
    plate_number = ''.join(output)
    
    return plate_number