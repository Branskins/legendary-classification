import pyodbc
import urllib3
import json

driver = '{ODBC Driver 17 for SQL Server}'
server = 'localhost' 
database = 'POKEMON_URL' 

con_string = f'DRIVER={driver};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
conn = pyodbc.connect(con_string)

def get_all_pokemon():
  # Initialize data to retrieve
  all_pokemon = []
  # Do initial HTTP request
  http = urllib3.PoolManager()
  res = http.request('GET', 'https://pokeapi.co/api/v2/pokemon?limit=200')
  json_data = json.loads(res.data.decode('utf-8'))
  # Append pokemon results
  all_pokemon.append(json_data['results'])

  while(json_data['next'] != None):
    # Get next URL to retrieve remaining data 
    next_request = json_data['next']
    res = http.request('GET', next_request)
    json_data = json.loads(res.data.decode('utf-8'))
    all_pokemon.append(json_data['results'])

  return all_pokemon

if __name__ == '__main__':
  pokemon = get_all_pokemon()
  print(len(pokemon))