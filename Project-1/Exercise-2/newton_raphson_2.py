e = 5.e-6  # ακρίβεια 5 δεκαδικών ψηφίων


def newton(f, df, d2f, x0):
    n = 1
    xi = x0
    while True:
        xi_1 = xi- (1 / ((df(xi) / f(xi)) - (d2f(xi) / (2 * df(xi)))))
        if abs(f(xi_1) / df(xi_1)) < e:
            break
        n += 1
        xi = xi_1
    return xi


if __name__ == "__main__":

    f = lambda x: 54 * x ** 6 + 45 * x ** 5 - 102 * x ** 4 - 69 * x ** 3 + 35 * x ** 2 + 16 * x - 4

    df = lambda x: 324 * x ** 5 + 225 * x ** 4 - 408 * x ** 3 - 207 * x ** 2 + 70 * x + 16

    d2f = lambda x: 1620 * x ** 4 + 900 * x ** 3 - 1224 * x ** 2 - 414 * x + 70

    print(newton(f, df, d2f, -2))

    print(newton(f, df, d2f, -1))

    print(newton(f, df, d2f, 0))

    print(newton(f, df, d2f, .7))

    print(newton(f, df, d2f, 1))