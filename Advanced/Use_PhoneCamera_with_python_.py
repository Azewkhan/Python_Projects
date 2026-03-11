import cv2                           #For this Task You have to download IP webcam
import numpy as np
url = "Your IP address/video"   # Here fill Your IP address from your IP webcam app after starting the server from top right corner
cp = cv2.VideoCapture(url)   # If we type 0 insteadof URL in here It will show laptop webcam 
while(True):
    camera, frame = cp.read()
    if frame is not None:
        cv2.imshow("Frame", frame)
    q = cv2.waitKey(1)
    if q==ord("q"):
        break
cv2.destroyAllWindows()