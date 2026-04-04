import cv2

cap = cv2.VideoCapture(0)

if not cap.read():
    print("Cannot open your webcam")
    
while True:
    res, frame = cap.read()
    if not res:
        print('cannot receive frame exiting....')
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow('webcam', gray)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()