import threading
import matplotlib.pyplot as plt
import numpy as np
import cv2
from src.segment_char import segment_characters
from src.predict import show_results
from src.extract_plate import extract_plate
import os
import time

green = cv2.imread("./src/img/colors/green.png")


whitelist = ["1AAV005","1AAC588"]

while True:

    images = []
    imageNames = []
    for filename in os.listdir("./src/img/img_from_cam"):
        img = cv2.imread(os.path.join("./src/img/img_from_cam", filename))
        imageNames.append(filename)
    if img is not None:
        images.append(img)

    plateImage = extract_plate(images[len(images)-1],imageNames[len(imageNames)-1])[1]
    char = segment_characters(plateImage,imageNames[len(imageNames)-1])


    result = show_results(char)
    time.sleep(1.5)
    if(result):
        print(result)
        if result in whitelist:
            plt.imshow(green)
            plt.show()
    else:
        print('no plate scanned')

    if cv2.waitKey(1) & 0xFF == 27:
        break


cv2.destroyAllWindows()