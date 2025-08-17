import cv2

# This holds all of the data to actually recognise faces
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# This decides what camera on your device to choose
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera couldn't be accessed, try changing the index or inserting a new camera!")
    exit()


while True:
    
    ret, frame = cap.read()

    if not ret:
        print("Error: Couldn't retrieve frame")
        continue

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.25, minNeighbors=5, minSize=(300, 300))

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    cv2. imshow('Face Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
