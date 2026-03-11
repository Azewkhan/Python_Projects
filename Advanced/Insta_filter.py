from instafilter import Instafilter  # Its an old library probably runs on python 3.10 not after that.
import cv2

image = cv2.imread("img.jpg") #Image you want to upload

model = Instafilter("Moon", device='cpu') #Moon is the type of the filter
new_image = model(image)

cv2.imwrite("modified_image.jpg", new_image)