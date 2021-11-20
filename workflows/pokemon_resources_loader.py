from data_loading.db_populate import DatabasePersistence
from data_loading.poke_api import get_pokemon_resources


def main():
    persistence = DatabasePersistence()

    df_resources = get_pokemon_resources()
    persistence.save_pokemon_resources(df_resources)


if __name__ == '__main__':
    main()
