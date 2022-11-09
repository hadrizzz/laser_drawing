import cv2 as cv
import numpy as np


lower = np.array([0, 0, 240])                           #choose color(hsv)
upper = np.array([255, 15, 255])                        #in this case it's white
canvas = np.zeros((800, 1280, 3), dtype='uint8')        #create canvas for drowing
frame_1 = None
temp1 = ()
temp2 = ()


webcam = cv.VideoCapture(0)                             #connect webcam

while 1:                                                #infinity loop for update frames 
    _, img = webcam.read()                              #get frame(img), _ is bool(is webcam work)
    image = cv.cvtColor(img, cv.COLOR_BGR2HSV)          #from bgr to hsv frame
    mask = cv.inRange(image, lower, upper)              #mask for computer to 'see' needed color


    contours, hierarchy = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE) 
    for contour in contours:                            #get coordinates of all pixels > 5
        if cv.contourArea(contour) > 5:                 #with needed color(first frame)
            temp1 = cv.boundingRect(contour)


    contours, hierarchy = cv.findContours(frame_1, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for contour in contours:                            #get coordinates of all pixels > 5
        if cv.contourArea(contour) > 5:                 #with needed color(previous frame)
            temp2 = cv.boundingRect(contour)

    
    if temp2 and temp1:
        cv.line(canvas,(temp2[0], temp2[1]), (temp1[0], temp1[1]), (0, 0, 255), 3)
    frame_1 = mask                                      #idea to get coordinates on frame and
    canvas = cv.addWeighted(canvas, 1, canvas, 1, 0)    #previous frame then connect them with
                                                        #with (green)line on canvas
    
    
    cv.imshow('test', canvas)
    # cv.imshow('mask', mask)                           #uncomment for seeing how computer see
    if cv.waitKey(1) == ord('q'):                       #to close programm
        break


webcam.release()
cv.destroyAllWindows()