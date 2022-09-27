# %%
import subprocess
from multiprocessing import Pool

import numpy as np
import ripser
from tqdm import tqdm

# %%
# every graph with 9 nodes
graph9_output = subprocess.check_output("./A2n_problem/Help/showg_linux64 -a ./A2n_problem/Help/graph9.g6", shell=True)
graph9_output = graph9_output.decode('utf-8')


# %%
# Parsing adjacent matrix
def parse_adj_mtr(graph_output):
    o_1 = graph_output.split('\n\n')
    o_2 = [el.strip() for el in tqdm(o_1)]
    o_3 = [el.split('\n')[1:] for el in tqdm(o_2)]
    o_4 = [[list(el2) for el2 in el] for el in tqdm(o_3)]
    o_5 = np.asarray(o_4).astype(bool)
    return o_5


o9_5 = parse_adj_mtr(graph_output=graph9_output)

# %%
rips = ripser.Rips(maxdim=4)


def Test9(inputs):
    return rips.fit_transform(
        1 - inputs.astype(int) - np.identity(9), distance_matrix=True
    )[4]


# %%
with Pool(5) as p:
    result = list(tqdm(
        p.imap(Test9, o9_5), total=len(o9_5)
    ))

for el in tqdm(result):
    if len(el) != 0:
        print(el)
        break
# None!!!
# %%
####################################################################################################

# graph10_output = subprocess.check_output("./A2n_problem/Help/showg_linux64 -a ./A2n_problem/Help/graph10c.g6",
#                                          shell=True)
# graph10_output = graph10_output.decode('utf-8')
# # %%
# o10_1 = graph10_output.split('\n\n')
# o10_2 = [el.strip() for el in tqdm(o10_1)]
# o10_3 = [el.split('\n')[1:] for el in tqdm(o10_2)]
# o10_4 = [[list(el2) for el2 in el] for el in tqdm(o10_3)]
# # %%
# o10_5 = np.asarray(o10_4).astype(bool)
# # %%
# rips = ripser.Rips(maxdim=4)
#
#
# # %%
# def Test10(inputs):
#     return rips.fit_transform(
#         1 - inputs.astype(int) - np.identity(10), distance_matrix=True
#     )[4]
#
#
# # %%
# with Pool(5) as p:
#     result = list(tqdm(
#         p.imap(Test9, o10_5), total=len(o10_5)
#     ))
#
# for el in tqdm(result):
#     if len(el) != 0:
#         print(el)
#         break
# # Only 1!!
