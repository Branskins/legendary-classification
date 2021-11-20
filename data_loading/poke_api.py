import pandas as pd
import urllib3
import json
import logging

logging.basicConfig(
    filename='poke_api.log',
    format='%(asctime)s - %(levelname)s: %(message)s',
    level=logging.DEBUG
)


def get_pokemon(url):
    json_data = None

    try:
        logging.info("Data loading process started: Getting individual Pokemon data")

        http = urllib3.PoolManager()
        res = http.request('GET', url)
        json_data = json.loads(res.data.decode('utf-8'))

        logging.info("Data loading process completed")
    except urllib3.exceptions.NewConnectionError:
        logging.warning("Data loading process failed: Error getting individual Pokemon data")
    except json.decoder.JSONDecodeError:
        logging.warning("Data loading process failed: Error Loading JSON")

    return json_data


def get_pokemon_resources():
    # Initialize data to retrieve
    resources = pd.DataFrame()
    # Do initial HTTP request
    try:
        logging.info("Data loading process started: Getting all Pokemon resources")

        http = urllib3.PoolManager()
        res = http.request('GET', 'https://pokeapi.co/api/v2/pokemon?limit=200')
        json_data = json.loads(res.data.decode('utf-8'))
        # Append pokemon results
        if len(json_data['results']) > 0:
            resources = pd.DataFrame(json_data['results'])

        while json_data['next'] is not None:
            # Get next URL to retrieve remaining data
            next_request = json_data['next']
            res = http.request('GET', next_request)
            json_data = json.loads(res.data.decode('utf-8'))
            # Append new data from pagination result
            if len(json_data['results']) > 0:
                resources = resources.append(pd.DataFrame(json_data['results']), ignore_index=True)

        logging.info("Data loading process completed")
    except urllib3.exceptions.NewConnectionError:
        logging.warning("Data loading process failed: Error getting all Pokemon resources")
    except json.decoder.JSONDecodeError:
        logging.warning("Data loading process failed: Error Loading JSON")

    return resources


def main():
    # Test for get_pokemon()
    url_to_success = 'https://pokeapi.co/api/v2/pokemon/ditto'
    url_to_fail = 'https://pokeapi.co/api/v2/pokemon/ditt'

    assert get_pokemon(url_to_success) is not None
    assert get_pokemon(url_to_fail) is None

    # Test for get_pokemon_resources()
    pokemon_resources = get_pokemon_resources()
    assert len(pokemon_resources) > 0


if __name__ == '__main__':
    main()
