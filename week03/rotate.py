import cv2

img = cv2.imread("imgs/RTX_4090.jpg")

height , width = img.shape[:2]
center = (width // 2, height // 2)

# .getRotationMatrix2D() = 1. center , 2. degree , 3. scale ratio
matrix = cv2.getRotationMatrix2D(center, 45, 1.0)

img_rotate = cv2.warpAffine(img, matrix, (width, height))

cv2.imshow("rotatr", img_rotate)

cv2.waitKey(0)
cv2.destroyAllWindows()