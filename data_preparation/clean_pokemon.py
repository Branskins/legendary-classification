import pandas as pd


def cleanse_pokemon(pokemon):
    dtf_pokemon = pd.DataFrame()

    # Filtering Mega Evolutions
    criteria = pokemon['name'].map(lambda name: name.endswith('-mega'))
    dtf_pokemon = pokemon[criteria]
    # Filtering Alolan forms
    criteria = dtf_pokemon['name'].map(lambda name: name.endswith('-alola'))
    dtf_pokemon = dtf_pokemon[criteria]
    # Filtering Galarian forms
    criteria = dtf_pokemon['name'].map(lambda name: name.endswith('-galar'))
    dtf_pokemon = dtf_pokemon[criteria]
    # Filtering Gigantamax forms
    criteria = dtf_pokemon['name'].map(lambda name: name.endswith('-gmax'))
    dtf_pokemon = dtf_pokemon[criteria]

    return dtf_pokemon
