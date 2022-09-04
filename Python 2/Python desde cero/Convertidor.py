import speech_recognition as sr

r = sr.Recognizer() 

with sr.Microphone() as source:
    print('Di algo : ')
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print('Tu dijiste: {}'.format(text))
    except:
        print('Perdon, pero no te escuche')
