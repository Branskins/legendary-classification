import pandas as pd
import data_loading.poke_api as api

from data_loading.db_populate import DatabasePersistence


def get_pokemon_apply(url):
    json_pokemon = api.get_pokemon(url)
    df_stats = pd.DataFrame(json_pokemon['stats'])
    s = pd.Series(df_stats['base_stat'])
    return s


def main():
    persistence = DatabasePersistence()
    column_names = ['hp', 'attack', 'defense', 'special_attack', 'special_defense', 'speed']

    df_resources = persistence.read_pokemon_resources()
    s_url = df_resources['url']
    s_name = df_resources['name']

    df_base_stats = s_url.apply(get_pokemon_apply)

    df_base_stats = df_base_stats.rename(dict(zip(range(6), column_names)), axis='columns')
    df_base_stats.insert(0, 'name', s_name)

    persistence.save_base_stats(df_base_stats)


if __name__ == '__main__':
    main()




