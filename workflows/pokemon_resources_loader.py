"""Start point of the execution workflow"""
from data_loading.db_populate import DatabasePersistence
from data_loading.poke_api import get_pokemon_resources


def main():
    """Loads the URL for every Pokemon, this saves the Pokemon name and the URL API"""
    persistence = DatabasePersistence()

    df_resources = get_pokemon_resources()
    persistence.save_pokemon_resources(df_resources)


if __name__ == '__main__':
    main()
