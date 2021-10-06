def delete_pokemon_forms(pokemon):
    # Suffixes of pokemon forms
    forms = ('-mega', '-alola', '-galar', '-gmax')
    # Filtering Mega Evolutions, Alolan, Galarian and Gigantamax forms
    criteria = pokemon['name'].map(lambda name: not name.endswith(forms))
    df = pokemon[criteria]

    return df
