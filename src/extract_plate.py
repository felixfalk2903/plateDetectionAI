import cv2
import matplotlib.pyplot as plt

def extract_plate(img,imgName): # the function detects and perfors blurring on the number plate.
    plate_img = img.copy()

    #Loads the data required for detecting the license plates from cascade classifier.
    plate_cascade = cv2.CascadeClassifier('./src/haarcascade-files/haarcascade_russian_plate_number.xml')

    # detects numberplates and returns the coordinates and dimensions of detected license plate's contours.
    plate_rect = plate_cascade.detectMultiScale(plate_img, scaleFactor = 1.3, minNeighbors = 7)
    plate =img.copy()

    for (x,y,w,h) in plate_rect:
        a,b = (int(0.02*img.shape[0]), int(0.025*img.shape[1])) #parameter tuning
        plate = plate_img[y+a:y+h-a, x+b:x+w-b, :]
        # finally representing the detected contours by drawing rectangles around the edges.
        cv2.rectangle(plate_img, (x,y), (x+w, y+h), (51,51,255), 3)
    cv2.imwrite('./src/img/zoomedPlate/' + imgName,plate)            
    return plate_img, plate # returning the processed image.