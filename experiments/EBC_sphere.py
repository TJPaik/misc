#%%
from ripser import ripser
# import matplotlib.pyplot as plt
from joblib import delayed, Parallel
import numpy as np
#%%
n_jobs = 27
#%%
def get_first_betti(n_points, n_dim, inspect_list):
    try:
        data = np.random.randn(n_points, n_dim)
        data /= np.linalg.norm(data, axis=1).reshape(-1, 1)
        diagrams = ripser(data, maxdim=1, coeff=101)['dgms']
        result = np.zeros(len(inspect_list))
        _result = np.digitize(
            2 * np.arcsin(diagrams[1]/2),
            inspect_list)
        for el in _result:
            result[el[0]: el[1]] += 1
        return result
    except:
        return get_first_betti(n_points, n_dim, inspect_list)
#%%
n_points = [4, 8, 16, 32, 64, 128, 256, 512, 1024]
for n_p in n_points:
    output = Parallel(n_jobs=n_jobs, verbose=9)(
        delayed(get_first_betti)(n_p, 2, np.linspace(0, np.pi, 1000))
        for _ in range(50000)
    )
    output = np.asarray(output)
    # plt.plot(output.mean(axis=0))
    # plt.show()
    # plt.close()
    np.save(f"first_betti_sphere_S1_{n_p}.npy", output)

for n_p in n_points:
    output = Parallel(n_jobs=n_jobs, verbose=9)(
        delayed(get_first_betti)(n_p, 3, np.linspace(0, np.pi, 1000))
        # for _ in range(25000)
        for _ in range(50000)
    )
    output = np.asarray(output)
    # plt.plot(output.mean(axis=0))
    # plt.show()
    # plt.close()
    np.save(f"first_betti_sphere_S2_{n_p}.npy", output)
#%%
