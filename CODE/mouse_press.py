from pynput.mouse import Button, Controller

import cv2
import numpy as np
import wx
m=Controller()

def mousepress(b):
    if b==0:
        m.press(Button.left)
    elif b==1:
        m.press(Button.right)

def mouserelease(b):
    if b==0:
        m.release(Button.left)
    elif b==1:
        m.release(Button.right)


