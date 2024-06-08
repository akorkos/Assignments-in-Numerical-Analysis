import numpy as np
import matplotlib.pyplot as plt
import tikzplotlib as tk

def lagrangeCoefficients(xi, x, n):
    L = np.ones(n)

    for i in range(n):
        for j in range(n):
            if i != j:
                L[i] *= (x - xi[j]) / (xi[i] - xi[j])
    return L


def lagrange(xi, yi, x):
    n = xi.shape[0]
    pn = 0

    for i in range(n):
        pn += yi[i] * lagrangeCoefficients(xi, x, n)[i]

    return pn


if __name__ == "__main__":

    # === 5.b ===

    f = lambda x: np.sin(x)
    d10f = lambda x: -np.sin(x)
    x = np.array([-np.pi, -2.80, -2.22, -1.31, -.19, .07, .8, 1.94, 3.07, np.pi])
    y = f(x)

    estimates = np.array([lagrange(x, y, xi) for xi in x])

    for i in estimates:
        print('%5f' % i)

    # === 5.b ===

    x1 = np.linspace(-np.pi, np.pi, 200)
    y1 = f(x1)

    estimates = np.zeros(200)

    for i in range(200):
        estimates[i] = lagrange(x, y, x1[i])

    errors = y1 - estimates
    min = np.min(errors)
    max = np.max(errors)
    print("%5f" % min, "%5f" % max)

    error = np.sqrt(sum((estimates - y1) ** 2) / 200)
    print("%f" % error)

    plt.title("Lagrange")
    plt.ylabel("Σφάλμα")
    plt.xlabel("$x$")
    plt.plot(x1, errors, color = "green")
    plt.ticklabel_format(style='plain')
    # plt.show()
    tk.save("t.tex")