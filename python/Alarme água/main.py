import time
import winsound
from win10toast import ToastNotifier
import datetime

def getTimeInput():
    hour = int(input("Horas de Intervalo: "))
    minutes = int(input("Minutos de Intervalo: "))
    seconds = int(input("Segundos de Intervalo: "))
    time_interval = seconds+(minutes*60)+(hour*3600)
    return time_interval

def log():
    now = datetime.datetime.now()
    start_time = now.strftime("%H:%M:%S")
    with open("log.txt", 'a') as f:
        f.write(f'Voce bebeu agua {now}\n')
    return 0

def notify():
    notification = ToastNotifier()
    f = 2500
    d = 2000 
    winsound.Beep(f, d)
    notification.show_toast("Hora de beber água")
    log()
    return 0

def starttime(time_interval):
    while True:
        time.sleep(time_interval)
        notify()

if __name__ == '__main__':
    time_interval = getTimeInput()
    starttime(time_interval)
