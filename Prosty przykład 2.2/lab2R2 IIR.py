import numpy as np
import pylab as pl

def f_kernel(x):
    if -np.sqrt(3) < x < np.sqrt(3):
        return x
    else:
        return 0


def gamma(i):
    return 0.5**i

N = 1000
t = np.linspace(0,100,N)

U = np.zeros(N)
for i in range(N):
    U[i] = gamma(i)

E = np.random.uniform(-0.01,0.01,N)

V = np.zeros(N)
V[0] = 0
for k in range(1,N):
    V[k] = 0.5 * V[k-1] + U[k]

Y = V + E

pl.title("V i Y")
pl.grid()
pl.plot(t, V)
pl.plot(t, Y)
pl.show()

f_u = np.zeros(N)
f_u.fill(1)
kernel = np.zeros(N)
for i in range(N):
    kernel[i] = f_kernel(f_u[i])

pl.title("Kernel")
pl.grid()
pl.plot(np.linspace(-3,3,N), kernel)
pl.show()