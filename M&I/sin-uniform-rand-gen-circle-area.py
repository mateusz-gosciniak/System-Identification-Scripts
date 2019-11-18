import numpy as np
import pylab as pl
import datetime


def f(_x):
    return sin_param(_x, 0, 2 * np.pi * 10, 1, 2)


def sin_param(_x, _x_axis=0, _x_scale=1, _y_axis=0, _y_scale=1):
    return (np.sin((_x + _x_axis) * _x_scale) + _y_axis) / _y_scale


def sin_random_generator(_seed, _n):
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


def get_point_in_circle(_set_x, _set_y, _r, _a, _b):
    _x_in_circle = []
    _y_in_circle = []
    for i in range(len(_set_x)):
        _c = np.sqrt(abs(_set_x[i] - _a)**2 + abs(_set_y[i] - _b)**2)
        if _c <= _r:
            _x_in_circle.append(_set_x[i])
            _y_in_circle.append(_set_y[i])
    return _x_in_circle, _y_in_circle


def get_error_chart(_n, _r, _a, _b, _plot=False):
    _rand_y = sin_random_generator(get_seed(), _n)
    _rand_x = sin_random_generator(get_seed(), _n)
    _x_in_circle, _y_in_circle = get_point_in_circle(_rand_x, _rand_y, _r, _a, _b)
    _number_of_points_in_circle = len(_x_in_circle)
    _real_area = np.pi * _r**2
    _estimated_area = _number_of_points_in_circle / _n
    _error = np.abs(100 - _estimated_area / _real_area * 100)
    if _plot:
        _t = np.linspace(0, 2 * np.pi)
        _x = _a + _r * np.cos(_t)
        _y = _b + _r * np.sin(_t)

        pl.plot(_rand_x, _rand_y, '.g')
        pl.plot(_x_in_circle, _y_in_circle, '.b')
        pl.plot(_x, _y, 'r')
        pl.grid(True)
        pl.show()
    return _error, _estimated_area, _real_area, _number_of_points_in_circle


N = 10000
r = 0.5
a = 0.5
b = 0.5

# Plot - wartości rosnące
# matrix = [100, 175, 250, 375, 500, 750, 1000, 1750, 2500, 3750, 5000, 7500, 10000, 17500, 25000, 37500, 50000, 75000, 100000]
# tab = []
# for i in range(len(matrix)):
#     error, estimated_area, real_area, number_of_points_in_circle = get_error_chart(N, r, a, b)
#     tab.append(error)
# pl.semilogx(matrix, tab, 'r')
# pl.show()

# Plot - wartości stałe
# tab = []
# for i in range(100):
#     error, estimated_area, real_area, number_of_points_in_circle = get_error_chart(N, r, a, b)
#     tab.append(error)
# pl.plot(tab, 'r')
# pl.show()

error, estimated_area, real_area, number_of_points_in_circle = get_error_chart(N, r, a, b, _plot=True)
print('Points: ', N)
print('Points in circle: ', number_of_points_in_circle)
print('estimated area: ', estimated_area)
print('real area: ', real_area)
print('error: ', error, '%')
