import cv2
import numpy as np
from pynput.mouse import Button, Controller
import wx

mouse = Controller()
app = wx.App(False)
(sx,sy) = (1980,1080)
(camx,camy) = (600,800)

cap = cv2.VideoCapture(0)
cap.set(3,camx)
cap.set(4,camy)

lowerbound = np.array([33,80,40])
upperbound = np.array([102,255,255])
kernelopen = np.ones((5,5))
kernelclose = np.ones((20,20))
#font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX,2,0.5,0,3,1)

mlocold=np.array([0,0])
mouseloc  = np.array([0,0])
dampingfactor = 2
pinchflag = 0

while True:
    _ , img = cap.read()

    img = cv2.resize(img,(600,800))

    imghsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    
    mask = cv2.inRange(imghsv,lowerbound,upperbound)
    
    maskopen = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernelopen)
    maskclose = cv2.morphologyEx(maskopen,cv2.MORPH_CLOSE,kernelclose)

    maskfinal = maskclose

    cont,h = cv2.findContours(maskfinal.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    
    #cv2.drawContours(img,cont,-1,(255,0,0),2)
    
    
    # for Drwaing the boxes around the color segmented image

    #for i in range(len(cont)):
     #   x,y,w,h = cv2.boundingRect(cont[i])
      #  cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        #cv2.cv.PutText(cv2.cv.fromarray(img),str(i+1),(x,y+h),)

    if len(cont) == 2:
        if pinchflag==1:
            pinchflag=0
            mouse.release(Button.left)
        
        x1,y1,w1,h1 = cv2.boundingRect(cont[0])
        x2,y2,w2,h2 = cv2.boundingRect(cont[1])
        cv2.rectangle(img,(x1,y1),(x1+w1,y1+h1),(250,0,0),2)
        cv2.rectangle(img,(x2,y2),(x2+w2,y2+h2),(250,0,0),2)
         
        cx1 = int(x1+w1/2)
        cy1 = int(y1+h1/2)

        cx2 = int(x2+w2/2)
        cy2 = int(y2+h2/2)

        cx = int((cx1+cx2)/2)
        cy = int((cy1+cy2)/2)


        cv2.line(img,(cx1,cy1),(cx2,cy2),(255,0,0),2)
        cv2.circle(img,(cx,cy),2,(0,0,255),2)
        
        mouseloc = mlocold + ((cx,cy)-mlocold)//dampingfactor


         
        mouse.position = (sx-(mouseloc[0]*sx//camx),sy-(mouseloc[1]*sy//camy))

        #mouse.release(Button.left)
        while mouse.position != (sx-(mouseloc[0]*sx//camx),sy-(mouseloc[1]*sy//camy)):
            pass
        
        mlocold = mouseloc



    elif (len(cont)==1):
        if pinchflag == 0:
            pinchflag = 1
            mouse.press(Button.left)


        x,y,w,h = cv2.boundingRect(cont[0])
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

        cx = int((x+w)/2)
        cy = int((y+h)/2)

        #cv2.circle(img,(cx,cy),(w+h)//4,(0,0,255),2)
        mouseloc = mlocold + ((cx,cy)-mlocold)//dampingfactor


         
        mouse.position = (sx-(mouseloc[0]*sx//camx),sy-(mouseloc[1]*sy//camy))

        #mouse.release(Button.left)
        while mouse.position != (sx-(mouseloc[0]*sx//camx),sy-(mouseloc[1]*sy//camy)):

            pass
        
        mlocold = mouseloc
        

    #cv2.imshow("msakclose",maskclose)
    #cv2.imshow("maskopen",maskopen)
    #cv2.imshow("mask",mask)
    cv2.imshow("original",img)
    cv2.waitKey(10)


