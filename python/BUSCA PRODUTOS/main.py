from selenium import webdriver
import time
import pyautogui

pp = str(input("Nome do produto: "))

nav = webdriver.Edge(executable_path=r"C:\Users\vbernardino-ieg\Downloads\msedgedriver.exe")
nav.get("https://www.amazon.com.br/")#
time.sleep(2)
nav.find_element_by_id("twotabsearchtextbox").click()
time.sleep(2)
pyautogui.write(pp)
time.sleep(1)
nav.find_element_by_id("nav-search-submit-button").click()

nav1 = webdriver.Edge(executable_path=r"C:\Users\vbernardino-ieg\Downloads\msedgedriver copy 1.exe")
nav1.get("https://www.mercadolivre.com.br/")#
pyautogui.write(pp)
time.sleep(1)
pyautogui.press('enter')

nav2 = webdriver.Edge(executable_path=r"C:\Users\vbernardino-ieg\Downloads\msedgedriver copy 2.exe")
nav2.get("https://www.enjoei.com.br/")#
time.sleep(0.5)
pyautogui.write(pp)
time.sleep(1)
pyautogui.press('enter')

nav3 = webdriver.Edge(executable_path=r"C:\Users\vbernardino-ieg\Downloads\msedgedriver copy 3.exe")
nav3.get("https://portuguese.alibaba.com/")
time.sleep(2)
nav3.find_element_by_xpath('/html/body/div[2]/header/div[2]/div[3]/div/div/form/div[2]/input').click()
time.sleep(2)
pyautogui.write(pp)
time.sleep(1)
pyautogui.press('enter')

nav4 = webdriver.Edge(executable_path=r"C:\Users\vbernardino-ieg\Downloads\msedgedriver copy 4.exe")
nav4.get("https://shopee.com.br/")
time.sleep(2)
nav4.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/div/form/input').click()
time.sleep(2)
pyautogui.write(pp)
time.sleep(1)
pyautogui.press('enter')

nav5 = webdriver.Edge(executable_path=r"C:\Users\vbernardino-ieg\Downloads\msedgedriver copy 5.exe")
nav5.get("https://pt.aliexpress.com/?gatewayAdapt=glo2bra")
time.sleep(2)
nav5.find_element_by_id("search-key").click()
time.sleep(2)
pyautogui.write(pp)
time.sleep(1)
pyautogui.press('enter')

nav6 = webdriver.Edge(executable_path=r"C:\Users\vbernardino-ieg\Downloads\msedgedriver copy 6.exe")
nav6.get("https://www.olx.com.br/")
time.sleep(2)
nav6.find_element_by_id('searchtext').click()
time.sleep(2)
pyautogui.write(pp)
time.sleep(1)
pyautogui.press('enter')
