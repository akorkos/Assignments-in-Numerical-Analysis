import numpy as np

e = 5.e-6  # ακρίβεια 5 δεκαδικών ψηφίων


def secant(f, x0, x1):
    n = 1
    xi = x1
    xi_1 = x0
    while abs(f(xi)) > e:
        xi1 = xi - (f(xi) * (xi - xi_1)) / (f(xi) - f(xi_1))
        if abs(f(xi) - f(xi_1)) < e:
            break
        xi_1 = xi
        xi = xi1
        n += 1
    return xi


if __name__ == "__main__":

    f = lambda x: 14 * x * np.exp(x - 2) - 12 * np.exp(x - 2) - 7 * x ** 3 + 20 * x ** 2 - 26 * x + 12

    print(secant(f, 0, 1))
    print(secant(f, 0, 2.5))
