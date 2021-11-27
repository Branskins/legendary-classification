import csv
import os
import pandas as pd
import pyodbc

from datetime import date
from sqlalchemy import create_engine
from sqlalchemy.engine import URL


class DataPersistence:

    def __init__(self):
        self.today = date.today().strftime('%Y-%m-%d')

    def save_pokemon_resources(self, resources):
        pass

    def read_pokemon_resources(self):
        pass

    def save_base_stats(self, stats):
        pass

    def read_base_stats(self):
        pass

    def save_calculated_stats(self, stats):
        pass

    def read_calculated_stats(self):
        pass

    def save_hierarchical_model_stats(self, stats):
        pass

    def read_hierarchical_model_stats(self):
        pass


class DatabasePersistence(DataPersistence):

    def __init__(self,
                 driver='{ODBC Driver 17 for SQL Server}',
                 server='localhost',
                 database='LegendaryClassification'):
        self.driver = driver
        self.server = server
        self.database = database
        self.engine = self._create_engine()
        self.pokemon_resource_table = 'PokemonResource'
        self.base_stat_table = 'BaseStat'
        self.calculated_stat_table = 'CalculatedStat'
        self.model_stat_table = 'HierarchicalModelStat'

    def _create_engine(self):
        connection_string = f'DRIVER={self.driver};SERVER={self.server};DATABASE={self.database};Trusted_Connection=yes'
        connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})

        engine = create_engine(connection_url)

        return engine

    def test_connection(self):
        _str = f'DRIVER={self.driver};SERVER={self.server};DATABASE={self.database};Trusted_Connection=yes'
        cnxn = pyodbc.connect(_str)
        cursor = cnxn.cursor()

    def save_pokemon_resources(self, resources):
        resources.to_sql(self.pokemon_resource_table, self.engine, if_exists='replace', index=False)

    def read_pokemon_resources(self):
        return pd.read_sql_table(self.pokemon_resource_table, self.engine)

    def save_base_stats(self, stats):
        stats.to_sql(self.base_stat_table, self.engine, if_exists='replace', index=False)

    def read_base_stats(self):
        return pd.read_sql_table(self.base_stat_table, self.engine)

    def save_calculated_stats(self, stats):
        stats.to_sql(self.calculated_stat_table, self.engine, if_exists='append', index=False)

    def read_calculated_stats(self):
        return pd.read_sql_table(self.calculated_stat_table, self.engine)

    def save_hierarchical_model_stats(self, stats):
        stats.to_sql(self.model_stat_table, self.engine, if_exists='replace', index=False)

    def read_hierarchical_model_stats(self):
        return pd.read_sql_table(self.model_stat_table, self.engine)


class CSVPersistence(DataPersistence):

    def save_pokemon_resources(self, resources):
        self.save_pokemon_resources_to_csv()

    def save_pokemon_resources_to_csv(self, pokemon):
        # Set CSV file name with today's date
        csv_name = f'pokemon_resources/pokemon_resources_{self.today}.csv'
        # Save temporary data into a CSV file
        with open(csv_name, 'w', newline='') as csvfile:
            field_names = pokemon[0].keys()
            writer = csv.DictWriter(csvfile, fieldnames=field_names)

            writer.writeheader()
            writer.writerows(pokemon)

    def read_pokemon_resources(self):
        return self.read_resources_from_csv()

    def read_resources_from_csv(self):
        files = []
        pokemon = []
        # Read all the CSV files
        with os.scandir('pokemon_resources') as it:
            files = [(entry.name, entry.stat().st_mtime) for entry in it if
                     entry.is_file() and entry.name.endswith('.csv')]
        # Order by date, get the latest date on top
        files = sorted(files, key=lambda entry: entry[1], reverse=True)
        csv_name = f'pokemon_resources/{files[0][0]}'
        # Read the most recent CSV file, make a list of dict
        with open(csv_name, 'r') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                pokemon.append(dict(row))

        return pokemon

    def save_hierarchical_model_stats(self, stats):
        self.save_pokemon_stats_to_csv()

    def save_pokemon_stats_to_csv(self, pokemon):
        # Set CSV file name with today's date
        csv_name = f'pokemon_stats/pokemon_stats_{self.today}.csv'
        # Save temporary data into a CSV file
        with open(csv_name, 'w', newline='') as csvfile:
            field_names = pokemon[0].keys()
            writer = csv.DictWriter(csvfile, fieldnames=field_names)

            writer.writeheader()
            writer.writerows(pokemon)

    def read_hierarchical_model_stats(self):
        return self.read_stats_from_csv()

    def read_stats_from_csv(self):
        files = []
        pokemon_df = pd.DataFrame()
        # Read all the CSV files
        with os.scandir('pokemon_stats') as it:
            files = [(entry.name, entry.stat().st_mtime) for entry in it if
                     entry.is_file() and entry.name.endswith('.csv')]
        # Order by date, get the latest date on top
        files = sorted(files, key=lambda entry: entry[1], reverse=True)
        csv_name = f'pokemon_stats/{files[0][0]}'
        # Read the most recent CSV file
        pokemon_df = pd.DataFrame(pd.read_csv(csv_name))

        return pokemon_df

