import cv2
from random import randrange
# loading some pretrained data
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# choose an image to detect a face
# img = cv2.imread('test.jpg')


# capturing the image
webcam = cv2.VideoCapture(0) # 0 is for accessing default webcam
# if you will pass the address of video it will work on video



# Now the next step is that we have to covert the image into black and white image because haarcascade algorith do not
# understand colour photos.
# face coordinate will have no of list  = number of faces in photo
# iterate forever over frames
while True:
    # Read the current frame
    successful_frame_read, frame = webcam.read()

    grayscaled_img = cv2.cvtColor(frame,cv2.COLOR_BGRA2GRAY)

    # detecting the frame
    frame_coordinates = trained_face_data.detectMultiScale(grayscaled_img)


    for (x,y,w,h) in frame_coordinates:
        cv2.rectangle(frame, (x , y) ,(x+w, y+h), (255, 255, 255),5)

    cv2.imshow('Face Detector',frame)
    # if wait key has no argument passed than it will show only one frame and to see next frame we have to press
    # spacebar if key pass 1 than after 1 milli second it will automatically press key
    key = cv2.waitKey(1) # it pauses the program on screen until any key is pressed and also returns an integer value which key was pressed

    # stopping program
    #Q = 81 and q= 113
    
    if key == 81 or key == 113:
        break






        # the code below was for the photo, same as video

    '''
# Detecting faces
face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
# detect face with multiplication
# print(face_coordinates)
for (x,y,w,h) in face_coordinates:
    cv2.rectangle(img, (x, y), (x + w, y + h), (randrange(256), randrange(256), randrange(256)), 10)
# face coordinate is a list 2D list (x,y) denotes the position at which face starts w and h are width and height

# showing image
cv2.imshow('Face Detector', img)
cv2.waitKey() # it pauses the program on screen until any key is pressed

'''