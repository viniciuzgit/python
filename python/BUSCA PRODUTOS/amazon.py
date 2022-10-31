import time
import pyautogui
from selenium import webdriver
from tkinter import Tk


pp = str(input("Nome do produto: "))
r = Tk()
nav = webdriver.Edge(executable_path=r"C:\Users\vbernardino-ieg\Downloads\msedgedriver.exe")
nav.get("https://www.amazon.com.br/")
time.sleep(2)
nav.find_element_by_id("twotabsearchtextbox").click()
time.sleep(2)
pyautogui.write(pp)
time.sleep(1)
nav.find_element_by_id("nav-search-submit-button").click()
time.sleep(2)
nav.find_element_by_xpath('//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div[3]/div/div/div/div/div/div/div[2]/div[1]/h2/a/span').click()
pyautogui.tripleClick(495, 405)
pyautogui.hotkey('ctrl', 'c')
nome_1 = r.clipboard_get()
pyautogui.doubleClick(495, 505)
pyautogui.hotkey('ctrl', 'c')
preco = r.clipboard_get()
p = str(preco)
print(' '*200)
print(f'Produto Encontrado: {nome_1}')
print(f'Preço: {p}')
