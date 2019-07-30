from soundly.io.load import load_audio
from soundly.features.temporal import get_zero_crossing_rate
from soundly.features.speech_features import get_mfcc
from soundly.features.spectral import get_audio_spectrum
from soundly.features.temporal import get_energy
# from soundly.features.temporal import get_geometric_mean
# from soundly.features.temporal import geo_mean
from soundly.features.temporal import get_steven_loudness

import numpy as np

sr, audio = load_audio("/home/fahad/PycharmProjects/soundly/soundly/io/audio_0.wav")

zcr = get_zero_crossing_rate(audio)
mfcc = get_mfcc(audio, sample_rate=sr, frame_size_=0.025)
mean_mfcc = np.array([np.mean(i) for i in mfcc.T])
std_mfcc = np.array([np.std(i) for i in mfcc.T])
# get_audio_spectrum()
from soundly.features.temporal import get_envelope
env = get_envelope(audio)
energy = get_energy(audio)
spec= get_audio_spectrum(audio, sample_rate=sr)
# g_mean = get_geometric_mean([1,2,3,4])
# g_mean1 = geo_mean(audio)
loud = get_steven_loudness(audio)
