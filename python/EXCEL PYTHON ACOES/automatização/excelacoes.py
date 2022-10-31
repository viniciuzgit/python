import time 
import pyautogui

def ec():
    pyautogui.click(750, 300)
def r():
    pyautogui.press('right')
    pyautogui.click(960, 190)
def volta():
    pyautogui.press('enter')
    pyautogui.press('up')
def site():
    pyautogui.click(500, 100)

def cod_acao():
    ec()
    pyautogui.click(900, 260)
    time.sleep(1)
    pyautogui.click(900, 260)
    pyautogui.click(960, 185)
    pyautogui.doubleClick()
    time.sleep(0.3)
    pyautogui.hotkey('ctrl', 'c')
    volta()

def pesquisa():
    if cont >= 2:
        pyautogui.click(296, 100)
    else:
        pyautogui.click(296, 140)
    time.sleep(0.3)
    pyautogui.hotkey('ctrl', 'backspace')
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.3)
    pyautogui.write('3')
    time.sleep(5)
    pyautogui.click(296, 180)

def valor_SI():
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'f')
    pyautogui.write('valor atual')
    pyautogui.click(200, 410)
    time.sleep(0.5)
    pyautogui.doubleClick()
    pyautogui.hotkey('ctrl', 'c')

def valor_XLSX():
    ec()
    pyautogui.press('right')
    pyautogui.press('right')
    pyautogui.click(960, 185)
    pyautogui.hotkey('ctrl', 'v')
    volta()

def min_SI():
    time.sleep(1)
    site()
    pyautogui.hotkey('ctrl', 'f')
    pyautogui.write('min. 52 semanas')
    pyautogui.click(200, 500)
    time.sleep(0.5)
    pyautogui.doubleClick()
    pyautogui.hotkey('ctrl', 'c')

def min_XLSX():
    ec()
    pyautogui.press('right')
    pyautogui.click(960, 185)
    pyautogui.hotkey('ctrl', 'v')
    volta()

def max_SI():
    site()
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'f')
    pyautogui.write('max. 52 semanas')
    pyautogui.click(490, 500)
    time.sleep(0.5)
    pyautogui.doubleClick()
    pyautogui.hotkey('ctrl', 'c')

def max_XLSX():
    ec()
    pyautogui.press('right')
    time.sleep(0.3)
    pyautogui.click(960, 185)
    time.sleep(0.3)
    pyautogui.hotkey('ctrl', 'v')
    volta()

def tag_a_SI():
    site()
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'f')
    pyautogui.write('tag along')
    pyautogui.click(425, 420)
    time.sleep(0.5)
    pyautogui.doubleClick()
    pyautogui.hotkey('ctrl', 'c')

def tag_a_XLSX():
    ec()
    pyautogui.press('right')
    pyautogui.press('right')
    pyautogui.click(960, 185)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.write('%')
    volta()

def PL_SI():
    site()
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'f')
    pyautogui.write('p/l')
    pyautogui.click(270, 420)
    time.sleep(0.5)
    pyautogui.doubleClick()
    pyautogui.hotkey('ctrl', 'c')

def PL_XLSX():
    ec()
    r()
    pyautogui.hotkey('ctrl', 'v')
    volta()

def DY_SI():
    time.sleep(1)
    pyautogui.click(80, 425)
    time.sleep(0.5)
    pyautogui.doubleClick()
    pyautogui.hotkey('ctrl', 'c')

def DY_XLSX():
    ec()
    pyautogui.press('right')
    r()
    pyautogui.hotkey('ctrl','v')
    pyautogui.press('%')
    volta()

def pvp_SI():
    site()
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'f')
    pyautogui.write('p/vp')
    pyautogui.click(100, 490)
    time.sleep(0.5)
    pyautogui.doubleClick()
    pyautogui.hotkey('ctrl', 'c')

def pvp_XLSX():
    ec()
    r()
    pyautogui.hotkey('ctrl','v')
    volta()
    site()

def mover():
    ec()
    pyautogui.hotkey('ctrl', 'left')
    pyautogui.hotkey('ctrl', 'left')
    pyautogui.hotkey('ctrl', 'left')
    pyautogui.hotkey('ctrl', 'left')
    
    pyautogui.click(890, 680)
    pyautogui.press('down')

def programa():
    cod_acao()
    time.sleep(1)
    pesquisa()
    time.sleep(1)
    valor_SI()
    time.sleep(1)
    valor_XLSX()
    time.sleep(1)
    min_SI()
    time.sleep(1)
    min_XLSX()
    time.sleep(1)
    max_SI()
    time.sleep(1)
    max_XLSX()
    time.sleep(1)
    tag_a_SI()
    time.sleep(1)
    tag_a_XLSX()
    time.sleep(1)
    PL_SI()
    time.sleep(1)
    PL_XLSX()
    time.sleep(1)
    DY_SI()
    time.sleep(1)
    DY_XLSX()
    time.sleep(1)
    pvp_SI()
    time.sleep(1)
    pvp_XLSX()
    time.sleep(1)
    mover()
    time.sleep(10)

pyautogui.alert('Status Invest na esquerda e o Excel na direita', 'Alerta!', button='Ok')
time.sleep(15)

cont = 0

while True:
    cont+=1
    programa()
    time.sleep(7)