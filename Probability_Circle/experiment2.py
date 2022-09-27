# %%
from multiprocessing import Pool
import tqdm
import matplotlib.pyplot as plt
import numpy as np
from ripser import Rips

# %%
rips = Rips()


# %%
def gen_points(P, N):
    tmp = np.random.randint(0, P, N)
    x = np.sin(np.pi * 2 * tmp / P)
    y = np.cos(np.pi * 2 * tmp / P)
    return x, y


# %%
def n_H1(epsilon, n_point, P):
    Bin = np.arange(0, 2 + epsilon, epsilon)
    X, Y = gen_points(P, n_point)
    diagrams = rips.fit_transform(np.array([X, Y]).T)
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
Epsilon = 0.01
n_trials = 10 ** 3
N_points_range = range(4, 32)
Points_range = range(4, 32)
for N_point in N_points_range:
    for Point in Points_range:
        final_result = np.zeros(len(np.arange(0, 2 + Epsilon, Epsilon)))
        j = 0
        for i in tqdm.tqdm(range(n_trials)):
            tmp = n_H1(Epsilon, N_point, Point)
            if tmp is not None:
                final_result += tmp
                j += 1
            else:
                print('None!!')
        final_result /= j
        plt.plot(np.arange(0, 2 + Epsilon, Epsilon), final_result)

    # name = f'exRegular/n_N{N_point}'
    # plt.savefig(f'Probability_Circle/experiment2/n_{N_point}_plus1.png')
    plt.show()
    plt.close()
# %%
Epsilon = 0.01
n_trials = 10 ** 3
N_points_range = range(4, 33)
Points_range = range(4, 33)
for Point in Points_range:
    for N_point in N_points_range:
        final_result = np.zeros(len(np.arange(0, 2 + Epsilon, Epsilon)))
        j = 0
        for i in tqdm.tqdm(range(n_trials)):
            tmp = n_H1(Epsilon, N_point, Point)
            if tmp is not None:
                final_result += tmp
                j += 1
            else:
                print('None!!')
        final_result /= j
        plt.plot(np.arange(0, 2 + Epsilon, Epsilon), final_result)

    # name = f'exRegular/n_P{Point}'
    # plt.savefig(f'Probability_Circle/experiment2/p_{Point}.png')
    plt.show()
    plt.close()
# %%
Epsilon = 0.01
n_trials = 10 ** 3
N_points_range = range(4, 32)
Points_range = [2 ** k for k in range(2, 10)]
for N_point in N_points_range:
    for Point in Points_range:
        final_result = np.zeros(len(np.arange(0, 2 + Epsilon, Epsilon)))
        j = 0
        for i in tqdm.tqdm(range(n_trials)):
            tmp = n_H1(Epsilon, N_point, Point)
            if tmp is not None:
                final_result += tmp
                j += 1
            else:
                print('None!!')
        final_result /= j
        plt.plot(np.arange(0, 2 + Epsilon, Epsilon), final_result, label=str(Point))

    # name = f'exRegular2/n_N{N_point}'
    plt.legend()
    plt.savefig(f'Probability_Circle/experiment2/n_{N_point}_x_2.png')
    plt.show()
    plt.close()
# %%
