import cv2

cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(cascade_path)

if face_cascade.empty():
    print("Haar cascade file does not exist")
    exit()
    
cap = cv2.VideoCapture(0)

if not cap.read():
    print('Cannot open the camera')
    exit()
    
while True:
    # declare with 2 variable as keep value as the same
    res, frame = cap.read()
    
    if not res:
        print('Cannot image reading from the camera')
        break
    
    gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray_scale,
        scaleFactor=1.1,
        minNeighbors=10,
        minSize=(30, 30)
    )
    
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x +w, y + h), (0, 255, 0), 4)
        
    cv2.imshow('face detection', frame)
    
    if cv2.waitKey(1) == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()