# import library OpenCV (cv2)
import cv2

# () = function

# 
img = cv2.imread('imgs/2025060616453877425_1.jpg')

# .imshow() = 1. program label, 2. input (.imread())
cv2.imshow('label', img)

# waiting key for....
# 1. 0 = any key, 2. 1 = customize key
cv2.waitKey(0)
cv2.destroyAllWindows()