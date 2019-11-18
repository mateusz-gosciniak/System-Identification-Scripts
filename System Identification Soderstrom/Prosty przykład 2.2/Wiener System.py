import numpy as np
import pylab as pl

def mi(x):
    N = len(x)
    y = np.zeros(N)
    for i in range(N):
        y[i] = np.sin(x[i])
    return y

N = 10**3
U = np.random.uniform(-1,1,N)
X = np.zeros(N)
for k in range(1,N):
    X[k] = U[k] - U[k-1]

t = np.linspace(0, 100, N)
V = mi(X)
Z = np.random.uniform(-0.01, 0.01, N)
Y = V + Z

pl.title("mu function")
pl.plot(np.linspace(-2.1, 2.1, 100), mi(np.linspace(-2.1, 2.1, 100)))
pl.show()

pl.title("Histogram of U")
pl.hist(U, bins=100, color='g', edgecolor='black')
pl.show()

pl.title("Histogram of X")
pl.hist(X, bins=100, color='g', edgecolor='black')
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
pl.plot(t, Y)
pl.show()

pl.title("Histogram of Y")
pl.hist(Y, bins=100, color='g', edgecolor='black')
pl.show()

FI = np.zeros((N, 2))
FI[0,0] = U[0]
FI[0,1] = 0
for k in range(1, N):
    FI[k,0] = U[k]
    FI[k,1] = U[k-1]

h = 1/np.sqrt(N)

def epanechnikov_kernel(u):
    return 3/4 * (1 - u**2)

xx = np.linspace(-N/2,N/2,N)
epanechnikov_kernel_x = np.zeros(N)
for i in range(N):
    epanechnikov_kernel_x[i] = epanechnikov_kernel(xx[i])
pl.title("Epanechnikov Kernel")
pl.plot(xx, epanechnikov_kernel_x)
pl.show()

SUM_A = 0
for k in range(N):
    FI_k = np.array([FI[k,0],FI[k,1]])[np.newaxis]
    K = epanechnikov_kernel( np.max(FI_k) / h )
    SUM_A += np.outer(FI_k, FI_k.T) * K
SUM_A = np.transpose(SUM_A)

SUM_B = 0
for k in range(N):
    FI_k = np.array([FI[k,0],FI[k,1]])[np.newaxis]
    K = epanechnikov_kernel( np.max(FI_k) / h )
    SUM_B += np.outer(FI_k, Y[k]) * K

Gamma_estimation = np.matmul(SUM_A, SUM_B)

print("Gamma estimation: ", Gamma_estimation)

Xk = np.zeros(N)
for k in range(N):
    Xk[k] = Gamma_estimation[0] * U[k] + Gamma_estimation[1] * U[k-1]

pl.title("Histogram of estimation of X")
pl.hist(Xk, bins=100, color='g', edgecolor='black')
pl.show()

pl.title("Plot of estimation of X")
pl.plot(np.linspace(0,N,N), X)
pl.show()

mu_dash = np.zeros(N)
for x in range(N):
    SUM_A = 0
    for k in range(N):
        SUM_A += Y[k] * epanechnikov_kernel( Xk[k] - X[x] / h )

    SUM_B = 0
    for k in range(N):
        SUM_B += epanechnikov_kernel( Xk[k] - X[x] / h )

    mu_dash[x] = SUM_A/SUM_B 

pl.title("Plot of estimation of mu function")
pl.plot(np.linspace(0,N,N), mu_dash)
pl.show()

pl.title("Histogram of estimation of mu")
pl.hist(mu_dash, bins=100, color='g', edgecolor='black')
pl.show()