import threading
import matplotlib.pyplot as plt
import numpy as np
import cv2
from src.segment_char import segment_characters
from src.predict import show_results
from src.extract_plate import extract_plate
import os


whitelist = ["1aav005"]

while True:

    images = []
    for filename in os.listdir("./src/img/img_from_cam"):
        img = cv2.imread(os.path.join("./src/img/img_from_cam", filename))
    if img is not None:
        images.append(img)

    plateImage = extract_plate(images[len(images)-1])[1]
    char = segment_characters(plateImage)


    result = show_results(char)

    if(result):
        print(result)
        if(whitelist.__contains__(result)):
            a=0
    else:
        print('no plate scanned')