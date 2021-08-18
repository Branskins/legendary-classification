import numpy as np
import pandas as pd
from sklearn.cluster import AgglomerativeClustering

from db_populate import read_stats_from_csv


def distance():
    pokemon_stats = read_stats_from_csv()
    names = pokemon_stats.iloc[:, -1]
    stats = pokemon_stats.iloc[:, :-1].to_numpy()
    rows = stats.shape[0]
    distance_matrix = np.ones((rows, rows))

    for i in range(rows):
        distance_matrix[i] = np.sqrt(((stats[i] - stats[0:rows, ]) ** 2).sum(axis=1))

    return distance_matrix, names


def main():
    # Load and select the stats
    pokemon_stats = read_stats_from_csv()
    stats = pokemon_stats.iloc[:, :-1]

    # Create clustering model
    clustering = AgglomerativeClustering().fit(stats)

    # Concat the results with the stats
    clustering_mapping_df = pd.concat([pokemon_stats, pd.Series(clustering.labels_, name='legendary')], axis=1)
    # Save the results
    clustering_mapping_df.to_csv('pokemon_results/results_ward_2021-08-17.csv')


if __name__ == '__main__':
    main()
