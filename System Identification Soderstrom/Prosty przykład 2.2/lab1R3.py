import numpy as np
import pylab as pl

def mi(x):
    return x**2

def triangular_kernel(u):
    return 1 - np.abs(u)

def epanechnikov_kernel(u):
    return 3/4 * (1 - u**2)

N = 10**4
x = np.linspace(-N/2,N/2,N)
h = 1/np.sqrt(N) # bandwidth parameter

U = np.random.uniform(0,1,N)
W = np.zeros(N)
for n in range(N):
    W[n] = mi(U[n])
V = np.zeros(N)
for n in range(N):
    V[n] = 3 * W[n] + 2 * W[n-1] + 1 * W[n-2]
Z = np.random.uniform(-0.01,0.01,N)
Y = V + Z

pl.title("Histogram of U")
pl.hist(U, 100, color='g', edgecolor='black')
pl.show()

pl.title("Histogram of W")
pl.hist(W, 100, color='g', edgecolor='black')
pl.show()

pl.title("Histogram of Z")
pl.hist(Z, 100, color='g', edgecolor='black')
pl.show()

pl.title("Plot of V")
pl.plot(x,V)
pl.show()

pl.title("Histogram of V")
pl.hist(V, 100, color='g', edgecolor='black')
pl.show()

pl.title("Plot of Y")
pl.plot(x,Y)
pl.show()

pl.title("Histogram of Y")
pl.hist(Y, 100, color='g', edgecolor='black')
pl.show()

epanechnikov_kernel_x = np.zeros(N)
for i in range(N):
    epanechnikov_kernel_x[i] = epanechnikov_kernel(x[i])
pl.title("Epanechnikov Kernel")
pl.plot(x, epanechnikov_kernel_x)
pl.show()

def R(U):
    N = len(U)
    R_vec = np.zeros(N)
    for n in range(N):
        R_vec[n] = 3 * mi(U[n]) + 1
    return R_vec

R_u = R(U)

pl.title("Plot of R with input U")
pl.plot(x, R_u)
pl.show()

R_x = R(x)

pl.title("Plot of R")
pl.plot(x, R_x)
pl.show()

def R_dash(U, Y, h, K):
    N = len(U)
    R_dash_vec = np.zeros(N)
    for k in range(N):
        var_A = 0
        var_B = 0
        for n in range(N):
            delta = U[n] - U[k]
            kernel = K(delta / h)
            var_A += Y[n] * kernel
            var_B += kernel
        R_dash_vec[k] = var_A / var_B
        print("K: = ", k)
    return R_dash_vec

R_dash_u = R_dash(U,Y,h,epanechnikov_kernel)

pl.title("Plot of estimation of R")
pl.plot(x, R_dash_u)
pl.show()


pl.title("Histogram of estimation R")
pl.hist(Y, 100, color='g', edgecolor='black')
pl.show()

mi_dash = np.zeros(N)
for i in range(N):
    mi_dash[i] = R_dash_u[i] - R_dash_u[0]

pl.title("Plot of estimation of mu")
pl.plot(x, mi_dash)
pl.show()

pl.title("Histogram of estimation mu")
pl.hist(Y, 100, color='g', edgecolor='black')
pl.show()

gamma_dash = np.zeros(3)
EY = np.sum(Y)/N
EU = np.sum(U)/N
for tau in range(3):
    sumUY = 0
    for n in range(N-tau):
        sumUY += (U[n] - EU) * (Y[n + tau] - EY)
    gamma_dash[tau] = sumUY/(N - tau)

alpha = 10
print("For parameter alpha equal 10, estimation of gamma:")
print(gamma_dash * alpha)
