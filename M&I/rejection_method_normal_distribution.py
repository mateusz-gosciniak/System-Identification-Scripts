import numpy as np
import pylab as pl
import datetime


def g_single(_x):
    return 0.5 * np.exp(-np.abs(_x))
    # return 1/8 #  opt 1


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
    return np.exp(-_x ** 2 / 2) / np.sqrt(2 * np.pi)


def f(_x):
    _y = []
    for _i in range(len(_x)):
        _y.append(f_single(_x[_i]))
    return _y

# ----------------------------


def sawtooth_x(_x):
    return sawtooth(_x + 0.0000001, 0.1, 1, 0)


def sawtooth(_x, _t, _a=1, _phy=0):
    _x = _x/_t + _phy
    return _a * (_x - np.floor(_x))


def reverse_cdf_exponential_function_u(_u):
    return -(np.log(abs(_u)))


def reverse_cdf_exponential_function(_u):
    _x = []
    for _i in range(len(_u)):
        _x.append(reverse_cdf_exponential_function_u(_u[_i]))
    return _x


def get_seed():
    _current_second = float(str(datetime.datetime.now()).split(':')[2])
    _seed = _current_second * np.e / np.pi
    return _seed


def exponential_function_random_generator(_seed, _n):
    _random_numbers = []
    e = np.random.uniform(0, 1, _n)

    _random_value = reverse_cdf_exponential_function_u(sawtooth_x(_seed))
    if e[0] > 0.5:
        _random_value = -_random_value
    for _i in range(_n - 1):
        _random_numbers.append(_random_value)
        _random_value = reverse_cdf_exponential_function_u(sawtooth_x(_random_numbers[_i]))
        if e[_i] > 0.5:
            _random_value = -_random_value

    _random_numbers.append(_random_value)
    return _random_numbers

# ----------------------------


N = 10**6
x = np.linspace(-4, 4, N)
X = np.random.uniform(0, 8, N) - 4
u = np.random.uniform(0, 1, N) # opt 1
# u = exponential_function_random_generator(get_seed(), N)
# c = 3.2  # opt 1
c = 2

good_Y = []
good_X = []
# bad_Y = []
# bad_X = []
for i in range(N):
    if u[i] > 0:
        # if c * g_single(X[i]) * u[i] <= f_single(X[i]):
        if u[i] <= f_single(X[i]):
            good_X.append(X[i])
            good_Y.append(u[i])
        # else:
        #     bad_X.append(X[i])
        #     bad_Y.append(u[i])
pl.plot(good_X, good_Y, 'b.')
# pl.plot(bad_X, bad_Y, 'r.')

pl.plot(x, f(x), 'r')
pl.plot(x, g(x), 'g')
pl.plot(x, cg(x, c), 'b')
pl.show()

pl.hist(good_X, 100, color='g', edgecolor='black')
pl.show()
