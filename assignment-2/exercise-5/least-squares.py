import numpy as np
import matplotlib.pyplot as plt
import tikzplotlib as tk

def leastSquares(xi, yi, degree = 9):
    n = xi.shape[0]
    A = np.zeros((n, degree))

    for i in range(degree):
        A[:, i] = xi[:] ** i

    b = yi
    c = np.linalg.inv(np.dot(A.T, A)).dot(A.T).dot(b)

    # === RMSE ===

    r = b - np.dot(A, c)
    normOfr = np.sqrt(sum(r ** 2))
    error = normOfr / np.sqrt(degree)

    print("%f" % error)

    return c


def calcaluteValue(estimates, x, degree):
    coeff = 0
    for i in range(degree):
        coeff += estimates[i] * (x ** i)

    return coeff


if __name__ == "__main__":

    # === 5.a ===

    f = lambda x: np.sin(x)
    x = np.array([-np.pi, -2.80, -2.22, -1.31, -.19, .07, .8, 1.94, 3.07, np.pi])
    y = np.array(f(x))
    degree = 9

    coefficients = np.array(leastSquares(x, y))

    estimatedValues = np.array([calcaluteValue(coefficients, x_i, degree) for x_i in x])

    print(estimatedValues)

    # === 5.b ===

    x = np.linspace(-np.pi, np.pi, 200)
    y = f(x)
    degree = 9

    estimates = leastSquares(x, y)

    estimatedValues = np.array([calcaluteValue(coefficients, x_i, degree) for x_i in x])

    errors = y - estimatedValues

    min = np.min(errors)
    max = np.max(errors)

    plt.title("Ελάχιστα τετράγωνα")
    plt.ylabel("Σφάλμα")
    plt.xlabel("$x$")
    plt.plot(x, errors, color="blue")
    plt.ticklabel_format(style='plain')
    # plt.show()
    tk.save("tτ.tex")
