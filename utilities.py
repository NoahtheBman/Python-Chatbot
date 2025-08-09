"""
Source File: utilities.py
Author: Noah Boggess
Purpose: Holds all of the rather useful responses' functions.  (Everythings thats not a game or setting...) 
Created 8/6/2025
Last Modified 8/8/2025
"""

import requests
from bs4 import BeautifulSoup
from datetime import datetime
import os
from constants import DEFAULT_DRIVES, DEFAULT_PROGRAM_FOLDERS
from collections import deque

"""
Utilities

Purpose:  Holds response functions that relate to utility.  
"""

class Utilities:
    def __init__(self, speech):
        self.speech = speech

    # Grabs the time

    def TellTime(self):
        now = datetime.now()
        current_time = now.strftime("%I:%M %p")
        self.speech.speak(f"The current time is {current_time}")

    # Takes in the word the user wants to define and webscrapes the dictionary api for a definition.

    def DefineWord(self):
        self.speech.speak("What word would you like me to define?")
        word = self.speech.listen()
        if not word:
            self.speech.speak("I didn't catch the word. Try again later.")
            return
        url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
        try:
            response = requests.get(url)
            data = response.json()
            if isinstance(data, list):
                definition = data[0]["meanings"][0]["definitions"][0]["definition"]
                self.speech.speak(f"The definition of {word} is: {definition}")
            else:
                self.speech.speak(f"Sorry, I couldn't find a definition for {word}.")
        except Exception as e:
            self.speech.speak("Something went wrong while fetching the definition.")
            print(f"Error: {e}")

    # Grabs a random joke from jokeapi. 

    def GetJoke(self):
        url = "https://v2.jokeapi.dev/joke/Any?type=single"
        response = requests.get(url)
        if response.ok:
            joke = response.json().get("joke")
            self.speech.speak(joke)
        else:
            self.speech.speak("Couldn't fetch a joke right now.")

    # Grabs a fun fact from uselessfacts website. 

    def GetFunFact(self):
        url = "https://uselessfacts.jsph.pl/random.json?language=en"
        try:
            response = requests.get(url)
            fact = response.json()['text']
            self.speech.speak("Here's a fun fact.")
            self.speech.speak(fact)
        except Exception as e:
            self.speech.speak("Sorry, I couldn't fetch a fun fact right now.")
            print(f"Error: {e}")

    # A helper function that instantiates BS and grabs the HTML components.  

    def parse_weather_page(self, html):
        soup = BeautifulSoup(html, "html.parser")
        try:
            location = soup.find("h2", class_="panel-title").text.strip()
            temp = soup.find("p", class_="myforecast-current-lrg").text.strip()
            condition = soup.find("p", class_="myforecast-current").text.strip()
            today = soup.find("div", class_="tombstone-container")
            period = today.find("p", class_="period-name").text.strip()
            short_desc = today.find("p", class_="short-desc").text.strip()
            temp_forecast = today.find("p", class_="temp").text.strip()
            return location, temp, condition, period, short_desc, temp_forecast
        except AttributeError:
            return None
        
    # Uses weather parser to read the weather. 

    def GetWeather(self):
        url = "https://forecast.weather.gov/MapClick.php?textField1=35.0169&textField2=-86.3598"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)
        parsed = self.parse_weather_page(response.content)
        
        if parsed:
            location, temp, condition, period, short_desc, temp_forecast = parsed
            self.speech.speak(f"{location}")
            self.speech.speak(f"Current Temp: {temp}")
            self.speech.speak(f"Condition: {condition}")
            self.speech.speak(f"{period}: {short_desc}, {temp_forecast}")
        else:
            self.speech.speak("Sorry, I couldn't parse the weather data.")


        # Just states weather a word is a palindrome or not. Kinda random but yea. 

    def IsPalindrome(self):
        self.speech.speak("What word would you like to test?")
        s = self.speech.listen()
        stack = deque()

        mid = len(s) // 2

        for i in range(mid):
            stack.append(s[i])

        if len(s) % 2 != 0:
            mid += 1

        for i in range(mid, len(s)):
            if s[i] != stack.pop():
                self.speech.speak("The word is not a palindrome.")
                return

        
    # This is a super genius way of allowing the steam and notebook opener functions to be more dynamic for the user.  
    
    def find_executable(self, executable_name):
        for drive in DEFAULT_DRIVES:
            for folder in DEFAULT_PROGRAM_FOLDERS:
                path = os.path.join(drive + "\\", folder, executable_name)
                if os.path.exists(path):
                    return path
        return None



        
        
