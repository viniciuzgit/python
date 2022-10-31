import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import tkinter as tk
 
# Open Youtube

os.startfile("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
time.sleep(1)
pyautogui.write('youtube.com')
time.sleep(1)
pyautogui.press('enter')
pyautogui.hotkey('win', 'up')
time.sleep(5)

# Microphone Activation
pyautogui.click(1000, 100)
time.sleep(20)

pyautogui.click(800, 100)
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'c')
pyautogui.hotkey('alt', 'tab')

# My Command
r = tk.Tk()
dado_copiado = r.clipboard_get()

meuArquivo = open('comando.txt', 'w')
meuArquivo.write(dado_copiado)
meuArquivo.close()

# Lower Words
time.sleep(1)




