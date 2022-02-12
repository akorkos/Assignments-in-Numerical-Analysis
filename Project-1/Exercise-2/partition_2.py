from random import uniform
import numpy as np

e = 5.e-6  # ακρίβεια 5 δεκαδικών ψηφίων


def partition(f, a, b):
    n = 1
    if np.sign(f(a)) * np.sign(f(b)) >= 0:
        return
    while (b - a) * .5 > e:
        m = uniform(a, b)
        if abs(f(m)) < e:
            break
        if np.sign(f(a)) * np.sign(f(m)) < 0:
            b = m
        else:
            a = m
        n += 1
    return m


if __name__ == "__main__":

    f = lambda x: 54 * x ** 6 + 45 * x ** 5 - 102 * x ** 4 - 69 * x ** 3 + 35 * x ** 2 + 16 * x - 4

    print(partition(f, -2, -1))
    print(partition(f, -1, -.5))
    print(partition(f, 0, .25))
    print(partition(f, .25, .75))
    print(partition(f, 1, 2))
