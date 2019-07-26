from scipy.io.wavfile import write


def write_audio(filename, sample_rate, data):
    """
    Write a numpy array as a WAV file
    :param filename: string or open file handle
    :param sample_rate: The sample rate (in samples/sec).
    :param data: A 1-D or 2-D numpy array of either integer or float data-type
    """
    try:
        write(filename=filename,
              rate=sample_rate,
              data=data)
    except FileNotFoundError:
        print("[-] Error can't write file: " + filename)
