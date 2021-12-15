import numpy as np


def lorenz(x, y, z, s=10, r=28, b=2.667):
    """
    Given:
       x, y, z: a point of interest in three dimensional space
       s, r, b: parameters defining the lorenz attractor
    Returns:
       x_dot, y_dot, z_dot: values of the lorenz attractor's partial
           derivatives at the point x, y, z
    """
    x_dot = s * (y - x)
    y_dot = r * x - y - x * z
    z_dot = x * y - b * z
    return np.asarray([x_dot, y_dot, z_dot])


def lorenz_next(x, y, z, s=10, r=28, b=2.667, dt=0.01):
    return lorenz(x, y, z, s, r, b) * dt + [x, y, z]


def lorenz_data(initial_vertex=(0.0, 1.0, 1.05), n_data=10000, s=10, r=28, b=2.667, dt=0.01):
    data = np.zeros((n_data, 3))
    data[0] = np.asarray(initial_vertex)
    for i in range(n_data - 1):
        data[i + 1] = lorenz_next(*data[i], s, r, b, dt)
    return data
