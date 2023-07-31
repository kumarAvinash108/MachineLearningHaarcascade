import cv2
import numpy
# face classifier
face_detect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# smile classifier
eye_detector = cv2.CascadeClassifier('haarcascade_eye.xml')

# Grab webcam feed
webcam = cv2.VideoCapture(0)

# showing the current frame

while True :
    successful_frame_read, frame = webcam.read()

    # if there's an error, break
    if not successful_frame_read:
        break

    # changing to grey scale
    grey_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # using classifier file to detect face coordinate
    face = face_detect.detectMultiScale(grey_scale)

    # same as above for smile



    # scaleFactor is the process of bluring the image
    # minNeighbors tells about minimum amount of neighbors

    for (x, y, w, h) in face:
         cv2.rectangle(frame, (x, y), (x + w, y + h), (100, 200, 50), 5)
         # getting sub frame
         the_face = frame[y:y+h, x:x+w]

         face_grey_scale = cv2.cvtColor(the_face, cv2.COLOR_BGR2GRAY)
         eye = eye_detector.detectMultiScale(face_grey_scale, scaleFactor=1.7, minNeighbors=20)

         # the code below was drawing rectangle in the smiling area

         for(x_,y_,w_,h_) in eye:
               cv2.rectangle(the_face, (x_, y_), (x_ + w_, y_ + h_), (50, 50, 200), 4)

        #code for printing smile
         # if len() > 0:
         #    cv2.putText(frame,'smiling', (x, y + h + 40), 3, cv2.FONT_HERSHEY_PLAIN, (255,255,255))







    cv2.imshow("smile detector",frame)
    key =  cv2.waitKey(1)

    if(key == 81 or key == 113) :
        break



# clean up

webcam.release()
cv2.destroyAllWindows()

print("Execution Completed")