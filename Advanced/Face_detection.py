import cv2
img = cv2.imread('img.jpg')

face_cascade = cv2.CascadeClassifier('face_detection.xml') # Pre trained model which can be downloaded in XML files
faces = face_cascade.detectMultiScale(img, 1.1, 4)
for (x, y, w, h) in faces:  # This is gonna put a rectangle on detected faces
  cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
cv2.imwrite("face_detected.png", img) 
print('Successfully saved')