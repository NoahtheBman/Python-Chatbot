"""
Source File: games.py
Author: Noah Boggess
Purpose: Holds all of the games related functions that the bot possesses. 
Created 8/6/2025
Last Modified 8/8/2025
"""
import random

class Games:
    def __init__(self, speech):
        # Reusing the shared speech engine instance passed from Bot.
        # This avoids creating multiple pyttsx3 engine instances.
        self.speech = speech

    # Flips a coin heads or tails.

    def FlipCoin(self):
        result = random.choice(["heads", "tails"])
        self.speech.speak(f"The coin landed on {result}")
        
    # Plays rock paper scissors with the user. 

    def RockPaperScissors(self):
        self.speech.speak("What is your choice?")
        user_choice = self.speech.listen()
        options = ["rock", "paper", "scissors"]
        bot_choice = random.choice(options)
        self.speech.speak(f"My choice is {bot_choice}.")

        winning_combos = {
            "rock": "scissors",
            "paper": "rock",
            "scissors": "paper"
        }

        if user_choice == bot_choice:
            self.speech.speak("It's a tie!")
        elif winning_combos.get(user_choice) == bot_choice:
            self.speech.speak("You win!")
        else:
            self.speech.speak("I win!")
