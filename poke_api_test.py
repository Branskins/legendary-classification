def main():
  pokemon_main_piece = []

  pokemon_piece_1 = []
  pokemon_piece_1.append({'name': 'wobbuffet', 'url': 'https://pokeapi.co/api/v2/pokemon/202/'})
  pokemon_piece_1.append({'name': 'girafarig', 'url': 'https://pokeapi.co/api/v2/pokemon/203/'})

  pokemon_piece_2 = []
  pokemon_piece_2.append({'name': 'pineco', 'url': 'https://pokeapi.co/api/v2/pokemon/204/'})
  pokemon_piece_2.append({'name': 'forretress', 'url': 'https://pokeapi.co/api/v2/pokemon/205/'})

  pokemon_main_piece.append(pokemon_piece_1)
  pokemon_main_piece.append(pokemon_piece_2)

  print(pokemon_main_piece)
  print(len(pokemon_main_piece))

if __name__ == '__main__':
  main()