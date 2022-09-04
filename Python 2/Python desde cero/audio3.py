def main():
 
    import speech_recognition as sr
    
    r = sr.Recognizer()
 
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
 
        print("Porfavor diga algo:")
 
        audio = r.listen(source)
 
        print("Procesando.... ")
 
 
        # recognize speech using google
 
        try:
            print("Tu dijiste: \n" + r.recognize_google(audio, language ="es_ES"))
            print("Audio guardado completado \n ")
 
 
        except Exception as e:
            print("Error :  " + str(e))
 
 
 
 
        # write audio
        with open("recorded.wav", "wb") as f:
            f.write(audio.get_wav_data())
 
 
if __name__ == "__main__":
    main()