import numpy as np

from db_populate import read_stats_from_csv


def disimilitud():
    pokemon_stats = read_stats_from_csv()
    names = pokemon_stats.iloc[:, -1]
    stats = pokemon_stats.iloc[:, :-1].to_numpy()
    dis = np.ones(stats.shape)
    rows = stats.shape[0]

    for i in range(rows):
        # np.sqrt(((x[0] - x[0:5, ]) ** 2).sum(axis=1))
        np.sqrt(((stats[i] - stats[i:rows, ]) ** 2).sum(axis=1))

    return dis


def main():
    return 1


if __name__ == '__main__':
    values = main()
