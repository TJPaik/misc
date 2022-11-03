# %%
from time import time
import pickle
import torch
import matplotlib.pyplot as plt
from gph import ripser_parallel
import persim
from torch.utils.data import DataLoader
from torchvision.datasets import MNIST
from torchvision.transforms import ToTensor
from ripser import ripser

# %%
torch.set_num_threads(26)
#
# # %%
# ds = MNIST("./", train=True, download=False, transform=ToTensor())
# dl = DataLoader(ds, batch_size=60000, shuffle=False)
# data, _ = next(iter(dl))
# data = data.squeeze()
# data2 = data.view(len(data), -1)
# # %%
# dm = torch.cdist(data2, data2, compute_mode='donot_use_mm_for_euclid_dist')
# # %%
# torch.save(dm, 'mnist_dm.pth')
# %%
dm = torch.load('mnist_dm.pth')
# %%
while True:
    rand_idx = torch.randint(0, 60000, (60000,))
    sub_dm_np = dm[rand_idx][:, rand_idx].numpy()
    q = time()
    print('start')
    dgm = ripser_parallel(sub_dm_np, metric='precomputed', maxdim=1, n_threads=26)
    print('end')
    print(time() - q)

#     persim.plot_diagrams(dgm['dgms'])
#     plt.show()
#     plt.close()

    with open(f'mnist_dgm_{time()}.pkl', 'wb') as f:
        pickle.dump(dgm, f)
# %%
