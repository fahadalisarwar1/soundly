import numpy as np
from scipy.signal import hilbert

from scipy.signal import find_peaks

all_features = [
    'zero_crossing_rate',
    "envelope",
    'energy',
    'steven_loudness'
    'peaks'
]


def get_zero_crossing_rate(audio=None):
    """
    Returns the Zero crossing Rate of the signal.
    :param audio: audio array
    :return: Zero Crossing Rate
    """
    zero_crosses = ((audio[:-1] * audio[1:]) < 0).sum()
    return zero_crosses


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


def get_peaks(audio=None):
    """
    Peaks of audio signal
    :param audio: audio data
    :return: peaks of the signal
    """
    if audio is not None:
        peaks = find_peaks(audio)[0]
        return peaks


def get_peak_envelope_ratio(envelope=None):
    """
    This algorithm computes the ratio between the index of the maximum value of the envelope of a signal
     and the total length of the envelope.This ratio shows how much the maximum amplitude is off-center.
     Its value is close to 0 if the maximum is close to the beginning (e.g. Decrescendo or Impulsive sounds),
     close to 0.5 if it is close to the middle (e.g. Delta sounds) and close to 1 if it is close to the end
      of the sound (e.g. Crescendo sounds).
     This algorithm is intended to be fed by the output of the Envelope algorithm
    :param envelope: the envelope of the signal
    :return: the maximum amplitude position to total length ratio
    """
    if envelope is not None:
        peak_index = np.argmax(envelope)
        return peak_index / len(envelope)
    else:
        print("[-] Error please provide envelope array")


def get_audio_duration(audio=None, sample_rate=None):
    """
    This algorithm outputs the total duration of an audio signal.
    :param audio: the input signal
    :param sample_rate: the sampling rate of the audio signal [Hz]
    :return: the duration of the signal [s]
    """
    if audio is not None:
        return len(audio)/sample_rate


def temporal_all_feat(audio=None,
                      sample_rate=None):
    """
    Calculates all of tmeporal features
    :param audio: audio data
    :param sample_rate: sampling rate of audio
    :return: dictionary of extracted temporal features
    """
    if audio is not None:
        energy_audio = get_energy(audio)
        loudness_audio = get_steven_loudness(audio)
        envelope_audio = get_envelope(audio)
        zcr_audio = get_zero_crossing_rate(audio)
        peaks_audio = get_peaks(audio)
        peak_envelope_ratio = get_peak_envelope_ratio()
        feat_dict = {
            'energy_audio': energy_audio,
            'loudness_audio': loudness_audio,
            'envelope_audio': envelope_audio,
            'zcr_audio': zcr_audio,
            'peaks_audio': peaks_audio,
            'peak_envelope_ratio': peak_envelope_ratio
        }
        return feat_dict
    else:
        print("[-] Error, No Audio Selected")
        return 0

