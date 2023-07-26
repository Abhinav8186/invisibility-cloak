import cv2
import numpy as np
import time

# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# outputFile = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))

cap = cv2.VideoCapture(0)
image = cv2.imread('me.jpeg')
# time.sleep(2)
# bg = 0

while True:
    ret, frame = cap.read()
    print(frame)
    frame = cv2.resize(frame,(640,480))
    image = cv2.resize(image,(640,480))
    
    u_black = np.array([104,153,70])
    l_black = np.array([30,30,0])
    
    mask = cv2.inRange(frame,l_black,u_black)
    resp = cv2.bitwise_and(frame,frame,mask = mask)
    f = frame - resp
    f = np.where(f == 0, image,f)
    cv2.imshow('video',frame)
    cv2.imshow('mask',f)
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
        