import winsound

# Freqência
f = 2500
# Duração
d = 1000 #1000ms = 1s
winsound.Beep(f, d)
error_sound = winsound.MessageBeep()
