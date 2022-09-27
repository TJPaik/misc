# %%
import matplotlib.pyplot as plt
import numpy as np
from ripser import Rips
from joblib import Parallel, delayed

# %%
rips = Rips()


# %%
def n_H1(epsilon, n_point):
    Bin = np.arange(0, 2 + epsilon, epsilon)
    x = np.random.multivariate_normal([0, 0], [[1, 0], [0, 1]], n_point).T
    x_n = x / np.linalg.norm(x, axis=0)
    diagrams = rips.fit_transform(x_n.T)
    if len(diagrams[1]) == 0:
        return np.zeros_like(Bin)
    elif len(diagrams[1]) > 1:
        return None
    else:
        result = np.zeros_like(Bin)
        _tmp = np.digitize(diagrams[1][0], Bin)
        result[_tmp[0]: _tmp[1]] = 1
        return result


# %%
RESULT = []
Epsilon = 0.01
n_trials = 10 ** 5
for n_points in range(4, 20):
    A = Parallel(n_jobs=4, verbose=1)(
        delayed(n_H1)(Epsilon, n_points) for i in range(n_trials)
    )
    final_result = sum(A) / n_trials
    # for i in tqdm.tqdm(range(n_trials)):
    #     tmp = n_H1(Epsilon, n_points)
    #     if tmp is not None:
    #         final_result += tmp
    #         j += 1
    #     else:
    #         print('None!!')
    # final_result /= j
    RESULT.append(final_result)
    plt.title(n_points)
    plt.plot(np.arange(0, 2 + Epsilon, Epsilon), final_result)
    # plt.savefig(f'Probability/n_{n_points}.png')
    plt.show()
    plt.close()
RESULT = np.asarray(RESULT)
# %%
np.save('Probability_Circle/experiment1/result.npy', RESULT)
# %%
for el, label in zip(RESULT, range(4, 20)):
    plt.plot(el, label=label)
plt.legend()
plt.show()
plt.savefig(f'Probability_Circle/experiment1/summary.png')
plt.close()
