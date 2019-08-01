import numpy as np
from scipy.stats.mstats import gmean


def get_mean(array=None):
    """
    Find mean of the data array
    :param array: data array
    :return: mean of the data
    """
    if array is not None:
        return np.mean(array)


def get_rms(array=None):
    """
    Computes the root mean square of an array/audio signal
    :param array: audio array
    :return: RMS of an array
    """
    if array is not None:
        return np.sqrt(np.mean(array**2))
    else:
        print("[-] Array not provided")
        return 0


def get_max(audio=None):
    """
    Find the max value of array
    :param audio:
    :return: max_value in array
    """
    if audio is not None:
        return np.max(audio)
    else:
        print("[-] No Audio Provided")


def get_min(audio=None):
    """
    Find the min value of array
    :param audio:
    :return: min_value in array
    """
    if audio is not None:
        return np.min(audio)
    else:
        print("[-] No Audio Provided")


def get_geometric_mean(audio=None):
    """
    returns the geometric mean of an array
    :param audio: audio array
    :return: geo-metric mean
    """
    if audio is not None:
        return gmean(audio)
    else:
        print("[-] No audio provided")
        return 0


def geo_mean(audio):
    """
    finds geometric mean of an array
    :param audio: array
    :return: geometric mean
    """
    a = np.array(audio)
    return a.prod() ** (1.0 / len(a))


def get_flatness(audio=None):
    """
    This algorithm computes the flatness of an array, which is defined as the ratio between
    the geometric mean and the arithmetic mean.
    :param audio: the input array
    :return:  the flatness (ratio between the geometric and the arithmetic mean of the input array)

    """
    if audio is not None:

        gm = get_geometric_mean(audio)
        _mean = get_mean(audio)
        flatness = gm / _mean
        return flatness
