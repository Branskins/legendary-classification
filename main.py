import math
import random

from personality_value_nature import p_value_nature
from db_populate import get_pokemon_from_csv
from poke_api import get_pokemon

def hp_stat(base_stat, iv, ev, lvl):
  return math.floor(((2 * base_stat + iv + math.floor(ev / 4)) * lvl) / 100) + lvl + 10

def other_stat(base_stat, iv, ev, lvl, nature):
  return math.floor((hp_stat(base_stat, iv, ev, lvl) - lvl - 5) * nature)

def personality_value():
  return random.randint(0, 254) % 25

def create_nature_instance(nature_name):
  module = __import__('nature')
  class_ = getattr(module, nature_name)
  instance = class_()
  return instance

def define_nature():
  p_value = personality_value()
  nature_name = p_value_nature[p_value]
  nature_instance = create_nature_instance(nature_name)
  return nature_instance

def calculate_stats(pokemon):
  pokemon_stats = pokemon['stats']
  total_stats = {}
  iv = ev = 0
  lvl = 50
  nature_instance = define_nature()
  print(f'Pokemon nature: {type(nature_instance).__name__}')

  for stat in pokemon_stats:
    stat_value = stat['base_stat']
    stat_name = stat['stat']['name']
    nature = nature_instance.multiplier(stat_name)
    if stat_name == 'hp':
      total_stats[stat_name] = hp_stat(stat_value, iv, ev, lvl)
    else:
      total_stats[stat_name] = other_stat(stat_value, iv, ev, lvl, nature)
  
  return total_stats

def create_pokemon():
  pass

def main():
  print('MAIN')


if __name__ == '__main__':
  main()