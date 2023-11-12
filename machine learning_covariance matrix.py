import numpy as np

A = np.array([
    [170,60,4.1],
    [165,55,3.0],
    [174,75,2.8],
    [169,67,2.9],
    [155,49,3.1],
    [172,63,3.6],
    [166,58,3.7],
    [168,61,4.0]
])
'''
print(A)
print()
print('covariance matrix')

B= np.cov(A,rowvar=False)
print(np.array2string(B,formatter={'float_kind':lambda x:"%.3f"%x}))
'''

c= list()
for i in range(0,8):
    c.append(A[i][0])

print(c)
C= np.mean(c)
print(C)

d=list()
for i in range(0,8):
    d.append(A[i][1])
print(d)
D=np.mean(d)
print(D)

e=list()
for i in range(0,8):
    e.append(A[i][2])
print(e)
E=np.mean(e)
print(E)

print(2/9*1/3*1/3*1/3*9/14)


