import cv2

img = cv2.imread("imgs/2025060616453877425_1.jpg")

# save an image
# .imwrite() = 1. new file name, 2. input
newImage = cv2.imwrite('newFile.jpg', img)

newFile = cv2.imread('newFile.jpg')

cv2.imshow('New File', newFile)

cv2.waitKey(0)
cv2.destroyAllWindows()