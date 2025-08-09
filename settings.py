"""
Source File: settings.py
Author: Noah Boggess
Purpose: Holds the settings resonses and the settings menu. (Will be updated to where its not shockingly annoying)
Created 8/6/2025
Last Modified 8/8/2025
"""
import json
import os

"""
Settings Manager

Purpose: Manages everything related to settings. 
"""

class SettingsManager:
    CONFIG_FILE = "settings.json"

    def __init__(self, speech_engine):
        self.speech = speech_engine
        self.settings = self.load_settings()
        self.apply_settings()

    # Loads the saved settings from json file. 

    def load_settings(self):
        if os.path.exists(self.CONFIG_FILE):
            try:
                with open(self.CONFIG_FILE, "r") as f:
                    return json.load(f)
            except json.JSONDecodeError:
                self.speech.speak("Settings file is corrupted. Loading defaults.")
                return {"voice_index": 0, "volume": 1.0}
        return {"voice_index": 0, "volume": 1.0}

    # Saves settings to json file. 

    def save_settings(self):
        with open(self.CONFIG_FILE, "w") as f:
            json.dump(self.settings, f)

    # Applies the lates bot settings. 

    def apply_settings(self):
        self.speech.voice_index = self.settings.get("voice_index", 0)
        self.speech.volume = self.settings.get("volume", 1.0)

    # Changes the voice of the bot.

    def change_voice(self):
        self.speech.speak("Would you like me to be a girl or a boy?")
        command = self.speech.listen()
        if "boy" in command:
            if self.speech.voice_index == 0:
                self.speech.speak("I am already a boy.")
            else:
                self.speech.voice_index = 0
                self.settings["voice_index"] = 0
                self.save_settings()
                self.speech.speak("Changing to boy voice.")
        elif "girl" in command:
            if self.speech.voice_index == 1:
                self.speech.speak("I am already a girl.")
            else:
                self.speech.voice_index = 1
                self.settings["voice_index"] = 1
                self.save_settings()
                self.speech.speak("Changing to girl voice.")
        else:
            self.speech.speak("I don't have that option.")
            self.change_voice()

    # Changes the volume of the bot. 

    def change_volume(self):
        self.speech.speak("Would you like to make my voice quieter or louder?")
        command = self.speech.listen()
        if "quieter" in command:
            self.speech.volume = max(0.0, self.speech.volume - 0.25)
            self.settings["volume"] = self.speech.volume
            self.save_settings()
            self.speech.speak("Turning down sound.")
        elif "louder" in command:
            self.speech.volume = min(1.0, self.speech.volume + 0.25)
            self.settings["volume"] = self.speech.volume
            self.save_settings()
            self.speech.speak("Turning up sound.")
        elif "what is your volume" in command:
            self.speech.speak(f"My volume is at {self.speech.volume}")
            self.change_volume()
        else:
            self.speech.speak("Exiting settings.")

    # Settings menu. The hub of the settings. 
    
    def settings_menu(self):
        while True:
            self.speech.speak("What would you like to do?")
            command = self.speech.listen()
            if "change volume" in command:
                self.change_volume()
            elif "change voice" in command:
                self.change_voice()
            elif "exit" in command:
                self.speech.speak("Exiting settings.")
                break
            else:
                self.speech.speak("That's not an option.")
