import pyttsx3
import speech_recognition as sr
import datetime
import pywhatkit
import os
import yfinance as yf
import pyjokes

#Escuchar nuestro microfono y devuelve el audio como texto para google

def transformar():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.8
        said = r.listen(source)
        try:
            print("Yo estoy escuchando")
            q = r.recognize_google(said, language="es")
            return q
        except sr.UnknownValueError:
            print("Lo lamento no entendi")
            return "Yo estoy esperando"
        except sr.RequestError:
            print("El servicio esta caido")
            return "Yo estoy esperando"
        except:
            return "Yo estoy esperando"

transformar()
