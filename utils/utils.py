import os
import time
from datetime import timedelta
import numpy as np
import torch


def time_since(start_time):
    seconds = int(time.time() - start_time)
    return str(timedelta(seconds=seconds))

def get_path(base_dir, base_name, suffix):
    return os.path.join(base_dir, base_name + suffix)

def set_random_seed(seed):
    """
    Set the random seed for Numpy and PyTorch operations
    Args:
        seed: seed for the random number generators
    """
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed(seed)

def unique(arr):
    # Finds unique rows in arr and return their indices
    arr = arr.cpu().numpy()
    arr_ = np.ascontiguousarray(arr).view(np.dtype((np.void, arr.dtype.itemsize * arr.shape[1])))
    _, idxs = np.unique(arr_, return_index=True)
    if torch.cuda.is_available():
        return torch.LongTensor(np.sort(idxs)).cuda()
    return torch.LongTensor(np.sort(idxs))

def parse_config(config_file):
    import yaml
    from easydict import EasyDict
    with open(config_file) as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    
    config = EasyDict(config)
    return config
