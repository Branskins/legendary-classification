from data_loading.db_populate import read_stats_from_csv
from data_preparation.clean_pokemon import delete_pokemon_forms
from data_modeling.clustering import load_clustering
from data_modeling.persistance import save_model


def modeling_clustering():
    pokemon_stats = read_stats_from_csv()
    pokemon_stats_new = delete_pokemon_forms(pokemon_stats)
    linkage_methods = ['ward', 'complete', 'average', 'single']
    for linkage in linkage_methods:
        model = load_clustering(pokemon_stats_new, linkage)
        save_model(model, f'pokemon_models/{linkage}.joblib')


def main():
    modeling_clustering()


if __name__ == '__main__':
    main()
