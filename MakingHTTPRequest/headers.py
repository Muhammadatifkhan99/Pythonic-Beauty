import requests

url = "https://icanhazdadjoke.com/"

# response = requests.get(url, headers={"Accept" : "text/plain"})
response = requests.get(url, headers={"Accept" : "application/json"})



print(response.text) # this is a string so we can not extract out the joke out of this
print(type(response.text))
print(type(response.json()))
print(response.json())

print("The id of the joke is: ", response.json()["id"])
print("The status code of the joke is: ", response.json()["status"])
print("The joke is: ", response.json()["joke"])