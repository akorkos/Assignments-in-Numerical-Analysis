import numpy as np

e = 5.e-6  # ακρίβεια 5 δεκαδικών ψηφίων


def converge(df, x):
    x = round(x, 2)
    if df(x) != 0:
        return True
    return False


def newton(f, df, x0):
    n = 1
    xi = x0
    while df(xi) != 0:
        xi_1 = xi - f(xi) / df(xi)
        if abs(f(xi_1) / df(xi_1)) < e:
            break
        n += 1
        xi = xi_1
    return xi


if __name__ == "__main__":

    f = lambda x: 14 * x * np.exp(x-2) - 12 * np.exp(x-2) - 7 * x ** 3 + 20 * x ** 2 - 26 * x + 12

    df = lambda x: 14 * x * np.exp(x-2) + 2 * np.exp(x-2) - 21 * x ** 2 + 40 * x - 26

    r1 = newton(f, df, 0)
    r2 = newton(f, df, 3)

    print(r1)
    print(r2)

    print(converge(df, r1))
    print(converge(df, r2))