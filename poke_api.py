import urllib3
import json
import math
import random

def personality_value():
  return random.randint(0, 254) % 25

def get_pokemon():
  http = urllib3.PoolManager()
  res = http.request('GET', 'https://pokeapi.co/api/v2/pokemon/bulbasaur')
  json_data = json.loads(res.data.decode('utf-8'))
  return json_data

def hp_stat(base_stat, iv, ev, lvl):
  return math.floor(((2 * base_stat + iv + math.floor(ev / 4)) * lvl) / 100) + lvl + 10

def other_stat(base_stat, iv, ev, lvl, nature):
  return math.floor((hp_stat(base_stat, iv, ev, lvl) - lvl - 5) * nature)

def calculate_stats(pokemon):
  pokemon_stats = pokemon['stats']
  total_stats = {}
  iv = ev = 0
  lvl = 50
  nature = 1
  for stat in pokemon_stats:
    stat_value = stat['base_stat']
    stat_name = stat['stat']['name']
    total_stats[stat_name] = other_stat(stat_value, iv, ev, lvl, nature)
  
  return total_stats

def main():
  print('MAIN')
  pokemon = get_pokemon()
  total_stats = calculate_stats(pokemon)
  print(total_stats)


if __name__ == '__main__':
  main()