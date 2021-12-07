import os
import cv2
import numpy as np
import requests
import time



port_address = 'http://192.168.0.173:4747/cam/1/frame.jpg'

img_width =640
img_height = 480

while True:
    time.sleep(1)
    img_req = requests.get(port_address)
    img_arr = np.array(bytearray(img_req.content), dtype=np.uint8)  
    cap = cv2.VideoCapture('http://192.168.0.173:4747/video?640x480')

    img = cv2.imdecode(img_arr, -1)

    frame = cv2.resize(img,(img_width,img_height))
    timestr = str(time.time())
    timestr += '.png'
    print(timestr)
    cv2.imwrite('./src/img/img_from_cam/' + timestr , frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

#workes when an other instance of droidcam runs in browser
#https://github.com/ravirajsinh45/connect_mobile_camera_with_computer_using_python/blob/master/using_wifi/take_mobile_camera_input_using_IPWebcam.ipynb

cv2.destroyAllWindows()