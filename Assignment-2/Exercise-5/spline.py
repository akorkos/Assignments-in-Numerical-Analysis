import numpy as np
import matplotlib.pyplot as plt


def splines(xi, yi):
    n = xi.shape[0]
    A = np.zeros((n, n))
    r = np.zeros(n)
    dx = np.zeros(n - 1)
    dy = np.zeros(n - 1)
    a = yi.copy()
    b = np.zeros(n)
    d = np.zeros(n)

    for i in range(n - 1):
        dx[i] = xi[i + 1] - xi[i]
        dy[i] = yi[i + 1] - yi[i]

    A[0, 0] = 1
    A[-1, -1] = 1

    for i in range(1, n - 1):
        A[i, i] = 2 * (dx[i-1] + dx[i])
        A[i, i + 1] = dx[i]
        A[i, i - 1] = dx[i - 1]

        r[i] = 3 * (dy[i] / dx[i] - dy[i - 1] / dx[i - 1])

    c = np.linalg.inv(A).dot(r)

    for i in range(n - 1):
        b[i] = dy[i] / dx[i] - dx[i] * (2 * c[i] + c[i + 1]) / 3
        d[i] = (c[i + 1] - c[i]) / (3 * dx[i])

    return a, b, c, d


def calculateValue(a, b, c, d, xi, x):
    n = xi.shape[0]
    pos = 0
    for i in range(n - 1):
        if xi[i] <= x <= xi[i + 1]:
            pos = i
            break
        elif xi[i] == xi[n - 1]:
            pos = n - 1

    return a[pos] + b[pos]*(x - xi[pos]) + c[pos]*(x - xi[pos])**2 + d[pos]*(x - xi[pos])**3


if __name__ == "__main__":

    # === 5.a ===

    f = lambda x: np.sin(x)

    x = np.array([-np.pi, -2.80, -2.22, -1.31, -.19, .07, .8, 1.94, 3.07, np.pi])
    y = np.array(f(x))

    a, b, c, d = splines(x, y)

    estimatedValues = np.array([calculateValue(a, b, c, d, x, x_i) for x_i in x])

    print(estimatedValues)

    # === 5.b ===

    x1 = np.linspace(-np.pi, np.pi, 200)
    y1 = f(x1)

    estimatedValues = np.array([calculateValue(a, b, c, d, x, x_i) for x_i in x1])

    errors = y1 - estimatedValues
    min = np.min(errors)
    max = np.max(errors)


    error = np.sqrt(sum((estimatedValues - y1) ** 2) / 200)
    print("%f" % error)

    plt.title("Spline")
    plt.ylabel("Σφάλμα")
    plt.xlabel("$x$")
    plt.plot(x1, errors, color="r")
    plt.ticklabel_format(style='plain')
    plt.show()
