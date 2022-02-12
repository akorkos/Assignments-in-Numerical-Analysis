import pagerank as pg
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":

    A1 = np.array([[0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                  [0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                  [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
                  [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
                  [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                  [0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                  [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0]])

    G1 = pg.createGoogleMatrix(A1, .15)

    p1 = pg.powerMethod(G1)

    G2 = pg.createGoogleMatrix(A1, .02)

    p2 = pg.powerMethod(G2)

    G3 = pg.createGoogleMatrix(A1, .6)

    p3 = pg.powerMethod(G3)

    x = [i for i in range(1, 16)]

    fig, ax = plt.subplots()
    plt.plot(x, p1, label='q = 0.15', color='green')
    ax.scatter(x, p2, label='q = 0.02', facecolors='r', edgecolors='r')
    ax.scatter(x, p3, label='q = 0.6', facecolors='b', edgecolors='b')
    plt.xticks(x)
    plt.xlabel("Ιστοσελίδα")
    plt.ylabel("Τάξη σελίδας")
    ax.legend()
    ax.grid(True)
    plt.show()