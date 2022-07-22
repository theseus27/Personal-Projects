import requests
import json

response = requests.get(f"https://pokeapi.co/api/v2/pokemon/900")
data = json.loads(response.content)
print(data)