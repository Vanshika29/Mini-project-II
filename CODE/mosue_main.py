import cv2
import numpy as np
from pynput.mouse import Button, Controller

import mouse_press
import keyboard_press
import wx


def main_virtual_mouse():

    mouse=Controller()
    #keybord = Controller()

    prey = 0
    prex = 0
    app=wx.App(False)
    (sx,sy)=wx.GetDisplaySize()
    (camx,camy)=(600,800)

    lowerBound=np.array([33,80,40])
    upperBound=np.array([102,255,255])

    cam= cv2.VideoCapture(0)

    kernelOpen=np.ones((5,5))
    kernelClose=np.ones((10,10))
    pinchFlag=0

    while True:
        ret, img=cam.read()
        img=cv2.resize(img,(300,400))

        #convert BGR to HSV
        imgHSV= cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        # create the Mask
        mask=cv2.inRange(imgHSV,lowerBound,upperBound)
        #morphology
        maskOpen=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernelOpen)
        maskClose=cv2.morphologyEx(maskOpen,cv2.MORPH_CLOSE,kernelClose)

        maskFinal=maskClose
        conts,h=cv2.findContours(maskFinal.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
        if (len(conts)==3):
            x1,y1,w1,h1=cv2.boundingRect(conts[0])
            x2,y2,w2,h2=cv2.boundingRect(conts[1])
            x3,y3,w3,h3=cv2.boundingRect(conts[2])
        
            cv2.rectangle(img,(x1,y1),(x1+w1,y1+h1),(255,0,0),2)
            cv2.rectangle(img,(x2,y2),(x2+w2,y2+h2),(255,0,0),2)
            cv2.rectangle(img,(x3,y3),(x3+w3,y3+h3),(255,0,0),2)

            mouse_press.mousepress(1)
            for i in range(100):
                pass
            mouse_press.mouserelease(1)

        elif(len(conts)==2):
            x1,y1,w1,h1=cv2.boundingRect(conts[0])
            x2,y2,w2,h2=cv2.boundingRect(conts[1])
            cv2.rectangle(img,(x1,y1),(x1+w1,y1+h1),(255,0,0),2)
            cv2.rectangle(img,(x2,y2),(x2+w2,y2+h2),(255,0,0),2)
        
            if abs(y1-y2)>20:
                if(pinchFlag==1):
                    pinchFlag=0
                    mouse_press.mouserelease(0)
        
                cv2.rectangle(img,(x1,y1),(x1+w1,y1+h1),(255,0,0),2)
                cv2.rectangle(img,(x2,y2),(x2+w2,y2+h2),(255,0,0),2)
                cx1=x1+w1//2
                cy1=y1+h1//2
                cx2=x2+w2//2
                cy2=y2+h2//2
                cx=(cx1+cx2)//2
                cy=(cy1+cy2)//2
                cv2.line(img, (cx1,cy1),(cx2,cy2),(255,0,0),2)
                cv2.circle(img, (cx,cy),2,(0,0,255),2)
                mouseLoc=(sx-(cx*sx//camx), cy*sy//camy)
                mouse.position=mouseLoc 
                while mouse.position!=mouseLoc:
                    pass
            else:
                if (y1 - prey)>0:
                    prey = y1
                    keyboard_press.keypress(2)
                    keyboard_press.keyrelease(2)
                elif (y1 - prey)<0:
                    prey = y1
                    keyboard_press.keypress(1)
                    keyboard_press.keyrelease(1)
            

        elif(len(conts)==1):
            x,y,w,h=cv2.boundingRect(conts[0])
            if(pinchFlag==0):
                pinchFlag=1
                mouse_press.mousepress(0)
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            cx=x+w//2
            cy=y+h//2
            cv2.circle(img,(cx,cy),(w+h)//4,(0,0,255),2)
            mouseLoc=(sx-(cx*sx//camx), cy*sy//camy)
            mouse.position=mouseLoc 
            while mouse.position!=mouseLoc:
                pass
        cv2.imshow("cam",img)
  
    
        if cv2.waitKey(1) == ord('q'):
            break


    cam.release()
    cv2.destroyAllWindows()