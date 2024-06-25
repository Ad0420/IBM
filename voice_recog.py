import requests
from playsound import playsound
import sounddevice as sd
import numpy as np
from gtts import gTTS
import os
import soundfile as sf
import speech_recognition as sr


# Initialize the speech recognition
recognizer = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("User: " + text)
        print("RED")
        return text
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Error {0}".format(e))
    return ""


def main():
    while True:
        user_input = listen()
        if "exit" in user_input:
            print("Exiting...")
            break


if __name__ == "__main__":
    main()