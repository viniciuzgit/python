from tkinter import Label, Tk
import time

app_window = Tk()
app_window.title("Relógio Digital")
app_window.geometry("420x158")
app_window.resizable(1, 1)

text_font = ("Boulder", 68, "bold")
background = "yellow"
foreground = "black"
border_width = 25

label = Label(app_window, font=text_font, bg=background, fg=foreground,
              border=border_width)
label.grid(row=0, colum=1)

def digital_clock():
    time_live = time.strftime("%H:%M:%S")
    label.config(text=time_live)
    label.after(200, digital_clock)


digital_clock()
