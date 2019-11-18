import numpy as np
import pylab as pl

# Orthogonal base
def fi(i, x):
    value = 0
    if i == 1:
        value = 1 / np.sqrt(2)
    elif i != 1:
        if np.mod(i,2) == 0:
            value = np.cos(i/2 * np.pi * x)
        elif np.mod(i,2) == 1:
            value = np.sin((i-1)/2 * np.pi * x)
    if -1 < value < 1:
        return value
    else:
        return 0

# PDF
def triangular_function_x(_x):
    if _x < -1:
        return 0
    elif _x > 1:
        return 0
    elif -1 < _x <= 0:
        return _x + 1
    elif 0 <= _x < 1:
        return -_x + 1


N = 10**6
S = 20

#X = np.random.triangular(-1,0,1,N)
X = np.random.rand(N) - np.random.rand(N)
x = np.linspace(-1.3,1.3,N)

#pl.title("Random X with triangle distribution")
#pl.plot(x, X)
#pl.show()

#pl.title("Sorted Random X with triangle distribution")
#pl.plot(x, np.sort(X))
#pl.show()

#pl.title("Histogram of Random X with triangle distribution")
#pl.hist(X, 100, color='g', edgecolor='black')
#pl.show()

alfa = np.zeros(N)
for i in range(S):
    for j in range(N):
        alfa[i] += fi(i,X[j])
    alfa[i] = alfa[i]/N


f = np.zeros(N)
for j in range(N):
    for i in range(S):
        f[j] += alfa[i] * fi(i,x[j])


f_original = np.zeros(N)
for i in range(N):
    f_original[i] = triangular_function_x(x[i])

pl.title("N="+str(N)+" S="+str(S))
pl.grid()
pl.plot(x, f)
pl.plot(x, f_original)
pl.show()



