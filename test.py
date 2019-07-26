from soundly.io.load import load_audio
from soundly.features.temporal import get_zero_crossing_rate
from soundly.features.speech_features import get_mfcc
from soundly.features.spectral import get_audio_spectrum
import numpy as np

sr, audio = load_audio("/home/fahad/PycharmProjects/soundly/soundly/io/audio_0.wav")

zcr = get_zero_crossing_rate(audio)
mfcc = get_mfcc(audio, sample_rate=sr, frame_size_=0.1, frame_stride_=0.1)
mean_mfcc = np.array([np.mean(i) for i in mfcc.T])
std_mfcc = np.array([np.std(i) for i in mfcc.T])
# get_audio_spectrum()
from soundly.features.temporal import get_envelope
env = get_envelope(audio)
