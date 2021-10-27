import numpy as np
import pandas as pd
from sklearn.cluster import AgglomerativeClustering
from datetime import date


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
    # When selecting rows on a DataFrame the index doesn't match with the labels
    # It's necessary to reset the index to make a column bind
    pokemon_stats = pokemon_stats.reset_index(drop=True)

    # Create clustering model
    clustering = AgglomerativeClustering(linkage=linkage).fit(stats)
    # Format clustering labels for concatenating
    labels = pd.Series(clustering.labels_, name='legendary')

    # Concat the results with the stats
    clustering_mapping_df = pd.concat([pokemon_stats, labels], axis=1)
    # Save the results
    today = date.today().strftime('%Y-%m-%d')
    csv_name = f'pokemon_results/results_{linkage}_{today}.csv'
    clustering_mapping_df.to_csv(csv_name)

    return clustering
