import numpy as np


def backSubstitution(U, b):
    n = b.size
    x = np.zeros(n)
    b = U[:, n]
    U = U[:, : n]
    n = U.shape[0]
    for i in range(n-1, -1, -1):
        temp = b[i]
        for j in range(n-1, i, -1):
            temp -= x[j] * U[i, j]
        x[i] = temp / U[i, i]
    return x


def decomposition(A, b):
    n = A.shape[0]
    U = np.concatenate((A, b), axis = 1)   # Επαυξημένος πίνακας
    L = np.identity(n)
    P = np.identity(n)
    for i in range(n):
        pivotRow = i + np.argmax(abs(U[i:, i]))
        U[[i, pivotRow]] = U[[pivotRow, i]]
        P[[i, pivotRow]] = P[[pivotRow, i]]
        for j in range(i + 1, n):
            m = U[j, i] / U[i, i]
            U[j] = U[j] - m * U[i]
            L[j, i] = m
    return U


def gauss(A, b):
    U = decomposition(A, b)
    return backSubstitution(U, b)


if __name__ == "__main__":
    A = np.array([[2., 1., 5.],
                  [4., 4., -4.],
                  [1., 3., 1.]])

    b = np.array([[5.],
                  [0.],
                  [6.]])

    print(gauss(A, b))