import numpy as np
import pylab as pl
import datetime


def f(_x):
    return sawtooth(_x + 0.0000001, 0.1, 1, 0)


def sawtooth(_x, _t, _a=1, _phy=0):
    _x = _x/_t + _phy
    return _a * (_x - np.floor(_x))


def triangular_function_x(_x):
    if _x <= -2:
        return 0
    elif _x >= 2:
        return 0
    elif -2 < _x <= 0:
        return _x/4 + 0.5
    elif 0 <= _x < 2:
        return -_x/4 + 0.5


def reverse_cdf_triangular_function_u(_u):
    if _u < 0:
        return 0
    elif 0 <= _u <= 0.5:
        return -2 + 4 * np.sqrt(_u * 0.5)
    elif 0.5 <= _u <= 1:
        return 2 + -4 * np.sqrt(0.5 - _u / 2)
    elif _u > 1:
        return 1


def triangular_function(_x):
    _y = []
    for _i in range(len(_x)):
        if _x[_i] <= -2:
            _y.append(0)
        elif _x[_i] >= 2:
            _y.append(0)
        elif -2 < _x[_i] <= 0:
            _y.append(_x[_i] / 4 + 0.5)
        elif 0 <= _x[_i] < 2:
            _y.append(-_x[_i] / 4 + 0.5)
    return _y


def cdf_triangular_function(_x):
    _y = []
    for _i in range(len(_x)):
        if _x[_i] <= -2:
            _y.append(0)
        elif _x[_i] >= 2:
            _y.append(1)
        elif -2 < _x[_i] <= 0:
            _y.append(_x[_i]**2 / 8 + _x[_i]/2 + 0.5)
        elif 0 <= _x[_i] < 2:
            _y.append(-_x[_i]**2 / 8 + _x[_i]/2 + 0.5)
    return _y


def reverse_cdf_triangular_function(_u):
    _x = []
    for _i in range(len(_u)):
        if _u[_i] < 0:
            _x.append(0)
        elif 0 <= _u[_i] <= 0.5:
            _x.append(-2 + 4 * np.sqrt(_u[_i] * 0.5))
        elif 0.5 <= _u[_i] <= 1:
            _x.append(2 + -4 * np.sqrt(0.5 - _u[_i]/2))
        elif _u[_i] > 1:
            _x.append(1)
    return _x


def get_seed():
    _current_second = float(str(datetime.datetime.now()).split(':')[2])
    _seed = _current_second * np.e / np.pi
    return _seed


def random_generator(_seed, _n):
    _random_numbers = []
    _random_value = reverse_cdf_triangular_function_u(f(_seed))
    for _i in range(_n - 1):
        _random_numbers.append(_random_value)
        _random_value = reverse_cdf_triangular_function_u(f(_random_numbers[_i]))

    _random_numbers.append(_random_value)
    return _random_numbers


# -------------------------------------


N = 1000000
x = np.linspace(-2, 2, N)
x_N = np.linspace(0, N, N)

pdf = triangular_function(x)
cdf = cdf_triangular_function(x)
cdf_reverse = reverse_cdf_triangular_function(x)

random_x = random_generator(get_seed(), N)
sorted_x = np.sort(random_x)

pl.plot(x, pdf)
pl.grid(True)
pl.show()
pl.plot(x, cdf)
pl.grid(True)
pl.show()
pl.plot(x, cdf_reverse)
pl.axis([0, 1, -2, 2])
pl.grid(True)
pl.show()

# Plot random numbers
pl.plot(x_N, random_x, 'xb')
pl.show()

# Plot sort random numbers
pl.plot(x_N, sorted_x, 'r')
pl.show()

# Plot histogram
pl.hist(random_x, 100, color='g', edgecolor='black')
pl.grid(True)
pl.show()
