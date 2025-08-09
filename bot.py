"""
Source File: bot.py
Author: Noah Boggess
Purpose: Holds all of the responses that the bot possesses. (The main hub for the bot)
Created 8/6/2025
Last Modified 8/8/2025
"""

import webbrowser
import subprocess
import sys
import os
from settings import SettingsManager
from games import Games
from utilities import Utilities
from botrpg import RPGGame
from constants import YOUTUBE_URL
from news import NewsFetcher
"""
Class Bot

Purposes:   Communicates with settings, games, utilities, and other files.
            Holds all responses the user can say and directs the user to the correct file.
"""
class Bot:
    def __init__(self, speech_engine):
        self.speech = speech_engine
        self.settings = SettingsManager(speech_engine)
        self.games = Games(speech_engine)
        self.utils = Utilities(speech_engine)
        self.botrpg = RPGGame(speech_engine)
        self.news_fetcher = NewsFetcher("96b2e9ae3caf493fa592edfc9c28b0f5")  

        
        self.command_map = {
            "hello": self.say_hello,
            "open youtube": self.open_youtube,
            "open steam": self.open_steam,
            "open notepad": self.open_notepad,
            "shut down": self.shut_down,
            "open settings": self.open_settings,
            "tell me a fun fact": self.utils.GetFunFact,
            "tell me a joke": self.utils.GetJoke,
            "define a word": self.utils.DefineWord,
            "tell me the time": self.utils.TellTime,
            "flip a coin": self.games.FlipCoin,
            "play rock-paper-scissors": self.games.RockPaperScissors,
            "play rock paper scissors": self.games.RockPaperScissors,
            "what is the weather": self.utils.GetWeather,
            "is this word a palindrome": self.utils.IsPalindrome,
            "close notepad": self.close_notepad,
            "close steam": self.close_steam,
            "lowe's steam": self.close_steam,
            "lowe's notepad": self.close_notepad,
            "read the news": self.read_news  
        }
        """
        Response funtions. 
        These are the function I had in this file before i made the dictionary.
        Easily moveable but a later problem. 
        """

    # Executes an action based on the given command.

    def respond(self, command):
        action = self.command_map.get(command)
        if action:
            action()
        else:
            self.speech.speak("I don't know how to respond to that yet.")

    # Says "Hey there"

    def say_hello(self):
        self.speech.speak("Hey there!")

    # Opens youtube from the browser

    def open_youtube(self):
        self.speech.speak("Opening YouTube.")
        webbrowser.open(YOUTUBE_URL)

    # Opens steam from the files using utilites.py's executable finder.

    def open_steam(self):
        path = self.utils.find_executable("Steam\\steam.exe")
        if path:
            self.speech.speak("Opening Steam.")
            subprocess.Popen(path)
        else:
            self.speech.speak("Steam executable not found.")

    # Opens notepad from the files using utilites.py's executable finder.

    def open_notepad(self):
        path = self.utils.find_executable("Notepad++\\notepad++.exe")
        if path:
            self.speech.speak("Opening Notepad.")
            subprocess.Popen(path)
        else:
            self.speech.speak("Notepad++ executable not found.")

    # Shuts the bot down. 

    def shut_down(self):
        self.speech.speak("Shutting down. Talk to you later!")
        sys.exit()

    # Opens the settings menu, directing it to settings.py

    def open_settings(self):
        self.speech.speak("Opening settings.")
        self.settings.settings_menu()

    # Closes the notepad app. 

    def close_notepad(self):
        try:
            subprocess.run(["taskkill", "/f", "/im", "notepad++.exe"], check=True) # taskkill is Windows kill but i can make it dynamic to linex and mac too.
            self.speech.speak("Notepad++ has been closed.")
        except subprocess.CalledProcessError:
            self.speech.speak("Couldn't close Notepad++. It may not be running.")

    # Closes the steam app

    def close_steam(self):
        try:
            subprocess.run(["taskkill", "/f", "/im", "steam.exe"], check=True) 
            self.speech.speak("Steam has been closed.")
        except subprocess.CalledProcessError:
            self.speech.speak("Couldn't close Steam. It may not be running.")

    # Reads the latest news.
    def read_news(self):
        headlines = self.news_fetcher.get_headlines()
        self.speech.speak("Here are today's top headlines.")
        for headline in headlines:
            self.speech.speak(headline)
