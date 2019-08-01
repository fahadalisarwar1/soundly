from soundly.features.statistical import get_max
import numpy as np


def test_max():
    arr = np.array([1, 2, 3, 4, 5, 6, 7])
    assert get_max(arr) == 7
