class RPGGame:
    def __init__(self, speech):
        self.speech = speech

    def start(self):
        self.speech.say("Welcome to the RPG adventure!")
        self.speech.say("You wake up in a dark forest. Do you go left or right?")
        choice = self.speech.listen().lower()

        if "left" in choice:
            self.speech.say("You encounter a friendly elf who gives you a potion.")
        elif "right" in choice:
            self.speech.say("A wild boar charges at you! You barely escape.")
        else:
            self.speech.say("You stand still, unsure what to do. The forest grows darker...")