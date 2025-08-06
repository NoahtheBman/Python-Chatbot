import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from bot import Bot
from speech import SpeechEngine

def main():
    # Initialize speech engine with default settings
    speech = SpeechEngine(rate=150, volume=1.0, voice_index=0)

    # Create your bot and pass in the speech engine
    assistant = Bot(speech)

    # Start the bot loop
    speech.speak("Hello! I'm ready to help.")
    while True:
        command = speech.listen()
        if command:
            assistant.respond(command)

if __name__ == "__main__":
    main()
