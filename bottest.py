"""
Source File: bottest.py
Author: Noah Boggess
Purpose: Allows the user to test if the bot actually works without having to speak to it. 
(Right now everything is hardcoded but can/will change)
Created 8/8/2025
Last Modified 8/8/2025
"""

import unittest
from unittest.mock import MagicMock, patch
from bot import Bot
from speech import SpeechEngine

"""
TestBot

Purpose: Just a way to tell if the bot gives the expected outcome quickly. Pretty cool. 
I don't have all the functions in here but if i need to debug something i can easily add it.  

"""

class TestBot(unittest.TestCase):

    def setUp(self):
        # Create a mock speech engine
        self.mock_speech = MagicMock()
        self.bot = Bot(self.mock_speech)

    # Tests the hello command

    def test_hello_command(self):
        self.bot.respond("hello")
        self.mock_speech.speak.assert_called_with("Hey there!")

    # Tests the open youtube command

    def test_open_youtube(self):
        with patch("webbrowser.open") as mock_open:
            self.bot.respond("open youtube")
            self.mock_speech.speak.assert_called_with("Opening YouTube.")
            mock_open.assert_called_with("https://youtube.com")

    # Tests the open steam command

    def test_open_steam(self):
        with patch("subprocess.Popen") as mock_popen:
            self.bot.respond("open steam")
            self.mock_speech.speak.assert_called_with("Opening Steam.")
            mock_popen.assert_called()

    # Tests the instance to where the user says something the bot doesnt know

    def test_unknown_command(self):
        self.bot.respond("sup")
        self.mock_speech.speak.assert_called_with("I don't know how to respond to that yet.")

    # Test fun fact command

    def test_fun_fact(self):
        with patch("utilities.requests.get") as mock_get:
            mock_get.return_value.ok = True
            mock_get.return_value.json.return_value = {"text": "Bananas are berries."}
            self.bot.respond("tell me a fun fact")
            self.mock_speech.speak.assert_any_call("Here's a fun fact.")
            self.mock_speech.speak.assert_any_call("Bananas are berries.")

    # Tests the rock paper scissors command. 

    def test_rps_user_wins(self):
        self.mock_speech.listen.return_value = "paper"
        with patch("random.choice", return_value="rock"):
            self.bot.respond("play rock paper scissors")
            self.mock_speech.speak.assert_any_call("You win!")

if __name__ == "__main__":
    unittest.main()
