import numpy as np
import torch
from gudhi.rips_complex import RipsComplex


def euler_characteristic(n_points, inspect_list):
    data = torch.rand(n_points, 2)
    _data = torch.rand(0, 2)
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            _data = torch.concat([_data, data + torch.tensor([i, j])])

    _distance_matrix = torch.cdist(_data, _data)
    distance_matrix = torch.zeros(n_points, n_points)
    for i in range(n_points):
        for j in range(n_points):
            distance_matrix[i, j] = torch.min(_distance_matrix[i::n_points, j::n_points])

    try:
        assert torch.all(~torch.isnan(distance_matrix))
        assert torch.all(distance_matrix >= 0)
    except AssertionError:
        print('None')
        return None

    rips = RipsComplex(distance_matrix=distance_matrix.numpy())
    tree = rips.create_simplex_tree(max_dimension=len(data) + 1)

    euler_characteristic_list = []
    generator = tree.get_filtration()
    # print(inspect_list)
    tmp = 0
    # last_summand = 0
    f = -np.inf
    for inspect_number in inspect_list:
        while True:
            if f <= inspect_number:
                try:
                    s, f = next(generator)
                    # print(f)
                    s = 1 if len(s) % 2 else -1
                    tmp += s
                except StopIteration:
                    s = 0
                    f = np.inf
            else:
                euler_characteristic_list.append(tmp - s)
                break
    return euler_characteristic_list
