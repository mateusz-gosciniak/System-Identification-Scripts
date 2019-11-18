import numpy as np
import pylab as pl

N = 10**5
G_size = 5
axis_x = np.linspace(0,10,N)

### MODELING

U = np.random.uniform(-np.sqrt(3), np.sqrt(3), N)
#U = np.random.normal(size=N) # for gauss distribution
EV_U = np.sum(U)/len(U)
Var_U = np.var(U)

print("Expected Value if U: " + str(EV_U))
print("Variance of U: " + str(Var_U))
pl.title("Histogram of U")
pl.hist(U, bins=100, color='g', edgecolor='black')
pl.show()

E = np.random.uniform(-0.01, 0.01, N)

pl.title("Histogram of E")
pl.hist(E, bins=100, color='g', edgecolor='black')
pl.show()

V = np.zeros(N)
V[0] = 1
for k in range(1, N):
    V[k] = 0.5*V[k-1] + U[k]
Y = V + E

pl.title("Y")
pl.plot(axis_x, Y)
pl.show()

pl.title("Histogram of Y")
pl.hist(Y, bins=100, color='g', edgecolor='black')
pl.show()

### IDENTIFICATION

G = np.zeros(G_size) # gamma dash - estimation of gamma
for i in range(G_size):
    SUM_UY = 0
    for k in range(1, N-i):
        SUM_UY += U[k] * Y[k+i]
    G[i] = SUM_UY / (N-i)

print("Gamma dash: " + str(G))

Y_dash = np.zeros(N) # Y dash - estimation of Y
for k in range(N):
    SUM_GU = 0
    for i in range(G_size):
        SUM_GU += G[i] * U[k-1]
    Y_dash[k] = SUM_GU

pl.title("Estimation of Y")
pl.plot(axis_x, Y_dash)
pl.show()

pl.title("Histogram of Estimation Y")
pl.hist(Y_dash, bins=100, color='g', edgecolor='black')
pl.show()
