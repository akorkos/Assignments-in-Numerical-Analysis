import pagerank as pg
import numpy as np
import matplotlib.pyplot as plt


if __name__ == "__main__":

    A3 = np.array([[0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                  [0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                  [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
                  [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                  [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                  [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                  [0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0]])

    G5 = pg.createGoogleMatrix(A3, .15)
    p5 = pg.powerMethod(G5)

    x = [i for i in range(1, 16)]

    fig, ax = plt.subplots()
    p5 = np.insert(p5, 9, 0)
    ax.scatter(x, pg.p, label='Γράφος με την σελίδα 10', facecolors='r', edgecolors='r')
    ax.scatter(x, p5, label='Γράφος δίχως την σελίδα 10', facecolors='b', edgecolors='b')
    plt.xticks(x)
    plt.ylabel("Βαθμός σημαντικότητας")
    plt.xlabel("Ιστοσελίδα")
    plt.grid(True)
    plt.legend()
    plt.show()