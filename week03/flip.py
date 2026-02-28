import cv2

img = cv2.imread("imgs\RTX_4090.jpg")

# .flip() = 1. image (input), 2. 1: horizontally, 0: vertically
img_flip = cv2.flip(img, 0)

cv2.imshow("flip",img_flip)
cv2.waitKey(0)
cv2.destroyAllWindows()