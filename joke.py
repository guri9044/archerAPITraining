import requests

url = "https://icanhazdadjoke.com/"

headers = {
  'Accept': 'application/json'
}

response = requests.get("https://icanhazdadjoke.com/", headers={'Accept': 'application/json'})
#response = requests('GET', "https://icanhazdadjoke.com/", headers={'Accept': 'application/json'})
jokeObj = response.json()
print(jokeObj["joke"])



if response.status_code == 200:
    joke = response.json().get('joke', 'No joke found.')
    print(joke)
else:
    print("Failed to fetch joke:", response.status_code)
