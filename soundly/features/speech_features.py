import numpy as np
from scipy.fftpack import dct


def get_mfcc(audio=None,
             sample_rate=None,
             frame_size_=0.025,
             pre_emphasis_=0.97,
             frame_stride_=0.01,
             NFFT_ = 512,
             n_fil_=40,
             num_coeff=15):
    """
    Computes MFCC for frames
    :param audio: audio signal
    :param sample_rate: sampling rate of audio
    :param frame_size_: size of each frame
    :param pre_emphasis_: pre-emphasis filter
    :param frame_stride_: overlapping duration
    :param NFFT_: N point FFT
    :param n_fil_: number of filter banks
    :param num_coeff: number of MFCC coefficients to be calculated
    :return: MFCC coefficients.
    """
    pre_emphasis = pre_emphasis_
    print("len" + str(len(audio)/sample_rate))
    emphasized_signal = np.append(audio[0], audio[1:] - pre_emphasis * audio[:-1])
    frame_size = frame_size_
    print(frame_size)
    frame_stride = frame_stride_
    frame_length, frame_step = frame_size * sample_rate, frame_stride * sample_rate  # Convert from seconds to samples
    signal_length = len(emphasized_signal)
    frame_length = int(round(frame_length))
    frame_step = int(round(frame_step))
    num_frames = int(np.ceil(
                        float(np.abs(signal_length - frame_length)) / frame_step))
    # Make sure that we have at least 1 frame
    print("num frames: "+str(num_frames))
    pad_signal_length = num_frames * frame_step + frame_length
    z = np.zeros((pad_signal_length - signal_length))
    pad_signal = np.append(emphasized_signal,
                           z)
    # Pad Signal to make sure that all frames have equal number of samples without truncating any
    # samples from the original signal

    indices = np.tile(np.arange(0, frame_length), (num_frames, 1)) + np.tile(
        np.arange(0, num_frames * frame_step, frame_step), (frame_length, 1)).T
    frames = pad_signal[indices.astype(np.int32, copy=False)]
    frames *= np.hamming(frame_length)
    NFFT = NFFT_
    mag_frames = np.absolute(np.fft.rfft(frames, NFFT))  # Magnitude of the FFT
    pow_frames = ((1.0 / NFFT) * (mag_frames ** 2))  # Power Spectrum

    low_freq_mel = 0
    nfilt = n_fil_
    high_freq_mel = (2595 * np.log10(1 + (sample_rate / 2) / 700))  # Convert Hz to Mel
    mel_points = np.linspace(low_freq_mel, high_freq_mel, nfilt + 2)  # Equally spaced in Mel scale
    hz_points = (700 * (10 ** (mel_points / 2595) - 1))  # Convert Mel to Hz
    bin = np.floor((NFFT + 1) * hz_points / sample_rate)

    fbank = np.zeros((nfilt, int(np.floor(NFFT / 2 + 1))))
    for m in range(1, nfilt + 1):
        f_m_minus = int(bin[m - 1])  # left
        f_m = int(bin[m])  # center
        f_m_plus = int(bin[m + 1])  # right

        for k in range(f_m_minus, f_m):
            fbank[m - 1, k] = (k - bin[m - 1]) / (bin[m] - bin[m - 1])
        for k in range(f_m, f_m_plus):
            fbank[m - 1, k] = (bin[m + 1] - k) / (bin[m + 1] - bin[m])
    filter_banks = np.dot(pow_frames, fbank.T)
    filter_banks = np.where(filter_banks == 0, np.finfo(float).eps, filter_banks)  # Numerical Stability
    filter_banks = 20 * np.log10(filter_banks)  # dB
    num_ceps = num_coeff
    mfcc = dct(filter_banks, type=2, axis=1, norm='ortho')[:, 1: (num_ceps + 1)]   # Keep 2-13

    filter_banks -= (np.mean(filter_banks, axis=0) + 1e-8)
    mfcc -= (np.mean(mfcc, axis=0) + 1e-8)
    return mfcc
