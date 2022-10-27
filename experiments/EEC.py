# %%
import matplotlib.pyplot as plt
import numpy as np
from joblib import Parallel, delayed

import Expectation_EulerCharacteristic as EEC

# %%
n_jobs = 24
# %%
sphere2_output = []
for i in [2, 5, 7, 10, 15, 20]:
    print(i)
    output = Parallel(n_jobs=n_jobs, verbose=9)(
        delayed(EEC.sphere.euler_characteristic)(i, 2, np.linspace(0, np.pi, 1000))
        for _ in range(25000)
    )
    output = np.asarray([el for el in output if el is not None])
    sphere2_output.append(output)
# %%
sphere3_output = []
for i in [2, 5, 7, 10, 15, 20]:
    print(i)
    output = Parallel(n_jobs=n_jobs, verbose=9)(
        delayed(EEC.sphere.euler_characteristic)(i, 3, np.linspace(0, np.pi, 1000))
        for _ in range(25000)
    )
    output = np.asarray([el for el in output if el is not None])
    sphere3_output.append(output)
# %%
output = EEC.sphere.euler_characteristic(20, 2, np.linspace(0, np.pi, 1000))
output = np.asarray(output)
tmp = np.concatenate([
    sphere3_output[5],
    output.reshape(1, -1)
])
# %%
sphere3_output[5] = tmp
# %%
sphere4_output = []
for i in [2, 5, 7, 10, 15, 20]:
    print(i)
    output = Parallel(n_jobs=n_jobs, verbose=9)(
        delayed(EEC.sphere.euler_characteristic)(i, 4, np.linspace(0, np.pi, 1000))
        for _ in range(25000)
    )
    output = np.asarray([el for el in output if el is not None])
    sphere4_output.append(output)
# %%
sphere5_output = []
for i in [2, 5, 7, 10, 15, 20]:
    print(i)
    output = Parallel(n_jobs=n_jobs, verbose=9)(
        delayed(EEC.sphere.euler_characteristic)(i, 5, np.linspace(0, np.pi, 1000))
        for _ in range(25000)
    )
    output = np.asarray([el for el in output if el is not None])
    sphere5_output.append(output)
# %%
plt.plot(output.mean(axis=0))
plt.show()
# %%
sphere3_output = np.asarray(sphere3_output)
sphere4_output = np.asarray(sphere4_output)
sphere5_output = np.asarray(sphere5_output)

# %%
np.save('sphere3_56.npy', sphere3_output)
np.save('sphere4_56.npy', sphere4_output)
np.save('sphere5_56.npy', sphere5_output)
# %%
torus = []
for i in [2, 5, 7, 10, 15, 20]:
    print(i)
    output = Parallel(n_jobs=n_jobs, verbose=9)(
        delayed(EEC.torus.euler_characteristic)(i, np.linspace(0, np.sqrt(2) / 2, 1000))
        for _ in range(50000)
    )
    output = np.asarray([el for el in output if el is not None])
    torus.append(output)
# %%
torus = np.asarray(torus)
# %%
np.save('torus_50000.npy', torus)
# %%
plt.plot(torus[0].std(axis=0))
plt.show()
# %%
# %%
