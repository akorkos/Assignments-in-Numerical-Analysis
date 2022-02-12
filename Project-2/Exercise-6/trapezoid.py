import numpy as np


def trapezoidError(d2f, a, b, n):
    M = abs(d2f(b))
    if abs(d2f(a)) > abs(d2f(b)):
        M = abs(d2f(a))

    return (b - a) ** 3 * M / (12 * n ** 2)


def trapezoid(f, a, b, n):
    I = f(a) + f(b)
    h = (b - a) / n

    for i in range(1, n):
        xi = a + i * h
        I += 2 * f(xi)

    I *= h / 2

    return I


if __name__ == "__main__":
    f = lambda x: np.sin(x)
    d2f = lambda x: - np.sin(x)

    print("%f" % (trapezoid(f, 0, np.pi / 2, 10)), "%f" % (trapezoidError(d2f, 0, np.pi / 2, 10)))
