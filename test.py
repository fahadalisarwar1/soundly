from soundly.io.load import load_audio
from soundly.features.temporal import temporal_all_feat
from soundly.features.spectral import get_audio_spectrum
sr, audio = load_audio("/home/fahad/PycharmProjects/soundly/soundly/io/audio_0.wav")

# feat_dict = temporal_all_feat(audio)
spec = get_audio_spectrum(audio)

from soundly.preprocessing.noise_removal import remove_noise

sr_audio, audio_tram = load_audio("/home/fahad/PycharmProjects/soundly/soundly/preprocessing/tram-2018-11-17-14-20-54_63.40_66.80_audio.wav")
sr_noise, noise_tram = load_audio("/home/fahad/PycharmProjects/soundly/soundly/preprocessing/tram-2018-11-17-13-29-24_29_39_noise.wav")
fil = remove_noise(audio=audio_tram, noise=noise_tram)

