from tkinter import *
import random
root = Tk()
root.title("Jogo de Cores")
root.geometry('600x300')
root.resizable(False,False)
colors = ["Red", "Orange", "White", "Black",
          "Green", "Blue", "Brown", "Purple",
          "Cyan", "Yellow", "Pink", "Magenta"]
timer = 60
pontos = 0
displayed_word_color = ''
def startGame():
    global displayed_word_color
    if(timer == 60):
        startCountDown()
        displayed_word_color = random.choice(colors).lower()
        display_words.config(text=random.choice(colors),
                             fg=displayed_word_color)
        entry_cor.bind('<Return>', displayNextWord)
def resetGame():
    global timer, score, displayed_word_color
    timer = 60
    pontos = 0
    displayed_word_color = ''
    game_score.config(text = "Pontos : " + str(pontos))
    display_words.config(text = '')
    time_left.config(text="Fim do Jogo em : -")
    entry_cor.delete(0, END)
def startCountDown():
    global timer
    if(timer >= 0):
        time_left.config(text = "Fim do Jogo em : " + str(timer) + "s")
        timer -= 1
        time_left.after(1000,startCountDown)
        if (timer == -1):
            time_left.config(text="Fim do Jogo!!!")
def displayNextWord(event):
    global displayed_word_color
    global pontos
    if(timer > 0):
        if(displayed_word_color == entry_cor.get().lower()):
            pontos += 1
            game_score.config(text = "Pontos : " + str(pontos))
        entry_cor.delete(0, END)
        displayed_word_color = random.choice(colors).lower()
        display_words.config(text = random.choice(colors), fg = displayed_word_color)
#
# Descrição
game_description = Label(text ="Digite a cor das palavras exibidas abaixo.\n"
                               "E lembre-se de não inserir o próprio texto da palavra",
                         font=('Helvetica',12), fg= "grey")
game_description.place(relx=0.15,rely=0.05)
#Pontos
game_score = Label(text = "Pontos : " + str(pontos),font=('Helvetica',16), fg = "green")
game_score.place(relx=0.4,rely=0.2)
#Cores
display_words = Label(font =('Helvetica',20), pady = 10)
display_words.place(relx=0.35, rely=0.3)
# Fim do Jogo
time_left = Label(text = "Fim do Jogo em : -", font =('Helvetica',14), fg = "orange")
time_left.place(relx=0.2, rely=0.5)
# Entrada
nomecor = StringVar()
entry_cor = Entry(textvariable=nomecor)
entry_cor.place(relx=0.2, rely=0.6,relwidth=0.45)
# Butão
# command = resetGame
reset_button = Button( text = "Reiniciar", fg = "black",
                       bg = "light blue",command=resetGame)
reset_button.place(relx=0.05, rely=0.9,relwidth=0.45)
star_button = Button( text = "Começar", fg = "black",
                      bg = "pink",command=startGame)
star_button.place(relx=0.5, rely=0.9,relwidth=0.45)
root.mainloop()