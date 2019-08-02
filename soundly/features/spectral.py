import numpy as np
from scipy.fftpack import fft
from scipy.signal import periodogram
from scipy.signal import find_peaks, find_peaks_cwt

__all_features__ = [
    'spectral_centroid',
    'spectral_rolloff',
    'audio_spectrum'
]


def get_audio_spectrum(audio=None):
    """
    Computes the magnitude spectrum of an array of Reals
    :param audio: audio array
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


def spectral_flux(audio=None):
    if audio is not None:

        spectrum = get_audio_spectrum(audio)
        # TODO Not completed yet
        return spectrum
    else:
        print("[-] No Audio provided")


def get_spectral_centroid(audio=None, sample_rate=None):
    """
    Calculates the spectral centroid of audio signal
    :param audio: audio array
    :param sample_rate: sampling rate of audio
    :return: spectral centroid
    """
    if audio is not None and sample_rate is not None:
        magnitudes = np.abs(np.fft.rfft(audio))  # magnitudes of positive frequencies
        length = len(audio)
        freqs = np.abs(np.fft.fftfreq(length, 1.0/sample_rate)[:length//2+1])  # positive frequencies
        return np.sum(magnitudes*freqs) / np.sum(magnitudes)  # return weighted mean
    else:
        print("[-] No Audio provided")
        return 0


def get_power_spectral_density(audio_array=None, sampling_rate=22050):
    """
    Estimate power spectral density using a periodogram.
    :param audio_array:
    :param sampling_rate:
    """
    f, psd = periodogram(audio_array, sampling_rate)
    return f, psd


def get_spectrum_peaks(spectrum=None):
    """
    find the spectrum peak frequencies and values
    :param spectrum: spectrum of signal
    :return: peak indexes, peak values
    """
    if spectrum is not None:

        peak_indices = find_peaks(spectrum)[0]
        peak_values = []
        for i in peak_indices:
            peak_values.append(spectrum[i])
        peak_values = np.asarray(peak_values)
        return peak_indices, peak_values



