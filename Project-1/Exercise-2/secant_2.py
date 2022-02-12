e = 5.e-6  # ακρίβεια 5 δεκαδικών ψηφίων


def secant(f, x0, x1, x2):
    xi = x0
    xi1 = x1
    xi2 = x2
    n = 1
    while abs(f(xi)) > e:
        q = f(xi) / f(xi1)
        r = f(xi2) / f(xi1)
        s = f(xi2) / f(xi)
        xi3 = xi2 - (r * (r - q) * (xi2 - xi1) + (1 - r) * s * (xi2 - xi)) / ((q - 1) * (r - 1) * (s - 1))
        xi = xi1
        xi1 = xi2
        xi2 = xi3
        n += 1
    return xi


if __name__ == "__main__":

    f = lambda x: 54 * x ** 6 + 45 * x ** 5 - 102 * x ** 4 - 69 * x ** 3 + 35 * x ** 2 + 16 * x - 4

    print(secant(f, -2, -1.75, -1.5))
    print(secant(f, -1, -.5, 0))
    print(secant(f, 0, .125, .25))
    print(secant(f, .4, .625, 1))
    print(secant(f, 1, 1.5, 2))
