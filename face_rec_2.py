import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')
# To capture video from webcam. 
cap = cv2.VideoCapture(0)
# To use a video file as input 

# cap = cv2.VideoCapture('filename.mp4')






while True:
    
    # Read the frame
    _, img = cap.read()
    font = cv2.FONT_HERSHEY_SIMPLEX

    
    cv2.putText(img,'Drakor Start-Up PROJECT ',(30,30), font, 1,(255,0,0),2)
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    eye = eye_cascade.detectMultiScale(gray, 1.1, 4)
    smile = eye_cascade.detectMultiScale(gray, 1.1, 4)
    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 1)
        cv2.putText(img,'Wajah ', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
    for (x, y, w, h) in eye:
        cv2.circle(img, (x+20, y+20), 35,  (255, 0, 0), 1)
        # cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.putText(img,'Mata ', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 1)
    for (x, y, w, h) in smile:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 255), 1)

    # Display
    cv2.imshow('img', img)

    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
        
# Release the VideoCapture object
cap.release()