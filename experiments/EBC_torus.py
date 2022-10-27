# %%
import numpy as np
from joblib import Parallel, delayed
import torch
from ripser import ripser

n_jobs = 27


def get_first_betti(n_points, inspect_list):
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
        return get_first_betti(n_points, inspect_list)

    distance_matrix = distance_matrix.numpy()
    diagrams = ripser(distance_matrix, distance_matrix=True, maxdim=1, coeff=101)['dgms'][1]
    result = np.zeros(len(inspect_list))
    _result = np.digitize(
        diagrams,
        inspect_list)
    for el in _result:
        result[el[0]: el[1]] += 1
    return result


# %%
n_points = [4, 8, 16, 32, 64, 128, 256, 512, 1024]
for n_p in n_points:
    output = Parallel(n_jobs=n_jobs, verbose=9)(
        delayed(get_first_betti)(n_p, np.linspace(0, np.sqrt(2) / 2, 1000))
        for _ in range(50000)
    )
    output = np.asarray(output)
    # plt.plot(output.mean(axis=0))
    # plt.show()
    # plt.close()
    np.save(f"first_betti_torus_{n_p}.npy", output)
# %%
