import pyttsx3


engine = pyttsx3.init()
# Control the rate. Higher rate = more speed
engine.setProperty("rate", 150)
text = "Hola seba como te encuentras el dia de hoy"
engine.say(text)
"""
Esperando otro audio
"""
another_text = "Me preguntaba si queria jugar un juego"
engine.say(another_text)
engine.runAndWait()


