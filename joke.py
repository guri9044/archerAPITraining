import requests

url = "https://icanhazdadjoke.com/"

headers = {
  'Accept': 'application/json'
}

response = requests.get(url, headers=headers)
if response.status_code == 200:
    joke = response.json().get('joke', 'No joke found.')
    print(joke)
else:
    print("Failed to fetch joke:", response.status_code)
