from torch.utils.data import IterableDataset, DataLoader


def double_dataloader(dataloader):
    global _iter1, _iter2, _order
    _iter1 = iter(dataloader)
    _iter2 = iter(dataloader)
    _order = 1

    class TmpIterableDs(IterableDataset):
        def __init__(self):
            super(TmpIterableDs, self).__init__()
            self.count = 0

        def __iter__(self):
            global _iter1, _iter2, _order
            if _order == 1:
                _iter2 = iter(dataloader)
                yield from _iter1
                _order = 2
            else:
                _iter1 = iter(dataloader)
                yield from _iter2
                _order = 1

        def __len__(self):
            return len(dataloader)

    tmp_iterable_ds = TmpIterableDs()
    return DataLoader(tmp_iterable_ds, 1, False, collate_fn=lambda x: x)
