import cv2

# open laptop webcam
cap = cv2.VideoCapture(0)

if not cap.read():
    print("Cannot open your webcam")
    
while True:
    res, frame = cap.read()
    
    if not res:
        print('cannot receive fram exiting....')
        break

    cv2.imshow('webcam', frame)
    
    if cv2.waitKey(1) == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()