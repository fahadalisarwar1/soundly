from scipy.io.wavfile import read


def load_audio(file_name):
    """
    Loads an audio file and returns the sample rate and content as an array
    :param file_name: string or open file handle
    :return: sample_rate int Sample rate of wav file
    and data_arr: Data read from wav file
    """
    try:
        sample_rate, data_arr = read(filename=file_name)
        return sample_rate, data_arr
    except FileNotFoundError:
        print("[-] File not found: "+file_name)





