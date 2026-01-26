import requests



url = "http://www.google.com"
res = requests.get(url)

# print(f"Your request to {url} came back is with status code of {res.status_code}")

# url2 = "https://news.ycombinator.com/"

# res2 = requests.get(url2)

# print(res2.status_code)


url1 = "https://icanhazdadjoke.com/search"

# res1 = requests.get(url1, headers={"Accept" : "text/plain"})

# print(res1.text)


res1 = requests.get(url1,
                     headers={"Accept" : "application/json"},
                     params={
                         "term" : "cat","limit" : 1}
                     )

print(res1.json()["results"])



