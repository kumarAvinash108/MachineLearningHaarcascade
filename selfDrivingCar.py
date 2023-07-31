import cv2

# our image
# img_file = 'Traffic.jpg'
# iframe = 't.mp4'
# out pre-trained car classifier

# working for people
humar_file = 'haarcascade_fullbody.xml'
humar_tracker = cv2.CascadeClassifier(humar_file)




#working for cars
classifier_file = 'cars.xml'
# creating opencv image
# img = cv2.imread(img_file)
video = cv2.VideoCapture('t.mp4')

car_tracker = cv2.CascadeClassifier(classifier_file)
# car_tracker = cv2.CascadeClassifier('cars.xml')
while True:
    (read_successful, frame) = video.read()
    if read_successful:
        grayscaled_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)


    else:
        break
    # detecting coordinates of the cars
    cars = car_tracker.detectMultiScale(frame)
    human = humar_tracker.detectMultiScale(frame)

    for (x, y, w, h) in cars:
                    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),5)

    for (x, y, w, h) in human:
                    cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),5)


    # detect cars
    # coordinates = car_tracker.detectMultiScale(grayscaled_frame)

    # for (x,y,w,h) in coordinates:
    #     cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),5)

    cv2.imshow('car detect',frame)
    key = cv2.waitKey(1)

     # Q = 81 and q= 113
    if(key == 81 or key == 113):
        break







'''  # detecting the frame
    frame_coordinates = classifier_file.detectMultiScale(grayscaled_img)

    for (x,y,w,h) in frame_coordinates:
        cv2.rectangle(frame, (x , y) ,(x+w, y+h), (255, 255, 255),5)
        '''

# converting image into gray-scaled
# img_gray = cv2.cvtColor(read_frame,cv2.COLOR_BGR2GRAY)
#
# # creating car classifier
#
#
# # detecting cars
# cars = car_tracker.detectMultiScale(img_gray) # getting coordinates
#
# # drawing the rectangle
# for (x,y,w,h) in cars:
#     cv2.rectangle(img,(x,y),(x+w, y+h),(255,255,255),5)
#
# cv2.imshow('car detector',img)

# print("code completed")