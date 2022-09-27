# %%
# from sympy.functions.combinatorial.numbers import nC
import matplotlib.pyplot as plt
import numpy as np
import math
from itertools import combinations
from sympy import symbols, integrate, floor, Sum, Indexed, lambdify, factorial, Piecewise
from sympy.abc import k, m, x
from tqdm import tqdm


def convert_distance_2_to_1(dist2):
    return math.asin(dist2 / 2) / math.pi


Original = np.load('Probability_Circle/experiment1/result.npy')
O_x_values = np.arange(0, 2 + 0.01, 0.01)
O_x_converted = np.asarray([convert_distance_2_to_1(el) for el in O_x_values])


# %%
def nCr(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))


def IH_CDF(n, x, x_floor=None):
    # result = 0
    # for k in range(math.floor(x) + 1):
    #     a = (-1) ** k
    #     b = nCr(n, k)
    #     c = (x - k) ** n
    #     result += a * b * c
    # return result / math.factorial(n)
    if x_floor is None:
        x_floor = floor(x)
    return Sum(
        ((-1) ** k) * nCr(n, k) * (x - k) ** n, (k, 0, x_floor)
    ).doit() / factorial(n)
    # return sum(
    #     ((-1) ** k) * nCr(n, k) * (x - k) ** n for k in range(floor(x) + 1)
    # ) / math.factorial(n)


# # %%
# IH_CDF(2, x, 0)
# # %%
# IH_CDF(2, x, 1).subs(x, 2)
# %%
# %%
# epsilon = 0.3
# epsilon_inverse = (1 / epsilon)
# n = 10
# x = symbols('x')
# # %%
# a = IH_CDF(n - 1, epsilon_inverse * (1 - x), 2)
# b = IH_CDF(n - 1, epsilon_inverse * (1 - epsilon), math.floor(epsilon_inverse * (1 - epsilon)))
# c = a - b
# d = (epsilon ** (n - 1)) * c
# # %%
# integrate(d, (x, 0, epsilon)) * math.factorial(10)
# %%
def get_prob(epsilon, n):
    epsilon_inverse = (1 / epsilon)
    thr = 1 - (floor(epsilon_inverse) * epsilon)
    COE = math.factorial(n) * (epsilon ** (n - 1))

    L = IH_CDF(n - 1, epsilon_inverse - 1)
    L_i = L * epsilon

    A = IH_CDF(n - 1, epsilon_inverse * (1 - x), floor(epsilon_inverse))
    A_i = integrate(A, (x, 0, 1 - floor(epsilon_inverse) * epsilon))

    B = IH_CDF(n - 1, epsilon_inverse * (1 - x), floor(epsilon_inverse) - 1)
    B_i = integrate(B, (x, 1 - floor(epsilon_inverse) * epsilon, epsilon))

    C = A_i + B_i - L_i

    return COE * C


# %%
RESULTS = []
for number_of_pts in range(4, 20):
    print(number_of_pts)
    probs = []
    for eps in tqdm(np.arange(0, 1 / 3, 0.015)[1:]):
        probs.append(
            get_prob(eps, number_of_pts)
        )
    probs = np.asarray(probs)
    RESULTS.append(probs)
RESULTS = np.asarray(RESULTS)
# %%
np.save('Probability_Circle/Formula_check/closed_results.npy', RESULTS)
RESULTS = np.load('Probability_Circle/Formula_check/closed_results.npy', allow_pickle=True)
# %%
plt.plot(np.arange(0, 1 / 3, 0.015)[1:], RESULTS[-1])
plt.show()
# %%
plt.plot(O_x_converted, Original[11])
plt.show()
# %%
[plt.plot(O_x_converted, Original[i], label=str(i + 4)) for i in range(len(Original))]
plt.legend()
plt.show()
# %%
[plt.plot(O_x_converted, Original[i], label=str(i + 4), color=f'C{i}') for i in range(len(Original))]
[plt.plot(np.arange(0, 1 / 3, 0.015)[1:], RESULTS[i], label=str(i + 4) + ' - c', color=f'C{i}', lw=5, alpha=0.5, ls=':')
 for i in
 range(len(RESULTS))]
# plt.legend()
# plt.savefig('Probability_Circle/Formula_check/summary.png')
plt.show()
plt.close()
# %%
