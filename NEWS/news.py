"""GET DAILY NEWS
use news api to get news .
fatch daily news.
"""


import requests
import json

query = input("What type of news you want to receive :: ") # get type of news from user as input 
r = requests.get(f'https://newsapi.org/v2/everything?q={query}&from=2024-06-10&sortBy=publishedAt&apiKey=d515bbdf565d440ea94376cc7f53bd95') # artical link from news api

news = json.loads(r.text)
# print(news , type(news))

for article in news["articles"]:
    print(f"\nTitle :: {article.get('title')}")
    print(f"Description :: {article.get('description')}")
    print(f"URL :: {article.get('url')}")
    print(f"Published at :: {article.get('publishedAt')}\n")
    print(" * "*50)
