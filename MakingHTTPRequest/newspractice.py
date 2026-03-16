import requests

url = "https://news.ycombinator.com/"
url2 = " https://hacker-news.firebaseio.com/v0/maxitem.json"

res = requests.get(url2, headers={"Accept" : "application/json"})

print(res.json())