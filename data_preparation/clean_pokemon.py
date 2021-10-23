def delete_pokemon_forms(pokemon):
    # Suffixes of special pokemon forms
    forms = ('-mega', '-alola', '-galar', '-gmax')

    # Filtering Mega Evolutions, Alolan, Galarian and Gigantamax forms
    criteria = pokemon['name'].map(lambda name: not name.endswith(forms))
    df_forms = pokemon[criteria]

    variations = ('pikachu-', 'castform-', 'kyogre-', 'groudon-', 'greninja-', 'necrozma-', 'magearna-', 'eternatus-')
    # Filtering Pikachu forms
    pikachu_criteria = df_forms['name'].map(lambda name: not name.startswith(variations))
    df = df_forms[pikachu_criteria]

    return df
