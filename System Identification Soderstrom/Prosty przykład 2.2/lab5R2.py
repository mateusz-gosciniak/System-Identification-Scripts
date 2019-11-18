import numpy as np
import pylab as pl

N = 10000

U = np.random.rand(N)
Z = np.random.uniform(-0.01, 0.01, N)

THETA = np.zeros(3)
THETA[0] = 1
THETA[1] = 1
THETA[2] = 1
FI = np.zeros((N,3))
FI[0] = [U[0], 0, 0]
FI[1] = [U[1], U[0], 0]
FI[2] = [U[2], U[1], U[0]]
for n in range(3, N):
    FI[n] = [U[n], U[n-1], U[n-2]]

Y = np.zeros(N)
for n in range(N):
    Y[n] = np.matmul(np.transpose(FI[n]), THETA) + Z[n]

pl.title("Plot Y")
pl.plot(np.linspace(0,1,N),Y)
pl.show()

pl.title("Histogram U")
pl.hist(U, bins=100, color='g', edgecolor='black')
pl.show()
lambda_ = 1

P = np.zeros((N,3,3))
P[0] = np.diag((10**3,10**3,10**3))
for n in range(1, N):
    a1 = np.matmul(P[n-1], FI[n])
    a2 = np.matmul(np.transpose(FI[n]), P[n-1])
    var_A = np.matmul(a1, a2)
    var_C = np.matmul(np.transpose(FI[n]), P[n-1])
    var_B = lambda_ + np.matmul(var_C, FI[n])

    P[n] = (1/lambda_) * P[n-1] - ( var_A / var_B )


THETA_dash = np.zeros((N,3))
THETA_dash[0] = [0, 0, 0]
for n in range(1, N):
    var_A = Y[n] - np.matmul(np.transpose(FI[n]), THETA_dash[n-1])
    var_B = np.matmul(P[n], FI[n])
    THETA_dash[n] = THETA_dash[n-1] + var_B * var_A

print(THETA)
print(THETA_dash)
pl.title("Plot Estimation of Theta")
pl.plot(np.linspace(0,N,N),THETA_dash)
pl.show()
