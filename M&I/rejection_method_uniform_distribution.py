import numpy as np
import pylab as pl


def half_circle(_x, _a, _b, _r):
    _val = _r ** 2 - (_x - _a) ** 2
    if _val > 0:
        return np.sqrt(_val) + _b


def f(_x):
    _y = []
    for _i in range(len(_x)):
        _y.append(f_single(_x[_i]))
    return _y


def g(_x):
    _y = []
    for _i in range(len(_x)):
        _y.append(g_single(_x[_i]))
    return _y


def cg(_x, _c):
    _y = []
    for _i in range(len(_x)):
        _y.append(_c * g_single(_x[_i]))
    return _y


def f_single(_x):
    return -1/9 * np.abs(_x) + 1/3
    # return half_circle(_x, 1, 0, 1)


def g_single(_x):
    return 1/6
    # return np.pi / 4


N = 100000

# x = np.linspace(0, 2, N)
# X = np.random.uniform(0, 2, N)
# u = np.random.uniform(0, 1, N)
# c = 4 / np.pi

x = np.linspace(-3, 3, N)
X = np.random.uniform(0, 1, N) * 6 - 3
u = np.random.uniform(0, 1, N)
c = 6

good_Y = []
good_X = []
bad_Y = []
bad_X = []
for i in range(N):
    # if c * g_single(X[i]) * u[i] <= f_single(X[i]):
    if u[i] <= f_single(X[i]):
        good_X.append(X[i])
        good_Y.append(u[i])
    else:
        bad_X.append(X[i])
        bad_Y.append(u[i])
pl.plot(good_X, good_Y, 'b.')
pl.plot(bad_X, bad_Y, 'r.')
# pl.show()

pl.plot(x, f(x), 'r')
pl.plot(x, g(x), 'g')
pl.plot(x, cg(x, c), 'b')
pl.show()


# pl.hist(good_X, 100, color='g', edgecolor='black')
# pl.show()
