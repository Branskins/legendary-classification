import numpy as np
import matplotlib.pyplot as plt

from data_modeling.clustering import distance


def heatmap(data, row_labels, col_labels, ax=None):

    if not ax:
        ax = plt.gca()

    im = ax.imshow(data)

    ax.set_xticks(np.arange(len(row_labels)))
    ax.set_yticks(np.arange(len(col_labels)))

    # ax.set_xticklabels(row_labels)
    # ax.set_yticklabels(col_labels)

    return im


def main():
    data, labels = distance()

    fig, ax = plt.subplots()
    im = heatmap(data, labels, labels, ax)
    fig.savefig('clustering.png')


if __name__ == '__main__':
    main()
