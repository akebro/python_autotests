import requests

URL = 'https://api.pokemonbattle.me/v2'

HEADERS = {
    'Content-Type' : 'application/json',
    'trainer_token' : '3ddcca0fff3d7abaa1f2870cd1b4cb3b'
    }

TOKEN = '3ddcca0fff3d7abaa1f2870cd1b4cb3b'

body = {
    "name": "generate",
    "photo": "generate"
    }

body_confirm = {
    "pokemon_id": "2244",
    "name": "Рак",
    "photo": "https://dolnikov.ru/pokemons/albums/027.png"
    }


body_confirm1 ={
    "pokemon_id": "2244"
}

response = requests.post(url = f'{URL}/pokemons', headers = HEADERS, json = body)

print(response.text)

response_confirm = requests.put(url = f'{URL}/pokemons', headers = HEADERS, json = body_confirm)

print(response_confirm.text)

response_confirm1 = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADERS, json = body_confirm1)

print(response_confirm1.text)