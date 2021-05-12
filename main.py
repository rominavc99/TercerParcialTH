import speech_recognition as sr
import time
import webbrowser
import playsound
import os
import random
from gtts import gTTS
from time import ctime

def alexa_speak(audio_string):
    tts = gTTS(text=audio_string, lang='es')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


def main():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)

        alexa_speak("Comienza a dictar")

        audio = r.listen(source)

        alexa_speak("Analizando .... ")


        # reconocer audio

        try:
            result = r.recognize_google(audio)
            alexa_speak("Tu dijiste \n" + r.recognize_google(audio))
            alexa_speak("Dictatdo guardado correctamente \n ")


        except Exception as e:
            print("Error :  " + str(e))


        # escribir texto
        with open("recorded.txt", "w") as f:
            f.write(result)

            


if __name__ == "__main__":
    main()