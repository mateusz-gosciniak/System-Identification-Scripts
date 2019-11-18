import numpy as np
import pylab as pl


def m_single(_x):
    if -2 < _x < 2:
        return -0.5 * _x**2 + 1
    else:
        return 0


def m(_x):
    _y = []
    for _i in range(len(_x)):
        if -2 <= _x[_i] <= 2:
            _y.append(-0.5 * _x[_i] ** 2 + 1)
        else:
            _y.append(0)
    return _y


def even_function(_x):
    _y = []
    for _i in range(len(_x)):
        if -2 < _x[_i] < 0:
            _y.append(np.abs(_x[_i]) * -1 + 1)
        elif 0 < _x[_i] < 2:
            _y.append(_x[_i] * -1 + 1)
        else:
            _y.append(0)
    return _y


N = 1000
sigma = 1

x_axis = np.linspace(-3, 3, N)

even_function_x = even_function(x_axis)
real_Y = m(x_axis)

random_x = np.random.normal(0, sigma, N)
Xn = even_function(even_function_x)
Zn = np.random.normal(0, sigma, N)
Yn = m(Xn) + Zn

pl.plot(x_axis, real_Y, 'r')
pl.plot(x_axis, Xn, 'rx')
#pl.plot(x_axis, Zn, 'gx')
#pl.plot(x_axis, Yn, 'bx')

pl.show()
