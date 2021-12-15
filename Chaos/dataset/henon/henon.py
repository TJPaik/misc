import numpy as np


def henon_next(x, y, a=1.4, b=0.3):
    '''Computes the next step in the Henon
    map for arguments x, y with kwargs a and
    b as constants.
    '''
    x_next = 1 - a * x ** 2 + y
    y_next = b * x
    return x_next, y_next


def henon_data(initial_vertex=(0, 0), n_data=10000, a=1.4, b=0.3):
    data = np.zeros((n_data, 2))
    data[0] = np.asarray(initial_vertex)
    for i in range(n_data - 1):
        data[i + 1] = henon_next(*data[i], a, b)
    return data
