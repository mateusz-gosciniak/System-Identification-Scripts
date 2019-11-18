import numpy as np
import pylab as pl
import datetime


def f(_x):
    return sawtooth(_x + 0.0000001, 0.1, 1, 0)


def sawtooth(_x, _t, _a=1, _phy=0):
    _x = _x/_t + _phy
    return _a * (_x - np.floor(_x))


def exponential_function_x(_x):
    return np.exp(-np.abs(_x))


def exponential_function(_x):
    _y = []
    for _i in range(len(_x)):
        _y.append(exponential_function_x(_x[_i]))
    return _y


def cdf_exponential_function_x(_x):
    return np.exp(-np.abs(_x))


def cdf_exponential_function(_x):
    _y = []
    for _i in range(len(_x)):
        _y.append(cdf_exponential_function_x(_x[_i]))
    return _y


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

    _random_value = reverse_cdf_exponential_function_u(f(_seed))
    if e[0] > 0.5:
        _random_value = -_random_value
    for _i in range(_n - 1):
        _random_numbers.append(_random_value)
        _random_value = reverse_cdf_exponential_function_u(f(_random_numbers[_i]))
        if e[_i] > 0.5:
            _random_value = -_random_value

    _random_numbers.append(_random_value)
    return _random_numbers


N = 1000000
x = np.linspace(-7, 7, N)
x_N = np.linspace(0, N, N)

pdf = exponential_function(x)
cdf = cdf_exponential_function(x)
cdf_reverse = reverse_cdf_exponential_function(x)

random_x = exponential_function_random_generator(get_seed(), N)
sorted_x = np.sort(random_x)

pl.plot(x, pdf, 'b')
pl.grid(True)
pl.show()
pl.plot(x, cdf, 'b')
pl.grid(True)
pl.show()
pl.plot(x, cdf_reverse, 'b')
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
