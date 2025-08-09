"""
Source File: speech.py
Author: Noah Boggess
Purpose: Holds the bot's speech abilities.  
Created 8/6/2025
Last Modified 8/8/2025
"""
import pyttsx3
import speech_recognition as sr

"""
SpeechEngine

Purpose:  Creates the speech engine instance so that the bot can talk. 
"""

class SpeechEngine:
    def __init__(self, rate=150, volume=1.0, voice_index=0):
        self.rate = rate
        self.volume = volume
        self.voice_index = voice_index
        self.recognizer = sr.Recognizer()

    # Sets the engine instance EVERY TIME it speaks. Otherwise it will speak once and never agian. Thanks pyttsx3.  

    def speak(self, text):
        print(f"Speaking: {text}")
        engine = pyttsx3.init('sapi5')
        engine.setProperty('rate', self.rate)
        engine.setProperty('volume', self.volume)
        engine.setProperty('voice', engine.getProperty('voices')[self.voice_index].id)
        engine.say(text)
        engine.runAndWait()

    # Listens for audio from the user and translates it to a string.  
    
    def listen(self):
        with sr.Microphone() as source:
            print("Listening...")
            audio = self.recognizer.listen(source)
        try:
            command = self.recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            self.speak("Sorry, I didn't catch that.")
            return ""
        except sr.RequestError:
            self.speak("Speech service is down.")
            return ""