import pyautogui
import time

msg = input('Texto pra ser enviado: ')
n = int(input('Número de vezes: '))
i = float(input('Intervalo: '))
time.sleep(7)

cont = 0
while cont < n:
    pyautogui.typewrite(msg+' ')
    pyautogui.press('enter')
    time.sleep(i)
    cont+=1
