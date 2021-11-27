import pandas as pd

from data_loading.db_populate import DatabasePersistence
from data_modeling.clustering import load_clustering


def main():
    persistence = DatabasePersistence()
    df_stats = persistence.read_calculated_stats()

    model = load_clustering(df_stats.iloc[:, 1:], 'ward')
    labels = pd.Series(model.labels_, name='legendary')
    model_mapping = pd.concat([df_stats.iloc[:, 0], labels], axis=1)

    persistence.save_hierarchical_model_stats(model_mapping)


if __name__ == '__main__':
    main()
