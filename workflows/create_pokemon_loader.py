import pandas as pd
import data_preparation.wild_pokemon as wp

from data_loading.db_populate import DatabasePersistence
from data_preparation.clean_pokemon import delete_pokemon_forms


def main():
    persistence = DatabasePersistence()
    df_base_stats = persistence.read_base_stats()
    df_base_stats = delete_pokemon_forms(df_base_stats)

    s_pokemon_names = df_base_stats.iloc[:, 0]

    for index in range(30):
        print(f'Iteration #{index}')
        df_stats = df_base_stats.iloc[:, 1:].apply(wp.calculate_stats_apply, axis=1)
        df_stats = pd.concat([s_pokemon_names, df_stats], axis=1)
        persistence.save_calculated_stats(df_stats)


if __name__ == '__main__':
    main()
