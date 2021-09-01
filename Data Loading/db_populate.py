import csv
import os
import pandas as pd
from datetime import date


def save_pokemon_resources_to_csv(pokemon):
    # Set CSV file name with today's date
    today = date.today().strftime('%Y-%m-%d')
    csv_name = f'pokemon_resources/pokemon_resources_{today}.csv'
    # Save temporary data into a CSV file
    with open(csv_name, 'w', newline='') as csvfile:
        field_names = pokemon[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=field_names)

        writer.writeheader()
        writer.writerows(pokemon)


def save_pokemon_stats_to_csv(pokemon):
    # Set CSV file name with today's date
    today = date.today().strftime('%Y-%m-%d')
    csv_name = f'pokemon_stats/pokemon_stats_{today}.csv'
    # Save temporary data into a CSV file
    with open(csv_name, 'w', newline='') as csvfile:
        field_names = pokemon[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=field_names)

        writer.writeheader()
        writer.writerows(pokemon)


def read_resources_from_csv():
    files = []
    pokemon = []
    # Read all the CSV files
    with os.scandir('../pokemon_resources') as it:
        files = [(entry.name, entry.stat().st_mtime) for entry in it if entry.is_file() and entry.name.endswith('.csv')]
    # Order by date, get the latest date on top
    files = sorted(files, key=lambda entry: entry[1], reverse=True)
    csv_name = f'pokemon_resources/{files[0][0]}'
    # Read the most recent CSV file, make a list of dict
    with open(csv_name, 'r') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            pokemon.append(dict(row))

    return pokemon


def read_stats_from_csv():
    files = []
    pokemon_df = pd.DataFrame()
    # Read all the CSV files
    with os.scandir('../pokemon_stats') as it:
        files = [(entry.name, entry.stat().st_mtime) for entry in it if entry.is_file() and entry.name.endswith('.csv')]
    # Order by date, get the latest date on top
    files = sorted(files, key=lambda entry: entry[1], reverse=True)
    csv_name = f'pokemon_stats/{files[0][0]}'
    # Read the most recent CSV file
    pokemon_df = pd.DataFrame(pd.read_csv(csv_name))

    return pokemon_df
