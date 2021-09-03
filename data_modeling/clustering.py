import numpy as np
import pandas as pd
from sklearn.cluster import AgglomerativeClustering
from datetime import date

from data_loading.db_populate import read_stats_from_csv


def distance(pokemon_stats):
    names = pokemon_stats.iloc[:, -1]
    stats = pokemon_stats.iloc[:, :-1].to_numpy()
    rows = stats.shape[0]
    distance_matrix = np.ones((rows, rows))

    for i in range(rows):
        distance_matrix[i] = np.sqrt(((stats[i] - stats[0:rows, ]) ** 2).sum(axis=1))

    return distance_matrix, names


def load_clustering(pokemon_stats, linkage):
    # Select the stats only
    stats = pokemon_stats.iloc[:, :-1]

    # Create clustering model
    clustering = AgglomerativeClustering(linkage=linkage).fit(stats)

    # Concat the results with the stats
    clustering_mapping_df = pd.concat([pokemon_stats, pd.Series(clustering.labels_, name='legendary')], axis=1)
    # Save the results
    today = date.today().strftime('%Y-%m-%d')
    csv_name = f'pokemon_results/results_{linkage}_{today}.csv'
    clustering_mapping_df.to_csv(csv_name)


def main():
    pokemon_stats = read_stats_from_csv()
    linkage_methods = ['ward', 'complete', 'average', 'single']
    for linkage in linkage_methods:
        load_clustering(pokemon_stats, linkage)


if __name__ == '__main__':
    main()