import requests

from random import choice
# import pyfiglet

# header = pyfiglet.pyfiglet_format("DAD JOKE 3000")

user_query = input("What would like for the day? ")

url1 = "https://icanhazdadjoke.com/search"

# Accept : text/html -> this will give you the all html of the page
# Accept : text/plain -> this will give you the plain text of the page

res = requests.get(url1, headers={"Accept" : "application/json"}, params={"term" : user_query}).json()

num_joke = res["total_jokes"]
resutls = res["results"]
if num_joke > 1:
    print(f"There are {num_joke} jokes")
    print(choice(resutls)["joke"])
elif num_joke == 1:
    print("There is one joke: ")
    print(res["results"][0]['joke'])
else:
    print("There is no joke")
# print(res)

# HTTP VERBS
# 1. GET Requests
# useful for retrieving data, going to google.com etc
# Data is passed in query string, no side effects
# can be cached, can be bookmarked
# 2. Post Requests
# useful for submitting data, like submitting a comment on reddit, sending something to a server
# data is passed in the request body, all sort of data, photos, etc
# can have side effects
#cannot be cached or bookmarked


#API-> Application Programming Interface
# allow you to get data from another application without needing to understand how the application works
#


