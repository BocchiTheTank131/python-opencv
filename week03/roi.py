import cv2

# library numpy using for handle list or array or calculate multi dimension or matrix
# numpy was made for high level calculation about science (Sci)
import numpy as np

# paper
# 1. size image (width, height (px)) 2. primary color (RGB)
img = np.zeros((400,600,3))

# Horizontal
# range() = 1. start 2. stop. 3. step
for x in range(0, 600, 100):
    # .line() = 1. img 2. point 1, 3. point 2, 4. color RGB, 5. line width
    cv2.line(img, (x, 0), (x, 400), (122, 122, 255), 1)
    
# Vertical
for y in range(0, 400, 100):
    cv2.line(img, (0, y), (600, y), (122, 122, 255), 1)

# Drawing a square (center) table
x1, y1 = 200, 100
x2, y2 = 400, 300

# Drawing a rectangle
# .rectangle() = 1. img 2. ROI where to draw
cv2.rectangle(img, (x1, y1), (x2, y2), (255,0,0),2)

# Text
# .putText() = 1, "string" 2. ROI 3. font 4. font size 5. color RGB 6. line width
cv2.putText(img,'my ROI area', (210, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,0,0), 2)

roi_img = img[y1:y2,x1:x2]

cv2.imshow("Main image with grid", img)
cv2.imshow("Cropped ROI", roi_img)

cv2.waitKey(0)
cv2.destroyAllWindows()