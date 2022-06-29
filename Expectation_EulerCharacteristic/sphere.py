import torch
from gudhi.rips_complex import RipsComplex
from tqdm import tqdm


def euler_characteristic(n_points, n_dim, inspect_list):
    data = torch.randn(n_points, n_dim)
    data /= torch.norm(data, dim=1)[:, None]
    distance_matrix = torch.cdist(data, data, )
    distance_matrix = 2 * torch.arcsin(distance_matrix / 2)
    assert torch.all(~torch.isnan(distance_matrix))

    rips = RipsComplex(distance_matrix.numpy())
    tree = rips.create_simplex_tree(max_dimension=len(data) + 1)

    euler_characteristic_list = []
    euler_characteristic_tmp = 0
    generator = tree.get_filtration()
    not_done = True
    for idx, inspect_number in tqdm(enumerate(inspect_list), disable=True):
        while not_done:
            try:
                simp, f_value = next(generator)
            except StopIteration:
                not_done = False
                break
            if f_value > inspect_number:
                euler_characteristic_list.append(
                    euler_characteristic_tmp
                )
                tmp = 1 if len(simp) % 2 else -1
                euler_characteristic_tmp += tmp
                # print(euler_characteristic, 'h')
                break
            else:
                tmp = 1 if len(simp) % 2 else -1
                euler_characteristic_tmp += tmp
                # print(euler_characteristic, 'c')
        if not not_done:
            euler_characteristic_list.append(euler_characteristic_tmp)
    return euler_characteristic_list
