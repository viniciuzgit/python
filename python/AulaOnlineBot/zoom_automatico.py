import time
import webbrowser
import pyautogui
import winsound

Actual_Time = time.strftime("%I:%M:%S")
print("Horas agora: " + Actual_Time)
Set_Alarm = input(" Que horas você vai entrar na próxima aula? (3 min antes)  \n "
                  "configure o alarme "
                  "H:M:S(tudo em dois dígitos): ")
url = 'https://us06web.zoom.us/j/85447368950?pwd=QmRCd3dhck52eFlNSG4wbitHR3ZqZz09'

while Actual_Time != Set_Alarm:
    print("Horas agora: " + Actual_Time)
    Actual_Time = time.strftime("%I:%M:%S")
    time.sleep(1)
if Actual_Time == Set_Alarm:
    print("\n\nHORA DA AULA ")
    winsound.Beep(2500, 2000)
    time.sleep(2)
    webbrowser.open(url)

time.sleep(10)
pyautogui.click(650, 500)
time.sleep(2)
pyautogui.click(800, 200)
time.sleep(15)
pyautogui.click(900, 600)
time.sleep(10)
pyautogui.click(750, 355)
time.sleep(2)
pyautogui.hotkey('win', 'up')
