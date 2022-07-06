import torch
import numpy as np
from gudhi.rips_complex import RipsComplex


def euler_characteristic(n_points, n_dim, inspect_list):
    data = torch.randn(n_points, n_dim)
    data /= torch.norm(data, dim=1)[:, None]
    distance_matrix = torch.cdist(data, data, )
    distance_matrix = 2 * torch.arcsin(distance_matrix / 2)
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


if __name__ == '__main__':
    from joblib import Parallel, delayed
    import matplotlib.pyplot as plt

    xs = np.linspace(0, np.pi, 1000)
    euler_characteristic(2, 2, xs)

    output = Parallel(n_jobs=8, verbose=9)(
        delayed(euler_characteristic)(10, 2, np.linspace(0, np.pi, 1000))
        for _ in range(40000)
    )
    output = np.asarray(output)

    plt.plot(
        # xs[:100],
        output.mean(axis=0)
    )
    plt.show()