import cv2

img = cv2.imread("imgs/2025060616453877425_1.jpg")

if img is None:
    print('Cloud not found reading the image')
   
# .cvtColor() = 1. input (image color), 2. function() 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

newImage = cv2.imwrite('grayScale.jpg', gray)

newFile = cv2.imread('grayScale.jpg')

cv2.imshow('grayScale',newFile)

cv2.waitKey(0)
cv2.destroyAllWindows()