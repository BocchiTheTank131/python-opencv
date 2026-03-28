# HSV vs RGB
# RGB = one color only
# HSV = tone and vibrancy of color

import cv2

# Kasane Teto :D
img = cv2.imread("imgs/teto.jpg")

# grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# mask
_, mask = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

#
result = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow('original', img)
cv2.imshow("grayscale", gray)
cv2.imshow('mask', mask)
cv2.imshow('result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()