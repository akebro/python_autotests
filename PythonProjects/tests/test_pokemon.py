import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2'

HEADERS = {
    'Content-Type' : 'application/json',
    'trainer_token' : '3ddcca0fff3d7abaa1f2870cd1b4cb3b'
    }

TOKEN = '3ddcca0fff3d7abaa1f2870cd1b4cb3b'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : 2313})
    assert response.status_code == 200
    

def test_part_of_response():
        response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : 2313})
        assert response.json()['data'][0]['trainer_name'] == 'Рак'