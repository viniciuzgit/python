import pyautogui
import time
import clipboard

comentario = input("Comentário para ser escrito: ")
time.sleep(7)

def comentar_foto():
    clipboard.copy(comentario)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.click()

# Contador Simples

def atividade():
    cont = 0
    if True:
        cont +=1
        while True:
            if cont < 7:
                print(cont)
                cont+=1
                time.sleep(0.5)
                comentar_foto()
            else:
                time.sleep(30)
                atividade()



# ESTE CÓDIGO ESTÁ COM PROBLEMAS