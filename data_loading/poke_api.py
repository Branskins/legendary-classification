import urllib3
import json
import logging

logging.basicConfig(
    filename='poke_api.log',
    format='%(asctime)s - %(levelname)s: %(message)s'
)


def get_pokemon(url):
    try:
        http = urllib3.PoolManager()
        res = http.request('GET', url)
        json_data = json.loads(res.data.decode('utf-8'))
    except urllib3.exceptions.NewConnectionError:
        print('Connection failed.')
    return json_data


def get_pokemon_resources():
    # Initialize data to retrieve
    all_pokemon = []
    # Do initial HTTP request
    try:
        http = urllib3.PoolManager()
        res = http.request('GET', 'https://pokeapi.co/api/v2/pokemon?limit=200')
        json_data = json.loads(res.data.decode('utf-8'))
        # Append pokemon results
        if len(json_data['results']) > 0:
            for pokemon_resource in json_data['results']:
                all_pokemon.append(pokemon_resource)

        while json_data['next'] is not None:
            # Get next URL to retrieve remaining data
            next_request = json_data['next']
            res = http.request('GET', next_request)
            json_data = json.loads(res.data.decode('utf-8'))
            for pokemon_resource in json_data['results']:
                all_pokemon.append(pokemon_resource)
    except urllib3.exceptions.NewConnectionError:
        print('Connection failed.')

    return all_pokemon
