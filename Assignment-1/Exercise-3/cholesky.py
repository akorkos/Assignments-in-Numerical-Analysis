import numpy as np


def cholesky(A):
    (n, m) = A.shape
    L = np.zeros((n, m))
    for k in range(n):
        for i in range(k + 1):
            sum = 0
            for j in range(i):
                sum += L[i, j] * L[k, j]
            if k == i:
                L[k, i] = np.sqrt(A[k, k] - sum)
            else:
                L[k, i] = (A[k, i] - sum) / L[i, i]
    return L


if __name__ == "__main__":

    A = np.array([[4, -1, 1],
                  [-1, 4.25, 2.75],
                  [1, 2.75, 3.5]])

    print(cholesky(A))

