import numpy as np
import pylab as pl

N = 10**4
axis_x = np.linspace(0,10,N)

### MODELING

U = np.random.uniform(-3, 3, N)

pl.title("Histogram of U")
pl.hist(U, bins=100, color='g', edgecolor='black')
pl.show()

E = np.random.uniform(-np.sqrt(3), np.sqrt(3), N)

pl.title("Histogram of E")
pl.hist(E, bins=100, color='g', edgecolor='black')
pl.show()

A = 0.5
B = 1

W = np.zeros(N)
W[0] = 0
for n in range(1, N):
    W[n] = A * W[n-1] + B * U[n]
Y = W + E

pl.title("Y")
pl.plot(axis_x, Y)
pl.show()

pl.title("Histogram of Y")
pl.hist(Y, bins=100, color='g', edgecolor='black')
pl.show()

### IDENTIFICATION
# LEAST SQUARES METHOD

def LSM(_Y, _U):
    _YforFI = _Y
    _YforFI = np.delete(_YforFI, -1)
    _YforFI = np.concatenate((np.zeros(1), _YforFI))
    _N = len(_U)
    _FI = np.zeros((_N, 2))
    for i in range(_N):
        _FI[i,0] = _YforFI[i]
        _FI[i,1] = _U[i]

    _FI_T = np.transpose(_FI)
    return np.matmul(np.matmul(np.linalg.inv(np.matmul(_FI_T, _FI)), _FI_T), _Y)

theta_dash = LSM(Y, U)
print("theta dash: ", theta_dash)

A_dash = theta_dash[0]
B_dash = theta_dash[1]

W_dash = np.zeros(N)
W_dash[0] = 0
for n in range(1, N):
    W_dash[n] = A_dash * W_dash[n-1] + B_dash * U[n]

theta_dash_iv = LSM(W_dash, U)

print("theta dash iv: ", theta_dash_iv)

pl.plot(np.linspace(0,N,N),W)
pl.show()
pl.plot(np.linspace(0,N,N),W_dash)
pl.show()
