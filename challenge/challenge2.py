import cv2

img1 = cv2.imread("imgs/RTX_4090.jpg")
img2 = cv2.imread("imgs/rx9060xt.jpg")
img3 = cv2.imread("imgs/bocchi.jpg")

img1_resize = cv2.resize(img1,(400,400))
img2_resize = cv2.resize(img2,(400,400))
img3_resize = cv2.resize(img3,(400,400))

img1_flip = cv2.flip(img1_resize, 1)
img2_flip = cv2.flip(img2_resize, 1)
img3_flip = cv2.flip(img3_resize, 1)

height , width = img1_flip.shape[:2]
center = (width // 2, height // 2)

matrix = cv2.getRotationMatrix2D(center, 15, 1.0)

img1_rotate = cv2.warpAffine(img1_flip, matrix, (width, height))
img2_rotate = cv2.warpAffine(img2_flip, matrix, (width, height))
img3_rotate = cv2.warpAffine(img3_flip, matrix, (width, height))

new_img1 = cv2.imwrite("new_img1.jpg", img1_rotate)
new_img2 = cv2.imwrite("new_img2.jpg", img2_rotate)
new_img3 = cv2.imwrite("new_img3.jpg", img3_rotate)

file1 = cv2.imread("new_img1.jpg")
file2 = cv2.imread("new_img2.jpg")
file3 = cv2.imread("new_img3.jpg")

cv2.imshow("newImage1", file1)
cv2.imshow("newImage2", file2)
cv2.imshow("newImage3", file3)

cv2.waitKey(0)
cv2.destroyAllWindows()