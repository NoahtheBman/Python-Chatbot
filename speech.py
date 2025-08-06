import pyttsx3
import speech_recognition as sr

class SpeechEngine:
    def __init__(self, rate=150, volume=1.0, voice_index=0):
        self.rate = rate
        self.volume = volume
        self.voice_index = voice_index
        self.recognizer = sr.Recognizer()

    def speak(self, text):
        print(f"Speaking: {text}")
        engine = pyttsx3.init('sapi5')
        engine.setProperty('rate', self.rate)
        engine.setProperty('volume', self.volume)
        engine.setProperty('voice', engine.getProperty('voices')[self.voice_index].id)
        engine.say(text)
        engine.runAndWait()

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