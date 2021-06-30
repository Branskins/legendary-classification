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
  print(json_data)

def hp_stat(base_stat, iv, ev, lvl):
  return math.floor(((2 * base_stat + iv + math.floor(ev / 4)) * lvl) / 100) + lvl + 10

def other_stat(base_stat, iv, ev, lvl, nature):
  return math.floor((hp_stat(base_stat, iv, ev, lvl) - lvl - 5) * nature)

def main():
  print('MAIN')


if __name__ == '__main__':
  main()