import pyautogui
import time

time.sleep(7)
message = '3 - MESSAGE.txt'
f = open(message, 'r')
for word in f:
    pyautogui.typewrite(word*100)
    pyautogui.press('enter')
    time.sleep(0.3)
