#numpy로 공분산행렬 구하기 

import numpy as np
A = np.array([[170,165,174,169,155,172,166,168]])
B = np.array([[60,55,75,67,49,63,58,61]])
C = np.array([[4.1,3.0,2.8,2.9,3.1,3.6,3.7,4.0]])

print(A)
print("평균")
print(np.mean(A))
print("분산")
print(np.var(A))
print()

print(B)
print("평균")
print(np.mean(B))
print("분산")
print(np.var(B))
print()

print(C)
print("평균")
print(np.mean(C))
print("분산")
print(np.var(C))


COV_MAT = np.array([
    [170, 60, 4.1],
    [165,55,3.0],
    [174,75,2.8],
    [169,67,2.9],
    [155,49,3.1],
    [172,63,3.6],
    [166,58,3.7],
    [168,61,4.0]
])


print(COV_MAT)
print()
print("Covariance matrix")
B= np.cov(COV_MAT,rowvar=False)
print(np.array2string(B,formatter={'float_kind':lambda x:"%.4f"% x}))





