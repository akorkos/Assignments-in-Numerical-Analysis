import numpy as np

e = 5.e-5  # ακρίβεια 4 δεκαδικών ψηφίων

n = 10  # ή 10000


def gaussSeidel(A, x, b):
    while True:
        X0 = np.copy(x)
        for i in range(n):
            sum = 0.0
            for j in range(n):
                if i != j:
                    sum = sum + A[i, j] * x[j]
            x[i] = (b[i] - sum) / A[i, i]
        norm = 0.0
        for i in range(n):
            norm += abs(x[i] - X0[i])
        if norm < e:
            break
    return x


if __name__ == "__main__":
    A = np.zeros((n, n))
    b = np.empty((n, 1))
    x = np.zeros(n)

    for i in range(n):
        for j in range(n):
            if i == j:
                A[i, j] = 5
            elif i + 1 == j or i == j + 1:
                A[i, j] = -2

    for i in range(n):
        if i == 0 or i == n - 1:
            b[i] = 3
        else:
            b[i] = 1

    print(gaussSeidel(A, x, b))

