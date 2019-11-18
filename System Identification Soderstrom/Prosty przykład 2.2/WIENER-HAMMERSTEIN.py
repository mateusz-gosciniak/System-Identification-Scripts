import numpy as np
import pylab as pl

def mi(x):
    return np.arctan(x)

def epanechnikov_kernel(u):
    return 3/4 * (1 - u**2)

# SIMULATION

N = 10**3
U = np.random.normal(size=N)
X = np.zeros(N)
for n in range(N):
    X[n] = 1 * U[n] + 1 * U[n-1]
W = np.zeros(N)
for n in range(N):
    W[n] = mi(X[n])
V = np.zeros(N)
for n in range(N):
    V[n] = 2 * W[n] + 1 * W[n-1]
Z = np.random.uniform(-0.01,0.01,N)
Y = Z + V

# PLOT SIMULATION

x = np.linspace(-10,10,N)
y = np.zeros(N)
for n in range(N):
    y[n] = mi(x[n])

xx = np.linspace(-N/2,N/2,N)
epanechnikov_kernel_x = np.zeros(N)
for i in range(N):
    epanechnikov_kernel_x[i] = epanechnikov_kernel(xx[i])

pl.title("Epanechnikov Kernel")
pl.plot(xx, epanechnikov_kernel_x)
pl.show()

pl.title("mu function")
pl.plot(np.linspace(-2.1, 2.1, 100), mi(np.linspace(-2.1, 2.1, 100)))
pl.show()

pl.title("Histogram of U")
pl.hist(U, bins=100, color='g', edgecolor='black')
pl.show()

pl.title("Histogram of X")
pl.hist(X, bins=100, color='g', edgecolor='black')
pl.show()

pl.title("Plot of W")
pl.plot(np.linspace(0,N,N), W)
pl.show()

pl.title("Histogram of W")
pl.hist(W, bins=100, color='g', edgecolor='black')
pl.show()

pl.title("Plot of V")
pl.plot(np.linspace(0,N,N), V)
pl.show()

pl.title("Histogram of V")
pl.hist(V, bins=100, color='g', edgecolor='black')
pl.show()

pl.title("Histogram of Z")
pl.hist(Z, bins=100, color='g', edgecolor='black')
pl.show()

pl.title("Output Y function")
pl.plot(np.linspace(0,N,N), Y)
pl.show()

pl.title("Histogram of Y")
pl.hist(Y, bins=100, color='g', edgecolor='black')
pl.show()

# IDENTIFICATION

def delta(u):
    return np.max(u)

h = 1/np.sqrt(N)

mu_dash = np.zeros(N)
for x in range(N):
    SUM_A = 0
    SUM_B = 0
    for k in range(N):
        SUM_A += Y[k] * epanechnikov_kernel( delta(U[x]) / h )
        SUM_B += epanechnikov_kernel( delta(U[x]) / h )

    mu_dash[x] = SUM_A/SUM_B 

pl.title("Estimation of mu function")
pl.plot(np.linspace(0,N,N), mu_dash)
pl.show()

FI = np.zeros((N, 2))
FI[0,0] = U[0]
FI[0,1] = 0
for k in range(1, N):
    FI[k,0] = U[k]
    FI[k,1] = U[k-1]

SUM_A = 0
for k in range(N):
    FI_k = np.array([FI[k,0],FI[k,1]])[np.newaxis]
    K = epanechnikov_kernel( np.max(FI_k) / h )
    SUM_A += np.outer(FI_k, FI_k.T) * K
SUM_A = np.transpose(SUM_A/N)

SUM_B = 0
for k in range(N):
    FI_k = np.array([FI[k,0],FI[k,1]])[np.newaxis]
    K = epanechnikov_kernel( np.max(FI_k) / h )
    SUM_B += np.outer(FI_k, Y[k]) * K

Kappa = np.matmul(SUM_A, SUM_B)

print("Kappa: ", Kappa)