import cv2
import numpy as np

cap = cv2.VideoCapture(0)
lowerbound = np.array([33,80,40])
upperbound = np.array([102,255,255])
kernelopen = np.ones((5,5))
kernelclose = np.ones((20,20))
#font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX,2,0.5,0,3,1)

while True:
    _ , frame = cap.read()

    img = cv2.resize(frame,(340,220))

    imghsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    
    mask = cv2.inRange(imghsv,lowerbound,upperbound)
    
    maskopen = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernelopen)
    maskclose = cv2.morphologyEx(maskopen,cv2.MORPH_CLOSE,kernelclose)

    maskfinal = maskclose

    cont,h = cv2.findContours(maskfinal.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    
    cv2.drawContours(img,cont,-1,(255,0,0),2)
    for i in range(len(cont)):
        x,y,w,h = cv2.boundingRect(cont[i])
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        #cv2.cv.PutText(cv2.cv.fromarray(img),str(i+1),(x,y+h),)





    #cv2.imshow("msakclose",maskclose)
    #cv2.imshow("maskopen",maskopen)
    #cv2.imshow("mask",mask)
    cv2.imshow("original",img)
    k = cv2.waitKey(10)

    if k == ord('q'):
        QuitProgram()


