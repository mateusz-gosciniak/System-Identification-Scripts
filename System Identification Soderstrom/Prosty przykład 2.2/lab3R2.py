import numpy as np
import pylab as pl

N = 10**6
axis_x = np.linspace(0,10,N)

### MODELING

U = np.random.uniform(-1,1,N)

pl.title("Histogram of U")
pl.hist(U, bins=100, color='g', edgecolor='black')
pl.show()

E = np.random.uniform(-0.01, 0.01, N)

pl.title("Histogram of E")
pl.hist(E, bins=100, color='g', edgecolor='black')
pl.show()

A = 0.5
B = 1

V = np.zeros(N)
V[0] = 0
for k in range(1, N):
    V[k] = A * V[k-1] + B * U[k]
Y = V + E

pl.title("Y")
pl.plot(axis_x, Y)
pl.show()

pl.title("Histogram of Y")
pl.hist(Y, bins=100, color='g', edgecolor='black')
pl.show()

### IDENTIFICATION
# LEAST SQUARES METHOD

YforFI = Y
YforFI = np.delete(YforFI, -1)
YforFI = np.concatenate((np.zeros(1), YforFI))

FI = np.zeros((N, 2))
for i in range(N):
    FI[i,0] = YforFI[i]
    FI[i,1] = U[i]

FI_T = np.transpose(FI)
vec_a_dash_b_dash = np.matmul(np.matmul(np.linalg.inv(np.matmul(FI_T, FI)), FI_T), Y)
delta = np.linalg.norm([A, B] - vec_a_dash_b_dash)

print("A: " + str(vec_a_dash_b_dash[0]) + " B: " + str(vec_a_dash_b_dash[1]))
print("N: " + str(N) + " delta: " + str(delta))



