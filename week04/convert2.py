import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("imgs/teto.jpg")

# normal
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# grayscale 3 layers
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_3in = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)

# finding red
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# R G B
# 1 1 1

# High R G B = 2 2 2
lower_red = np.array([0, 120, 70])
upper_red = np.array([10, 255, 255])
mask = cv2.inRange(img_hsv, lower_red, upper_red)

color_part = cv2.bitwise_and(img_rgb, img_rgb, mask=mask)
gray_part = cv2.bitwise_and(gray_3in, gray_3in, mask=cv2.bitwise_not(mask))

final_image = cv2.add(color_part, gray_part)

plt.imshow(final_image)
plt.title('Color Splash: Red only')
plt.show()
# cv2.imshow("Output", final_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()