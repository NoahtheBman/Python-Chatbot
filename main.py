"""
Source File: main.py
Author: Noah Boggess
Purpose: Sets settings for the bot and listens in a loop for as long as the bot runs. 
Created 8/6/2025
Last Modified 8/8/2025
"""
import sys
import os
import argparse

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from bot import Bot
from speech import SpeechEngine
# Sets settings and generates the speech engine.  
def main():
    parser = argparse.ArgumentParser(description="Run the speech-enabled bot assistant.")
    parser.add_argument("--rate", type=int, default=150, help="Speech rate (default: 150)")
    parser.add_argument("--volume", type=float, default=1.0, help="Speech volume between 0.0 and 1.0 (default: 1.0)")
    parser.add_argument("--voice_index", type=int, default=0, help="Voice index for the speech engine (default: 0)")
    args = parser.parse_args()

    # Initialize speech engine with CLI or default settings
    speech = SpeechEngine(rate=args.rate, volume=args.volume, voice_index=args.voice_index)

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
