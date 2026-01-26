import requests

from random import choice
# import pyfiglet

# header = pyfiglet.pyfiglet_format("DAD JOKE 3000")

user_query = input("What would like for the day? ")

url1 = "https://icanhazdadjoke.com/search"

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
