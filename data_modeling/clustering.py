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
    # Create clustering model
    clustering = AgglomerativeClustering(linkage=linkage).fit(pokemon_stats)

    return clustering
