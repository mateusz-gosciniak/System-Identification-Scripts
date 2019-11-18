import numpy as np
import pylab as pl


def circle(_a, _b, _r, _n):
    _t = np.linspace(0, 2 * np.pi, _n)
    _x = _a + _r * np.cos(_t)
    _y = _b + _r * np.sin(_t)
    return _x, _y


def rand_circle(_x, _y):
    _x_rand = []
    _y_rand = []
    for _i in range(len(_x)):
        _x_rand.append(_x[_i] + np.random.uniform(-0.15, 0.15))
        _y_rand.append(_y[_i] + np.random.uniform(-0.15, 0.15))
    return _x_rand, _y_rand


def return_s(_x, _y):
    _s = []
    for _i in range(len(_x)):
        _s.append(-(_x[_i] ** 2 + _y[_i] ** 2))
    return _s


N = 100
a = 1
b = 2
r = 1

x_org, y_org = circle(a, b, r, N)
X, Y = rand_circle(x_org, y_org)
S = return_s(X, Y)

n = len(X)
F = np.zeros((n, 3))
for i in range(n):
    F[i, 0] = X[i]
    F[i, 1] = Y[i]
    F[i, 2] = 1

Ft = np.transpose(F)
FtF = np.matmul(Ft, F)
FtS = np.matmul(Ft, S)
A = np.matmul(np.linalg.inv(FtF), FtS)

print('Ftf: ', FtF)
print('Ftf ^ -1: ', FtF ** -1)
print('Ftf ^ -1: ', 1/FtF)

dash_a = A[0] / -2
dash_b = A[1] / -2
dash_r = np.sqrt(-A[2] + dash_a**2 + dash_b**2)

print('dash_a', dash_a)
print('dash_b', dash_b)
print('dash_r', dash_r)

x_dash, y_dash = circle(dash_a, dash_b, dash_r, N)

pl.plot(x_org, y_org, 'r')
pl.plot(X, Y, 'gx')
pl.plot(x_dash, y_dash, 'b')
pl.show()
