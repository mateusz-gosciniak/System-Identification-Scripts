import numpy as np
import pylab as pl
import datetime


def f(_x):
    return sawtooth(_x + 0.0000001, 0.1, 1, 0)


def sawtooth(_x, _t, _a=1, _phy=0):
    _x = _x/_t + _phy
    return _a * (_x - np.floor(_x))


def sawtooth_random_generator(_seed, _n):
    _random_numbers = []
    _random_value = f(_seed)
    for _i in range(_n - 1):
        _random_numbers.append(_random_value)
        _random_value = f(_random_numbers[_i])

    _random_numbers.append(_random_value)
    return _random_numbers


def get_seed():
    _current_second = float(str(datetime.datetime.now()).split(':')[2])
    _seed = _current_second * np.e / np.pi
    return _seed


N = 1000000
x = np.linspace(0, 1, N)

org_sawtooth = f(x)
random_x = sawtooth_random_generator(get_seed(), N)

x_N = np.linspace(0, N, N)
sorted_x = np.sort(random_x)
# fft_x = np.fft.fft(random_x)

# Plot sin
# pl.plot(x, org_sawtooth, 'r')
# pl.plot(x, random_x, 'xg')
# pl.grid(True)
# pl.show()

# Plot fft random numbers
# pl.plot(x[1:], fft_x[1:])
# pl.show()

# Plot random numbers
# pl.plot(x_N, random_x, 'bx')
# pl.show()

# Plot sort random numbers
pl.plot(x_N, sorted_x, 'b')
pl.show()

# Plot histogram
pl.hist(random_x, 100, color='g', edgecolor='black')
pl.grid(True)
pl.show()

# Plot numpy uniform random generator
# numpy_random_x = np.random.uniform(0, 1, N)
# pl.hist(numpy_random_x, 100, color='g', edgecolor='black')
# pl.grid(True)
# pl.show()
