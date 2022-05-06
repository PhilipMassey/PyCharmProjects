import requests
import rapid_apis as ra_apis

url = "https://seeking-alpha.p.rapidapi.com/screeners/list"

headers = {
    'x-rapidapi-host': "seeking-alpha.p.rapidapi.com",
    'x-rapidapi-key': ra_apis.seeking_alpha_key
    }

response = requests.request("GET", url, headers=headers)

print(response.json())