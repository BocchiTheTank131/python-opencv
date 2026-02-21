import cv2

cap = cv2.VideoCapture('video/meme1.mp4')

while cap.isOpened():
    # res = result
    res, frame = cap.read()
    
    if not res:
        print("Not find the video")
        break
    
    cv2.imshow('output',frame)
    
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()