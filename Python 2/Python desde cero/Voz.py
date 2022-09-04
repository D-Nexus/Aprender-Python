import speech_recognition as sr

listener = sr.Recognizer()

with sr.Microphone() as micro:
    print("Escuchando...")
    sonido = listener.listen(micro)
    texto = listener.recognize_google(sonido, language ="es_ES")
    print(texto)