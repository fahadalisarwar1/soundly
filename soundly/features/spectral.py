import numpy as np
from scipy.fftpack import fft

__all_features__ = [
    'spectral_centroid',
    'spectral_rolloff'
]


def get_audio_spectrum(audio=None, sample_rate=None):
    """
    Computes the magnitude spectrum of an array of Reals
    :param audio: audio array
    :param sample_rate: sampling rate of audio signal
    :return: spectrum of the signal
    """
    if audio is not None:
        len_audio = len(audio)
        audio_fft = fft(audio)
        audio_fft = audio_fft[0: int(np.ceil((len_audio + 1)/2.0))]
        mag_fft = np.abs(audio_fft)
        mag_fft = mag_fft / float(len_audio)
        mag_fft = mag_fft ** 2
        if len_audio % 2 > 0:
            mag_fft[1: len(mag_fft)] = mag_fft[1: len(mag_fft)] * 2
        else:
            mag_fft[1: len(mag_fft)-1] = mag_fft[1: len(mag_fft)-1] * 2
            return mag_fft
    else:
        print("[-] No Audio provided")

# def spectral_rolloff(audio=None):

