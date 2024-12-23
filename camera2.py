
import numpy as np
import cv2 as cv
 

# make sure the xml model file is in same directory as this program.
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Read the input image
#img = cv2.imread('monalisa.jpg')

# Convert into grayscale
#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#plt.imshow(gray)



cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
 
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Detect faces
    #detectMultScale returns an 2d ndarray
    faces = face_cascade.detectMultiScale(gray)
    print('detected face(s) at:', faces)

    # Draw rectangle around the faces
    for (x, y, w, h) in faces:
      cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 255), 5)
      cv2.rectangle(img, (x-5, y-5), (x+w+5, y+h+5), (0, 0, 0), 5)

    # Display the resulting frame
    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
        break
 
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
