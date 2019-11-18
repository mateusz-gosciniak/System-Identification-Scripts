import numpy as np
import pylab as pl
from scipy.stats import norm


def kernel_uniform(_x):
    if np.abs(_x) <= 1:
        return 0.5
    return 0


def kernel(_x):
    if -0.5 <= _x <= 0.5:
        return 1
    return 0


N = 1000
h = 1
x = np.linspace(-4, 4, N)
y = norm.pdf(x)
xn = np.random.randn(N)

# print('x: ', x)
# print('xn: ', xn)

result = []
for j in range(N):
    _sum = 0
    for i in range(j):
        # print('j: ', j, '; i: ', i)
        # print('x[j]: ', x[j])
        # print('xn[i]: ', xn[i])
        _sum = _sum + kernel_uniform((x[j] - xn[i]) / h)

    # print('_sum: ', _sum)
    result.append((1 / ((j+1) * h)) * _sum)

pl.plot(x, result, 'r')
pl.plot(x, y, 'b')
pl.grid(True)
pl.show()
