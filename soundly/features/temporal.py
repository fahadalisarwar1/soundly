import numpy as np
from scipy.signal import hilbert
from scipy.stats.mstats import gmean

all_features = [
    "mean",
    "max",
    "min",
    'zero_crossing_rate',
    "envelope",
    'rms',
    'energy'
]


def get_zero_crossing_rate(audio=None):
    """
    Returns the Zero crossing Rate of the signal.
    :param audio: audio array
    :return: Zero Crossing Rate
    """
    zero_crosses = ((audio[:-1] * audio[1:]) < 0).sum()
    return zero_crosses


def get_mean(audio=None):
    """
    Find mean of the data array
    :param audio: data array
    :return: mean of the data
    """
    if audio is not None:
        return np.mean(audio)


def get_envelope(audio=None):
    """
    Calculate the envelope of an audio signal
    :param audio: Audio Data
    :return: envelop of the signal
    """
    if audio is not None:
        analytic_signal = hilbert(audio)
        amplitude_envelope = np.abs(analytic_signal)
        return amplitude_envelope
    else:
        print("[-] No audio Provided!")
        return 0


def get_rms(audio=None):
    """
    Computes the root mean square of an array/audio signal
    :param audio: audio array
    :return: RMS of an array
    """
    if audio is not None:
        return np.sqrt(np.mean(audio**2))
    else:
        print("[-] Audio not provided")
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


def get_energy(audio=None):
    """
    returns the energy of a signal
    :param audio: audio signal
    :return: energy of the signal
    """
    if audio is not None:
        return np.sum(np.power(audio, 2))
    else:
        print("[-] Error, No Audio File provided")
        return 0


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
    a = np.array(audio)
    return a.prod() ** (1.0 / len(a))


def get_steven_loudness(audio=None):
    """
    Calculates loudness of an audio array based on Steven's Power Law
    ref: https://en.wikipedia.org/wiki/Stevens%27s_power_law
    :param audio: audio array
    :return: loudness
    """
    if audio is not None:

        return np.power(get_energy(audio), 0.67)
    else:
        print("[-] Error, No Audio Provided")
