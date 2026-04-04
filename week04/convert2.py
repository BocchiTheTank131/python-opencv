import cv2
import numpy as np
import matplotlib.pyplot as plt

# Kasane Teto :D
img = cv2.imread("imgs/teto.jpg")

# normal
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# grayscale 3 layers
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_3in = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)

# finding red
# HSV = color tone
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# tone lower
lower_red = np.array([0, 120, 70])
# tone higher
upper_red = np.array([10, 255, 255])
# .inRange() = range of tone color between lower and higher
mask = cv2.inRange(img_hsv, lower_red, upper_red)

# comparision between color(normal) and grayscale

# .bitwise_and() = comparision 2 things
color_part = cv2.bitwise_and(img_rgb, img_rgb, mask=mask)
gray_part = cv2.bitwise_and(gray_3in, gray_3in, mask=cv2.bitwise_not(mask))

# merge between normal image and gray scale
final_image = cv2.add(color_part, gray_part)

# show the final image after merging
plt.imshow(final_image)
# create a title
plt.title('Color Splash: Red only')
# showing the output
plt.show()