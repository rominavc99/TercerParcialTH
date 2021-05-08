import speech_recognition as sr 
r = sr.Recognizer()

with sr.Microphone() as recurso:
    print("dime algo")
    audio=r.listen(recurso)
    try:
        texto = r.recognize_google(audio, language='es-ES')
        print("Este es el audio capturado: {} ".format(texto))
        with open("audio.wav", "wb") as fichero:
            fichero.write(audio.get_wav_data())
    except:
        print("No entendi, puedes repetir?")