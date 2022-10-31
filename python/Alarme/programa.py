import time
import webbrowser

Set_Alarm = input("Configure o alarme como H:M:S(tudo em dois dígitos): ")
url = input('Digite o site que você quer abrir: ')
Actual_Time = time.strftime("%I:%M:%S")
while Actual_Time != Set_Alarm:
    print("Horas agora: " + Actual_Time)
    Actual_Time = time.strftime("%I:%M:%S")
    time.sleep(1)
if Actual_Time == Set_Alarm:
    print("Você pode ver sua página agora :) ")
    time.sleep(2)
    webbrowser.open(url)
