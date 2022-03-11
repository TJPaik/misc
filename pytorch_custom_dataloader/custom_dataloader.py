from torch.utils.data import IterableDataset, DataLoader
# pytorch                   1.7.1           py3.9_cuda11.0.221_cudnn8.0.5_0    pytorch

from .zmod import Zmod


def custom_dataloader(dataloader, n=3, prepare=2):
    _iter_list = [None for _ in range(n)]
    _order = Zmod(0, n)

    class TmpIterableDs(IterableDataset):
        def __init__(self):
            super(TmpIterableDs, self).__init__()
            _iter_list[0] = iter(dataloader)

        def __iter__(self):
            nonlocal _iter_list, _order
            iter_now = _iter_list[_order.number]
            for i in range(prepare):
                if _iter_list[(_order + i + 1).number] is None:
                    _iter_list[(_order + i + 1).number] = iter(dataloader)
            yield from iter_now
            _iter_list[_order.number] = None
            _order += 1

        def __len__(self):
            return len(dataloader)

    tmp_iterable_ds = TmpIterableDs()
    return DataLoader(tmp_iterable_ds, 1, False, collate_fn=lambda x: x)
