import cv2

# 1. Load Haar Cascade file
cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(cascade_path)

# Check file location if non-existant
if face_cascade.empty():
    print("Haar Cascade file does not exist")
    exit()
    
# 2. Load image
img = cv2.imread('D:/python-opencv/imgs/3000.jpg')

# Check file location if non-existant
if img is None:
    print("Image file does not exist")
    exit()

# 3. Convert to grayscale
grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 4. Face detection
# .detechMultiScale() = detection object (face)
faces = face_cascade.detectMultiScale(
    grayscale, # converted to grayscale
    scaleFactor=1.1, # Scan face to reduce the size
    minNeighbors=20, # should trust that it was a real face
    minSize=(30, 30) # interested the object at least 30x30 pixels in the size box
)

print(f"Face found: {len(faces)}")
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow("idk",img)
cv2.waitKey(0)
cv2.destroyAllWindows()