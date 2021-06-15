import numpy as np 
import cv2
from datetime import datetime
flag=0
cap = cv2.VideoCapture(0)
while(cap.isOpened()):
    ret, frame = cap.read()
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    font= cv2.FONT_HERSHEY_SIMPLEX
    org = (5,30)
    fontScale = 1
    color = (255, 0, 0)
    thickness = 2
    frame=cv2.putText(frame,'cam1',org,font,fontScale,color,thickness,cv2.LINE_AA)
    frame = cv2.putText(frame,str(datetime.now()),(400,20),font,0.5,(255,255,255),2,cv2.LINE_AA)
    if ret==True:
        cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("QUIT")
        break
    if cv2.waitKey(1) & 0xFF == ord('i'):
        frame = cv2.imread("Laptop.jpg")
        print("IMAGE")
        window_name = 'frame'
        
        cv2.imwrite(window_name,frame)
    elif cv2.waitKey(1) & 0xFF == ord('r'):
        fourcc = cv2.VideoWriter_fourcc(*'XVID') 
        #out = cv2.VideoWriter('C:\\Users\\hp\\Desktop\\internship\\vira9.mp4', fourcc, 20.0, (640, 450))
        out = cv2.VideoWriter('Rec.mp4', fourcc, 20.0, (640, 480))
        print("REC")
        flag=1
    if flag==1:
        out.write(frame)
cap.release()
if(flag==1):
    
    out.release()
cv2.destroyAllWindows() 


















