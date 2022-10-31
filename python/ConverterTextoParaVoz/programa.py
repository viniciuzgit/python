import pyttsx3

def convertTexto(texto):
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()
    
convertTexto("QUALQUER COISA")

