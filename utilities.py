import requests
from bs4 import BeautifulSoup
from datetime import datetime

class Utilities:
    def __init__(self, speech):
        self.speech = speech

    def TellTime(self):
        now = datetime.now()
        current_time = now.strftime("%I:%M %p")
        self.speech.speak(f"The current time is {current_time}")

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

    def GetJoke(self):
        url = "https://v2.jokeapi.dev/joke/Any?type=single"
        response = requests.get(url)
        if response.ok:
            joke = response.json().get("joke")
            self.speech.speak(joke)
        else:
            self.speech.speak("Couldn't fetch a joke right now.")

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

    def GetWeather(self):
        url = "https://forecast.weather.gov/MapClick.php?textField1=35.0169&textField2=-86.3598"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")
        location = soup.find("h2", class_="panel-title").text.strip()
        temp = soup.find("p", class_="myforecast-current-lrg").text.strip()
        condition = soup.find("p", class_="myforecast-current").text.strip()
        today = soup.find("div", class_="tombstone-container")
        period = today.find("p", class_="period-name").text.strip()
        short_desc = today.find("p", class_="short-desc").text.strip()
        temp_forecast = today.find("p", class_="temp").text.strip()
        self.speech.speak(f"{location}")
        self.speech.speak(f"Current Temp: {temp}")
        self.speech.speak(f"Condition: {condition}")
        self.speech.speak(f"{period}: {short_desc}, {temp_forecast}")