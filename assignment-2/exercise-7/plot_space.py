import numpy as np
import matplotlib.pyplot as plt
import tikzplotlib as tk

def leastSquares(xi, yi, degree = 9):
    n = xi.shape[0]
    A = np.zeros((n, degree))
    b = yi

    for i in range(degree):
        A[:, i] = xi[:] ** i

    c = np.linalg.inv(np.dot(A.T, A)).dot(A.T).dot(b)

    return c


def calcaluteValue(estimates, x, degree):
    coeff = 0
    for i in range(degree):
        coeff += estimates[i] * (x ** i)

    return coeff


if __name__ == "__main__":

    x = np.array([_ for _ in range(1, 11)])
    y = np.array([5.64, 5.60, 5.64, 5.70, 5.66, 5.60, 5.50, 5.50, 5.60, 5.60])
    daysToBePredicted = np.array([i for i in range(11, 16)])

    coefficients2 = np.array(leastSquares(x, y, 2))
    coefficients3 = np.array(leastSquares(x, y, 3))
    coefficients4 = np.array(leastSquares(x, y, 4))
    predictions2 = np.array([calcaluteValue(coefficients2, i, 2) for i in daysToBePredicted])
    predictions3 = np.array([calcaluteValue(coefficients3, i, 3) for i in daysToBePredicted])
    predictions4 = np.array([calcaluteValue(coefficients4, i, 4) for i in daysToBePredicted])
    actual = [5.60, 5.50, 5.54, 5.64, 5.64]

    # plt.title("ΣΠΕΙΣ")
    plt.ylabel("Τιμή")
    plt.xlabel("Α/Α συνεδρίασης")
    plt.plot(daysToBePredicted, actual, label="Πραγματική τιμή μετοχής", color="r", linestyle="dashed")
    plt.xticks(daysToBePredicted)
    plt.scatter(daysToBePredicted, predictions2, label="Πολυώνυμο 2ου βαθμού")
    plt.scatter(daysToBePredicted, predictions3, label="Πολυώνυμο 3ου βαθμού")
    plt.scatter(daysToBePredicted, predictions4, label="Πολυώνυμο 4ου βαθμού")
    plt.legend()
    # plt.show()
    tk.save("test1.tex")