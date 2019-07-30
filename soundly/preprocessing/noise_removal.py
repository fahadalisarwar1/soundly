from scipy.signal import stft
from scipy.signal import istft
import numpy as np
import math
import scipy


def amp_2_db(x,):
    """

    :param x:
    """
    s = np.asarray(x)
    mag = np.abs(s)
    mag_db = 20 * math.log10(mag)
    # power = np.square(mag)
    return mag_db


def db_2_amp(db_val):
    amp = np.power(10, db_val/20)
    return amp


def remove_noise(
    audio=None,
    noise=None,
    n_grad_freq=2,
    n_grad_time=4,
    n_fft=2048,
    win_length=2048,
    hop_length=512,
    n_std_thresh=1.5,
    prop_decrease=1.0,
):
    """
    Remove noise from audio based upon a clip containing only noise
    :param audio:
    :param noise:
    :param n_grad_freq:
    :param n_grad_time:
    :param n_fft:
    :param win_length:
    :param hop_length:
    :param n_std_thresh:
    :param prop_decrease:
    """
    noise_stft = stft(x=noise, nfft=n_fft)
    noise_stft_db = amp_2_db(noise_stft[2])
    mean_freq_noise = np.mean(noise_stft_db, axis=1)
    std_freq_noise = np.std(noise_stft_db, axis=1)
    noise_thresh = mean_freq_noise + std_freq_noise * n_std_thresh

    sig_stft = stft(x=audio, nfft=n_fft)
    sig_stft_db = amp_2_db(np.abs(sig_stft[2]))
    mask_gain_db = np.min(amp_2_db(np.abs(sig_stft)))
    print(noise_thresh, mask_gain_db)

    smoothing_filter = np.outer(
        np.concatenate(
            [
                np.linspace(0, 1, n_grad_freq + 1, endpoint=False),
                np.linspace(1, 0, n_grad_freq + 2),
            ]
        )[1:-1],
        np.concatenate(
            [
                np.linspace(0, 1, n_grad_time + 1, endpoint=False),
                np.linspace(1, 0, n_grad_time + 2),
            ]
        )[1:-1],
    )
    smoothing_filter = smoothing_filter / np.sum(smoothing_filter)
    # calculate the threshold for each frequency/time bin
    db_thresh = np.repeat(
        np.reshape(noise_thresh, [1, len(mean_freq_noise)]),
        np.shape(sig_stft_db)[1],
        axis=0,
    ).T
    # mask if the signal is above the threshold
    sig_mask = sig_stft_db < db_thresh
    sig_mask = scipy.signal.fftconvolve(sig_mask, smoothing_filter, mode="same")
    sig_mask = sig_mask * prop_decrease

    sig_stft_db_masked = (
        sig_stft_db * (1 - sig_mask)
        + np.ones(np.shape(mask_gain_db)) * mask_gain_db * sig_mask
    )  # mask real
    sig_imag_masked = np.imag(sig_stft) * (1 - sig_mask)
    sig_stft_amp = (db_2_amp(sig_stft_db_masked) * np.sign(sig_stft)) + (
        1j * sig_imag_masked
    )

    recovered_signal = istft(sig_stft_amp, hop_length, win_length)
    recovered_spec = amp_2_db(
        np.abs(stft(recovered_signal, n_fft, hop_length, win_length))
    )
    return recovered_signal
