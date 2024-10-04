import numpy as np

N, M = map(int, input().split())
A = []
for i  in range(N):
    row = [int(x) for x in input().split()]
    A.append(row)

A_1=np.array(A)
b = A_1[:,(M-1)]
c = np.delete(A_1, M-1, 1)
x = np.linalg.solve(c, b)
print(x)
