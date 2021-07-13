from db_populate import save_pokemon_to_csv

def pokemon_resources():
  pokemon_main_piece = []

  pokemon_main_piece.append({'name': 'wobbuffet', 'url': 'https://pokeapi.co/api/v2/pokemon/202/'})
  pokemon_main_piece.append({'name': 'girafarig', 'url': 'https://pokeapi.co/api/v2/pokemon/203/'})
  pokemon_main_piece.append({'name': 'pineco', 'url': 'https://pokeapi.co/api/v2/pokemon/204/'})
  pokemon_main_piece.append({'name': 'forretress', 'url': 'https://pokeapi.co/api/v2/pokemon/205/'})

  return pokemon_main_piece

def main():
  pokemon = pokemon_resources()
  save_pokemon_to_csv(pokemon)

if __name__ == '__main__':
  main()