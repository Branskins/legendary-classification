import numpy as np

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
    return 1


if __name__ == '__main__':
    values = main()
