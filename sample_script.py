from soundly.features.spectral import get_power_spectral_density

file = "/home/fahad/Py" \
       "charmProjects/AudioProject/data/raw/air_conditioner/22.wav"
from soundly.io.load import load_audio

sr, audio = load_audio(file)

# f, psd = get_power_spectral_density(audio, 10000)

from soundly.features.spectral import get_spectrum_peaks
import numpy as np
arr = []
for i in range(5):
    arr.append(np.random.randint(1, 100))

arr = np.array(arr)
ind, peaks = get_spectrum_peaks(arr)


