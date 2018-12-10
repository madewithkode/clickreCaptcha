import time
import pyautogui

def deceivereCaptcha():
    x = input("Enter X Coordinate:\n");
    y = input("Enter Y Coordinate:\n");
    x = int(x);
    y = int(y);
    time.sleep(5) 
    pyautogui.click(x, y)

deceivereCaptcha();