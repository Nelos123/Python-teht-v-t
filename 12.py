import requests

response = requests.get("https://api.chucknorris.io/jokes/random")

if response.status_code == 200:
    data = response.json()
    print(data["value"])
else:
    print("haku epäonnistui")