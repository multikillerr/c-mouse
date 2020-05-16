import cv2
import numpy as np
import time
import shutil
import pyautogui
def main():
    print ("Hello World, This is a code written for experimenting with mouse in order to reach goals like movement and clicking without having a hardware mouse\n")
    print ("Please keep your webcam ready if its running on \n")
    cap=cv2.VideoCapture(0)
    kernelOpen=np.ones((5,5))
    kernelClose=np.ones((20,20))
    time.sleep(3)
    f1=open('/opt/c-mouse/get_resolution/width.txt','r')
    width=int(f1.readline())
    f2=open('/opt/c-mouse/get_resolution/height.txt','r')
    height=int(f2.readline())
    lower_green=np.array([65,100,100])
    upper_green=np.array([80,255,255])
    lower_red=np.array([170,100,0])
    upper_red=np.array([180,255,255])
    lower_blue=np.array([25,50,50])
    upper_blue=np.array([255,255,255])
    while(1):
        _,frame=cap.read()
        frame=cv2.resize(frame,(width,height))
        frame1=cv2.resize(frame,(200,140))
        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        mask1=cv2.inRange(hsv,lower_green,upper_green)
        mask2=cv2.inRange(hsv,lower_red,upper_red)
        mask3=cv2.inRange(hsv,lower_blue,upper_blue)
        maskOpen1=cv2.morphologyEx(mask1,cv2.MORPH_OPEN,kernelOpen)
        maskClose1=cv2.morphologyEx(maskOpen1,cv2.MORPH_CLOSE,kernelClose)
        maskFinal1=maskClose1
        maskOpen2=cv2.morphologyEx(mask2,cv2.MORPH_OPEN,kernelOpen)
        maskClose2=cv2.morphologyEx(maskOpen2,cv2.MORPH_CLOSE,kernelClose)
        maskFinal2=maskClose2
        maskOpen3=cv2.morphologyEx(mask3,cv2.MORPH_OPEN,kernelOpen)
        maskClose3=cv2.morphologyEx(maskOpen3,cv2.MORPH_CLOSE,kernelClose)
        maskFinal3=maskClose3
        conts1,h=cv2.findContours(maskFinal1.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
        conts2,h=cv2.findContours(maskFinal2.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
        conts3,h=cv2.findContours(maskFinal3.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
        mask=mask1+mask2+mask3
        for i in range(len(conts1)):
            x,y,w,h=cv2.boundingRect(conts1[i])
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)
            x_new=width-(x+w/2)
            y_new=(y+h/2)
            pyautogui.moveTo(x_new,y_new)
            for j in range(len(conts2)):
                a,b,c,d=cv2.boundingRect(conts2[j])
                cv2.rectangle(frame,(a,b),(a+c,b+d),(0,255,0),3)
                if (abs((a+c)-(x+w))+abs((b+d)-(y+h))<15 or (abs(a-x)+abs(b-y))<15):
                    pyautogui.click(button='left')
            for k in range(len(conts3)):
                l,m,n,o=cv2.boundingRect(conts3[k])
                cv2.rectangle(frame,(a,b),(a+c,b+d),(255,0,0),3)
                if (abs((l+n)-(x+w))+abs((m+o)-(y+h))<15 or (abs(l-x)+abs(m-y))<15):
                    pyautogui.click(button='right')
        res=cv2.bitwise_and(frame,frame,mask=mask)
        frame1=cv2.flip(frame1,1)
        mask=cv2.flip(mask,1)
        res=cv2.flip(res,1)
        #cv2.imshow("MaskFinal",maskFinal1)
        #cv2.imshow('frame',frame)
        #cv2.imshow('mask',mask)
        #cv2.imshow('res',res)
        #cv2.imshow('Me',frame1)
        k=cv2.waitKey(5)& 0xFF
        if k==27:
            break

    cv2.destroyAllWindows()
    cap.release()
if __name__=="__main__":
    main()
