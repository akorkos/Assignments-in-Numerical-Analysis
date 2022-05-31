import numpy as np


def createGoogleMatrix(A, q):
    n = A.shape[0]
    ni = []
    G = np.zeros((n, n))
    for i in range(n):
        ni.append(sum(A[i, :]))
    print(ni)
    for i in range(n):
        for j in range(n):
            G[i, j] = (q / n) + ((A[j, i] * (1 - q)) / ni[j])
            G[i, j] = round(G[i, j], 5)

    return G


def powerMethod(A):
    x = np.array([8.1, 7.3, 4.4]).T
    for _ in range(10000):
        x = np.dot(A, x)
        x = x / np.linalg.norm(x, 1)  # Κανονικοποιίηση των αποτελεσμάτων
    return x


def isStochastic(A):
    stochastic = True
    sumOfCols = A.sum(axis=0)  # Άθροισμα όλων των στηλών του πίνακα
    for i in sumOfCols:
        if round(i, 2) != 1:
            stochastic = False
    return stochastic


A = np.array([[0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                  [0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                  [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
                  [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                  [0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                  [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0]])

G = createGoogleMatrix(A, .15)

p = powerMethod(G)

stochastic = isStochastic(G)

if __name__ == "__main__":
    A = np.array([[1,8.1,4.4],[8.1, 8.1, -7.3], [4.4, -7.3, 2]])
    print(powerMethod(A))