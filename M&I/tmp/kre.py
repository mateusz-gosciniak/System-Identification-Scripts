# KERNEL REGRESSION ESTIMATE

import numpy as np
import pylab as pl


def kernel_epanechnikov(_x):
    if np.abs(_x) <= 1:
        return 0.75 - (1 - _x**2)
    return 0


def kernel_triangular(_x):
    if np.abs(_x) <= 1:
        return 1 - np.abs(_x)
    return 0


def kernel_uniform(_x):
    if np.abs(_x) <= 1:
        return 0.5
    return 0


def estimate(_x, _xn, _h, _n, _yn):
    _m_dash = []
    for _j in range(_n):
        _sum_1 = 0
        _sum_2 = 0
        for _i in range(_j+1):
            _sum_1 = _sum_1 + _yn[_i] * kernel_uniform((_x[_j+1] - _xn[_i]) / _h)
            _sum_2 = _sum_2 + kernel_uniform((_x[_j+1] - _xn[_i]) / _h)
        _sum_1 = 1 / ((_j+1) * _h) * _sum_1
        _sum_2 = 1 / ((_j+1) * _h) * _sum_2
        _m_dash.append(_sum_1 / _sum_2)
    return _m_dash


N = 1000
a = 1
sigma = 1
h = 1

x = np.linspace(-3, 3, N)
m = np.arctan(a * x)
Xn = np.random.uniform(-3, 3, N)
Zn = np.random.normal(0, sigma)
Yn = np.arctan(a * Xn) + Zn
# '''
m_dash = estimate(x, Xn, h, N, Yn)

pl.plot(x, m)
pl.plot(x, m_dash)
# '''
'''
k = []
for i in range(N):
    k.append(kernel_uniform(x[i]))

pl.plot(x, k, 'g')

k = []
for i in range(N):
    k.append(kernel_triangular(x[i]))

pl.plot(x, k, 'r')
'''
pl.grid(True)
pl.show()

