#from pynput.keyboard import Key, Controller
import pyautogui
import cv2
import numpy as np
import wx

#keybord = Controller()

def keypress(b):
    if b==1:
        pyautogui.press('up')
    elif b==2:
        pyautogui.press('down')
    

def keyrelease(b):
    if b==1:
        pyautogui.keyUp('up')
    elif b==2:
        pyautogui.keyUp('down')
   

