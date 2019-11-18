import numpy as np
import pylab as pl


def system(_x, _z, _l):
    _y = []
    for _n in range(len(_x)):
        _sum = 0
        for _k in range(len(_l)):
            _sum += _l[_k] * _x[_n - _k] + _z[_n]
        _y.append(_sum)
    return _y


def estimate(_xn, _yn, _n, _l, _sigma):
    return np.mean(_xn[_n] * _yn[_n + _l]) / _sigma

N = 1000
x_array = np.linspace(-1, 1, N)
sigma = 1

x_lambda = [0, 1, 2, 3]
Lambda = [1, 2, -1, -2]
Xn = np.random.uniform(-1, 1, N)
Zn = np.random.normal(0, 1, N)
Yn = system(Xn, Zn, Lambda)
Lambda_estimate = [estimate(Xn, Yn, 10, 0, sigma),
                   estimate(Xn, Yn, 10, 1, sigma),
                   estimate(Xn, Yn, 10, 2, sigma),
                   estimate(Xn, Yn, 10, 3, sigma)]
print('Lambda_estimate: ', Lambda_estimate)

pl.plot(x_lambda, Lambda, 'bx')
pl.plot(x_lambda, Lambda_estimate, 'ro')
pl.grid(True)
pl.show()

