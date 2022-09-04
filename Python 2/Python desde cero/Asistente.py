import pyttsx3
import time

m = True


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
# Control the rate. Higher rate = more speed
engine.setProperty("rate", 150)
text = "Porfavor ingrese su nombre"
engine.say(text)
engine.runAndWait()

while (m == True):

    n = input("Ingrese su nombre: ")


    another_text = "Su nombre es"
    engine.say(another_text + n)
    engine.runAndWait()

    another_text = "Es correcto ese nombre, confirme porfavor"
    engine.say(another_text)
    engine.runAndWait()

    x = True

    while (x == True):
        respuesta = input("si o no: ").lower()

        if (respuesta == "si"):

            another_text = "Gracias por la información, que tenga un buen día"
            engine.say(another_text)
            engine.runAndWait()
            m = False
            x = False
        elif(respuesta == "no"):
            another_text = "Entonces ingrese su nombre nuevamente "
            engine.say(another_text)
            engine.runAndWait()
            x = False
        else:
            another_text = "No se ha ingresado una respuesta valida, intente denuevo"
            engine.say(another_text)
            engine.runAndWait()



