import random

class Games:
    def __init__(self, speech):
        self.speech = speech

    def FlipCoin(self):
        result = random.choice(["heads", "tails"])
        self.speech.speak(f"The coin landed on {result}")

    def RockPaperScissors(self):
        self.speech.speak("What is your choice?")
        choice = self.speech.listen()
        options = ["rock", "paper", "scissors"]
        bot_choice = random.choice(options)
        self.speech.speak(f"My choice is {bot_choice}.")
        if choice == bot_choice:
            self.speech.speak("It's a tie!")
        elif (choice == "rock" and bot_choice == "scissors") or \
             (choice == "paper" and bot_choice == "rock") or \
             (choice == "scissors" and bot_choice == "paper"):
            self.speech.speak("You win!")
        else:
            self.speech.speak("I win!")