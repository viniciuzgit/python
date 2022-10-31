import pyautogui
import time

def escolher():
    time.sleep(7)
    pyautogui.write('y')
    time.sleep(1)
    pyautogui.press('enter')
    #atualizar
    pyautogui.click(85, 65)
    time.sleep(3)
    pyautogui.click(1020, 670)


while True:
    escolher()
