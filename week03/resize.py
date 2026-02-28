import cv2

img = cv2.imread("imgs/RTX_4090.jpg")

# Resize
# .resize() = 1. image (input), 2. (width <px>, height <px>)
img_resize = cv2.resize(img, (300, 450))


cv2.imshow("resize", img_resize)
cv2.waitKey(0)
cv2.destroyAllWindows()