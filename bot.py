import webbrowser
import subprocess
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from settings import SettingsManager
from games import Games
from utilities import Utilities
from botrpg import RPGGame



class Bot:
    def __init__(self, speech_engine):
        self.speech = speech_engine
        self.settings = SettingsManager(speech_engine)
        self.games = Games(speech_engine)
        self.utils = Utilities(speech_engine)
        self.botrpg = RPGGame(speech_engine)

    def respond(self, command):
        if "hello" in command:
            self.speech.speak("Hey there!")
        elif "open youtube" in command:
            self.speech.speak("Opening YouTube.")
            webbrowser.open("https://youtube.com")
        elif "open steam" in command:
            self.speech.speak("Opening Steam.")
            subprocess.Popen(r"C:\Program Files (x86)\Steam\steam.exe")
        elif "open notepad" in command:
            self.speech.speak("Opening Notepad.")
            subprocess.Popen(r"C:\Program Files\Notepad++\notepad++.exe")
        elif "shut down" in command:
            self.speech.speak("Shutting down. Talk to you later!")
            sys.exit()
        elif "open bot settings" in command:
            self.speech.speak("Opening settings.")
            self.settings.settings_menu()
        elif "tell me a fun fact" in command:
            self.utils.GetFunFact()
        elif "tell me a joke" in command: 
            self.utils.GetJoke()
        elif "define a word" in command: 
            self.utils.DefineWord()
        elif "tell me the time" in command:
            self.utils.TellTime()
        elif "flip a coin" in command:
            self.games.FlipCoin()
        elif "play rock-paper-scissors" in command or "play rock paper scissors" in command:
            self.games.RockPaperScissors()
        elif "what is the weather" in command:
            self.utils.GetWeather()
        else:
            self.speech.speak("I don't know how to respond to that yet.")
       