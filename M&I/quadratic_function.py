import numpy as np
import pylab as pl
import datetime


def sawtooth(_x, _t, _a=1, _phy=0):
    _x = _x/_t + _phy
    return _a * (_x - np.floor(_x))


def quadratic_function_x(_x):
    if _x < 0:
        return 0
    elif 0 <= _x <= 1:
        return 2 * _x
    elif _x > 1:
        return 0


def reverse_cdf_quadratic_function_x(_x):
    if _x < 0:
        return 0
    elif 0 <= _x <= 1:
        return np.sqrt(_x)
    elif _x > 1:
        return 1


def quadratic_function(_x):
    _y = []
    for _i in range(len(_x)):
        if _x[_i] < 0:
            _y.append(0)
        elif 0 <= _x[_i] <= 1:
            _y.append(2 * _x[_i])
        elif _x[_i] > 1:
            _y.append(0)
    return _y


def cdf_quadratic_function(_x):
    _y = []
    for _i in range(len(_x)):
        if _x[_i] < 0:
            _y.append(0)
        elif 0 <= _x[_i] <= 1:
            _y.append(_x[_i]**2)
        elif _x[_i] > 1:
            _y.append(1)
    return _y


def reverse_cdf_quadratic_function(_x):
    _y = []
    for _i in range(len(_x)):
        if _x[_i] < 0:
            _y.append(0)
        elif 0 <= _x[_i] <= 1:
            _y.append(np.sqrt(_x[_i]))
        elif _x[_i] > 1:
            _y.append(1)
    return _y


def get_seed():
    _current_second = float(str(datetime.datetime.now()).split(':')[2])
    _seed = _current_second * np.e / np.pi
    return _seed


def random_generator(_seed, _n):
    _random_numbers = []
    _random_value = reverse_cdf_quadratic_function_x(f(_seed))
    for _i in range(_n - 1):
        _random_numbers.append(_random_value)
        _random_value = reverse_cdf_quadratic_function_x(f(_random_numbers[_i]))

    _random_numbers.append(_random_value)
    return _random_numbers


def f(_x):
    return sawtooth(_x + 0.0000001, 0.1, 1, 0)


N = 1000
x = np.linspace(0, 1, N)
x_N = np.linspace(0, N, N)

pdf = quadratic_function(x)
cdf = cdf_quadratic_function(x)
cdf_reverse = reverse_cdf_quadratic_function(x)

random_x = random_generator(get_seed(), N)
sorted_x = np.sort(random_x)

pl.plot(x, pdf)
pl.grid(True)
pl.show()
pl.plot(x, cdf)
pl.grid(True)
pl.show()
pl.plot(x, cdf_reverse)
pl.grid(True)
pl.show()

# Plot random numbers
pl.plot(x_N, random_x, 'b')
pl.show()

# Plot sort random numbers
pl.plot(x_N, sorted_x, 'b')
pl.show()

# Plot histogram
pl.hist(random_x, 100, color='g', edgecolor='black')
pl.grid(True)
pl.show()
