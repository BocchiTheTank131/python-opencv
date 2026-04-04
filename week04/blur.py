import cv2
# Kasane teto :D

img = cv2.imread("imgs/teto.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# .GaussianBlur() = 1. input 2. (kernel <odd numeric>) 3. rubbing intensity
# kernel = size of image for blur 5x5 (if kernel is greater = more blur)
blurred = cv2.GaussianBlur(gray, (5,5),0)

# .Canny() = draw lines at the edges
edges = cv2.Canny(blurred, 10, 100)

cv2.imshow('blurred', blurred)
cv2.imshow("smooth edges", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()