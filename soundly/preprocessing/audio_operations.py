from soundly.io.load import load_audio


def select_duration(audio=None, sampling_rate=None, duration=None):
    """
    select a specific duration of audio
    :param audio: audio (filename or data array)
    :param sampling_rate: sampling rate of array
    :param duration: duration in seconds you want to select.
    :return: sliced audio array
    """
    if audio is not None:
        if isinstance(audio, str):
            if audio.endswith(".wav"):
                sample_rate, audio_arr = load_audio(audio)
                try:
                    return audio_arr[:int(sample_rate*duration)]
                except ValueError:
                    print("[-] Invalid Duration")

        else:
            try:
                return audio[:int(sampling_rate * duration)]
            except ValueError:
                print("[-] Invalid Duration")
