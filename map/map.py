#!/usr/bin/env python

import json
import math
import numpy as np
import pylab as pl
import matplotlib


class Point:
    def __init__(self, _coord1, _coord2, _is_cart=True):
        if _is_cart:
            self.x = _coord1
            self.y = _coord2
            self.rho, self.phi = cart2pol(_coord1, _coord2)
        else:
            self.rho = _coord1
            self.phi = _coord2
            self.x, self.y = pol2cart(_coord1, _coord2)


def tangent_angle(_tan_fi):
    return np.arctan(_tan_fi) * 180 / np.pi


def angle_between_straights_lines(_a1, _a2):
    if 1 + _a1 * _a2 == 0:
        return 90
    return tangent_angle(np.abs((_a1 - _a2) / (1 + _a1 * _a2)))


def coefficients_straight_line_coord(_x1, _y1, _x2, _y2):
    _a = (_y1 - _y2) / (_x1 - _x2)
    _b = _y1 - _a * _x1
    return _a, _b


def coefficients_straight_line(_p1, _p2):
    return coefficients_straight_line_coord(_p1.x, _p1.y, _p2.x, _p2.y)


def linear_equation(_a, _b, _x):
    return _a * _x + _b


def angle_between_3_points(_p1, _p2, _p3):
    _a1, _ = coefficients_straight_line(_p1, _p2)
    _a2, _ = coefficients_straight_line(_p2, _p3)
    return angle_between_straights_lines(_a1, _a2)


def cart2pol(_x, _y):
    _rho = np.sqrt(_x**2 + _y**2)
    _phi = np.arctan2(_y, _x)
    _phi = math.degrees(_phi)
    return _rho, _phi


def pol2cart(_rho, _phi):
    _theta = math.radians(_phi)
    _x = _rho * np.cos(_theta)
    _y = _rho * np.sin(_theta)
    return _x, _y


def load_data_from_file(_path):
    _file = open(_path)
    _data = json.load(_file)
    _file.close()
    return _data


def parse_laser_data(_data):
    _phi = (np.pi / len(_data)) * np.arange(0, len(_data))
    _new_data = []
    for _i in range(len(_data)):
        if not _data[_i] == float('inf') and not np.isnan(_data[_i]):
            _new_data.append(Point(_data[_i], _phi[_i], False))
    return _new_data


def plot_laser_data(_data, _is_cart=True, _settings='rx'):
    if _is_cart:
        for _i in range(len(_data)):
            pl.plot(_data[_i].x, _data[_i].y, _settings)
    else:
        _ax = pl.subplot(111, projection='polar')
        for _i in range(len(_data)):
            _ax.plot(_data[_i].phi, _data[_i].rho, _settings)


def linear_equation_from_2points(_p1, _p2):
    _a, _b = coefficients_straight_line(_p1, _p2)
    return linear_equation(_a, _b, np.linspace(-5, 5))


def simple_edge_finder(_data, _limit_angle):
    _edge_data = []
    for _i in range(len(_data) - 2):
        _p1 = _data[_i]
        _p2 = _data[_i + 1]
        _p3 = _data[_i + 2]
        _angle = angle_between_3_points(_p1, _p2, _p3)
        if _angle > _limit_angle:
            #_edge_data.append(_p1)
            _edge_data.append(_p2)
            #_edge_data.append(_p3)
    return _edge_data


def plot_angle_between_3points(_p1, _p2, _p3):
    _y1 = linear_equation_from_2points(_p1, _p2)
    _y2 = linear_equation_from_2points(_p2, _p3)
    _angle = angle_between_3_points(_p1, _p2, _p3)

    print("p1.x: ", _p1.x, 'p1.y: ', _p1.y)
    print("p2.x: ", _p2.x, 'p2.y: ', _p2.y)
    print("p3.x: ", _p3.x, 'p3.y: ', _p3.y)
    print('angle: ', _angle)

    pl.plot(_p1.x, _p1.y, 'rx')
    pl.plot(_p2.x, _p2.y, 'rx')
    pl.plot(_p3.x, _p3.y, 'rx')
    pl.plot(np.linspace(-5, 5), _y1, 'g')
    pl.plot(np.linspace(-5, 5), _y2, 'b')


# Load data
path = r'map_boxes_0.json'
data = load_data_from_file(path)

time = []
pose = []
scan = []
for i in range(len(data)):
    time.append(data[i]['time'])
    pose.append(data[i]['pose'])  # x[m], y[m], z[degrees]
    scan.append(data[i]['scan'])  # 512 x rho

# Method presentation
scan = parse_laser_data(scan[0])
edge_data = simple_edge_finder(scan, 45)
plot_laser_data(scan, _settings='rx')
plot_laser_data(edge_data, _settings='gx')
pl.grid(True)
pl.show()

matrix = np.zeros((5340, 1500))
for i in range(len(scan)):
    x = int(scan[i].x * 1000)
    y = int(scan[i].y * 10000)
    matrix[x][y] = 1

fig, ax = pl.subplots(1)
p = ax.pcolormesh(matrix)
pl.show()
