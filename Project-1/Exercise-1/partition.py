import numpy as np

e = 5.e-6  # ακρίβεια 5 δεκαδικών ψηφίων


def partition(f, a, b):
    n = 1
    if np.sign(f(a)) * np.sign(f(b)) >= 0:
        return
    while (b - a) * .5 > e:
        m = (b + a) * .5
        if abs(f(m)) < e:
            break
        if np.sign(f(a)) * np.sign(f(m)) < 0:
            b = m
        else:
            a = m
        n += 1
    return m


if __name__ == "__main__":

    f = lambda x: 14 * x * np.exp(x - 2) - 12 * np.exp(x - 2) - 7 * x ** 3 + 20 * x ** 2 - 26 * x + 12

    print(partition(f, 0, 1.5))
    print(partition(f, 1.5, 3))