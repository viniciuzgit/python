# ctrl + f5 = run

# Open Youtube

import time
import os
import pyautogui
import tkinter as tk
import pyttsx3

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
pyautogui.hotkey('alt', 'tab')

# Lower Words
time.sleep(1)
os.startfile('comando.txt')
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('alt', 'tab')
texto = ''
pyautogui.click(170, 20)
pyautogui.click(155, 80)
pyautogui.write('texto')
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(0.2)
pyautogui.press('right')
time.sleep(0.2)
pyautogui.press('right')
time.sleep(0.2)
pyautogui.press('right')
time.sleep(0.2)
pyautogui.press('right')
time.sleep(0.2)
pyautogui.press('right')
time.sleep(0.2)
pyautogui.press('right')
time.sleep(0.2)
pyautogui.press('right')
time.sleep(0.2)
pyautogui.press('right')
time.sleep(0.2)
pyautogui.press('right')
pyautogui.hotkey('ctrl', 'v')
texto.lower()

# Identificar o comando e executar

texto.lower()

if texto == 'quero assistir filmes e séries' or texto == 'filme' or texto == 'quero assistir filme' or texto == 'quero assistir filmes' or texto == 'série' or texto == 'quero assistir série' or texto == 'quero assistir séries' or texto == 'séries' or texto == 'filmes':
    os.startfile("C:\Users\vbernardino-ieg\AppData\Roaming\Telegram Desktop\Telegram.exe")
    time.sleep(2)
    pyautogui.click(pyautogui.click(150, 50))
    pyautogui.write('@NetflixFilmesESeries_Bot')
    pyautogui.click(pyautogui.click(150, 120))
    pyautogui.write('Main Menu')
    pyautogui.press('enter')
    time.sleep(2)

    def convertTexto(texto):
        engine = pyttsx3.init()
        engine.say(texto)
        engine.runAndWait()


    convertTexto("aqui estão seus filmes e séries")



