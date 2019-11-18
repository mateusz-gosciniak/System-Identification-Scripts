import numpy as np
import pylab as pl

# Orthogonal base
def fi(x, i):
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

# Parameters
N = 4000 # Number of Samples
K = 22 # Parametr K
n = 10000 # Quality of Axis X
x = np.linspace(-1.3,1.3,n) # Axis X
X = np.random.triangular(left=-1,mode=0,right=1,size=N) # Samples

#pl.title("Random X with triangle distribution")
#pl.plot(x, X)
#pl.show()

#pl.title("Sorted Random X with triangle distribution")
#pl.plot(x, np.sort(X))
#pl.show()

#pl.title("Histogram of Random X with triangle distribution")
#pl.hist(X, 100, color='g', edgecolor='black')
#pl.show()

alfa = 0
n = 100
index = 0
x = np.linspace(-1.3,1.3,n) # Axis X

f = np.zeros(n)
for i in x:
    alfa = 0
    for j in range(K):
        suma = 0
        for g in range(N):
            suma = suma + fi(X[g],j)
        alfa = suma/N
        f[index] = f[index] + alfa * fi(i,j)
    index = index + 1
    print(i)

f_original = np.zeros(n)
for i in range(n):
    f_original[i] = triangular_function_x(x[i])

pl.title("N="+str(N)+" K="+str(K))
pl.grid()
pl.plot(x, f)
pl.plot(x, f_original)
pl.show()
