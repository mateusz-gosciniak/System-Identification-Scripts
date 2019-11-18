import numpy as np
import pylab as pl

def mi(x):
    return x**2

def LSM(_Y, _FI_T):
    _FI = np.transpose(_FI_T)
    a = np.matmul(_FI_T, _FI)
    a = np.linalg.inv(a)
    b = np.matmul(_FI_T, _Y)
    return np.matmul(a,b)

N = 10**5
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

fi = np.zeros((6,N))

fi[0,0] = np.cos(U[0])
fi[1,0] = mi(U[0])
fi[2,0] = 0
fi[3,0] = 0
fi[4,0] = 0
fi[5,0] = 0

fi[0,1] = np.cos(U[1])
fi[1,1] = mi(U[1])
fi[2,1] = np.cos(U[0])
fi[3,1] = mi(U[0])
fi[4,1] = 0
fi[5,1] = 0

for n in range(2,N):
    fi[0,n] = np.cos(U[n])
    fi[1,n] = mi(U[n])
    fi[2,n] = np.cos(U[n-1])
    fi[3,n] = mi(U[n-1])
    fi[4,n] = np.cos(U[n-2])
    fi[5,n] = mi(U[n-2])


Theta_dash = LSM(Y,fi)
print("Estimation of Gamma parameters: ")
print(Theta_dash[1],Theta_dash[3],Theta_dash[5])
