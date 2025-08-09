"""
Source File: bot.py
Author: Noah Boggess
Purpose: Grabs the latest news. (Currently. Made this a new file so i could just use this for anything with an API Key)
Created 8/8/2025
Last Modified 8/8/2025
"""

import requests

"""
NewsFetcher

Purpose: Fetches the news with the API key. 

"""
class NewsFetcher:
    def __init__(self, api_key):
        self.api_key = api_key

    # Fetches the news and reads it.  

    def get_headlines(self, country="us", category="general", limit=5):
        url = "https://newsapi.org/v2/top-headlines"
        params = {
            "country": country,
            "category": category,
            "apiKey": self.api_key,
            "pageSize": limit
        }
        response = requests.get(url, params=params)
        if response.ok:
            articles = response.json().get("articles", [])
            return [article["title"] for article in articles]
        else:
            return ["Sorry, I couldn't fetch the news."]
