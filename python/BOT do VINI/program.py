from selenium import webdriver
import os
import time
import webbrowser
import pyautogui
import winsound
import pyttsx3

RED = "\033[1;31m"
BOLD = "\033[;1m"

def convertTexto(texto):
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()

while True:
    print(RED + "\nMYBOT" + BOLD + " ...")
    escolha = int(input('\nDigite o número de sua opção\n0. PARAR PROGRAMA\n1. Fazer uma '
                        'pesquisa\n2. Abrir um APP ou pasta\n3. Abrir Instagram\n4. Novo '
                        'Documento Word\n5. Definir horário para entar na aula '
                        'online\n6. Estatística\n-> '))
                        # Criar um novo arquivo HTML
    if escolha == 0:
        break
    else:
        pass
    if escolha == 1:
        pesquisa = input('Digite o que quer pesquisar:\n')
        navegador = webdriver.Chrome(
            executable_path=r"C:\Users\vbernardino-ieg\Downloads\chromedriver_win32"
                            r"\chromedriver.exe")
        navegador.get("https://www.google.com.br")
        time.sleep(0.8)
        pyautogui.write(pesquisa)
        pyautogui.press('enter')
        time.sleep(2)
        convertTexto("Foram achados esses resultados")
    if escolha == 2:
        app = input('Digite qual app/pasta você quer acessar:\n')
        pyautogui.hotkey('win', 's')
        time.sleep(0.5)
        pyautogui.write(app)
        time.sleep(0.5)
        pyautogui.press('enter')
        time.sleep(1)
        convertTexto("Foram achados esses resultados")
    if escolha == 3:
        usuario = input('Usuário Insta: ')
        senha = input('Senha Insta: ')
        navegador = webdriver.Chrome(
            executable_path=r"C:\Users\vbernardino-ieg\Downloads\chromedriver_win32"
                            r"\chromedriver.exe")
        navegador.get("https://www.instagram.com/")
        time.sleep(2)
        navegador.find_element_by_xpath('//*[@id="loginForm"]/div/div['
                                        '1]/div/label/input').send_keys(usuario)
        navegador.find_element_by_xpath('//*[@id="loginForm"]/div/div['
                                        '2]/div/label/input').send_keys(senha)
        navegador.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]').click()
        time.sleep(3)
        navegador.find_element_by_xpath('//*['
                                        '@id="react-root"]/section/main/div/div/div/div'
                                        '/button').click()
        time.sleep(2)
        navegador.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button['
                                        '2]').click()
        time.sleep(2)
        navegador.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button['
                                        '2]').click()
    if escolha == 4:
        print("Vou abrir uma arquivo word pra você, mas primeiro preciso saber se você "
              "deseja renomear o arquivo")
        opcao_renomear = input(" Renomear sim ou não?\n-> ")
        opcao_renomear = opcao_renomear.lower()
        if opcao_renomear == 'sim':
            archivewordname = input('  Nome do arquivo -> ')
            word = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word"
            os.startfile(word)
            time.sleep(1.5)
            pyautogui.hotkey('win', 'up')
            pyautogui.click(200, 200)
            time.sleep(0.5)
            pyautogui.click(30, 40)
            time.sleep(0.5)
            pyautogui.click(35, 300)
            time.sleep(0.5)
            pyautogui.click(230, 240)
            time.sleep(1)
            pyautogui.click(700, 350)
            time.sleep(1)
            pyautogui.write(archivewordname)
            time.sleep(1)
            pyautogui.click(1300, 170)
        else:
            word = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word"
            os.startfile(word)
            time.sleep(1.5)
            pyautogui.hotkey('win', 'up')
            pyautogui.click(200, 200)
    if escolha == 5:
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
    if escolha == 6:
        cdados = []
        print('Dados Estatísticos')
        print('Montar o conjunto de dados: ')
        while True:
            ins = float(input('Inserir número no conjunto de dados: '))
            print('OBS: 0 para parar\n')
            if ins == 0:
                print(cdados)
                break
            else:
                cdados.append(ins)
        time.sleep(1)
        print('\nConjunto de dados organizado:')
        ordenar = sorted(cdados)
        print(ordenar[::1])
        time.sleep(1)
        a = int(input("\nO que quer fazer?\n1. Soma dos números no conj de dados\n2. Média\n3. Moda\n4. Desvio Médio\n5. Variância\n6. Desvio Padrão\n-> "))
        if a == 1:
            print(f'SOMA: {sum(cdados)}')            
