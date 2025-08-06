class SettingsManager:
    def __init__(self, speech_engine):
        self.speech = speech_engine

    def change_voice(self):
        self.speech.speak("Would you like me to be a girl or a boy?")
        command = self.speech.listen()
        if "boy" in command:
            if self.speech.voice_index == 0:
                self.speech.speak("I am already a boy.")
            else:
                self.speech.voice_index = 0
                self.speech.speak("Changing to boy voice.")
        elif "girl" in command:
            if self.speech.voice_index == 1:
                self.speech.speak("I am already a girl.")
            else:
                self.speech.voice_index = 1
                self.speech.speak("Changing to girl voice.")
        else:
            self.speech.speak("I don't have that option.")
            self.change_voice()

    def change_volume(self):
        self.speech.speak("Would you like to make my voice quieter or louder?")
        command = self.speech.listen()
        if "quieter" in command:
            self.speech.volume = max(0.0, self.speech.volume - 0.25)
            self.speech.speak("Turning down sound.")
        elif "louder" in command:
            self.speech.volume = min(1.0, self.speech.volume + 0.25)
            self.speech.speak("Turning up sound.")
        elif "what is your volume" in command:
            self.speech.speak(f"My volume is at {self.speech.volume}")
            self.change_volume()
        else:
            self.speech.speak("Exiting settings.")

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