# News app
import requests
import json

query = input("Enter your search query: ")
url = f"https://newsapi.org/v2/everything?q={query}&from=2025-11-12&sortBy=publishedAt&apiKey=d8e34f4273d44d518986d0fa26f039a1"
r = requests.get(url)
print(r.text)
news_data = json.loads(r.text)
print(news_data, type(news_data))

for article in news_data["articles"]:
    print(article["title"])
    # print(article["url"])
    print(article["description"])
    # print(article["content"])
    print("---------------------------------------------------\n\n")
