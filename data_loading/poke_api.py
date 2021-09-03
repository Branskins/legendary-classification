import urllib3
import json


def get_pokemon(url):
    http = urllib3.PoolManager()
    res = http.request('GET', url)
    json_data = json.loads(res.data.decode('utf-8'))
    return json_data


def get_pokemon_resources():
    # Initialize data to retrieve
    all_pokemon = []
    # Do initial HTTP request
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

    return all_pokemon