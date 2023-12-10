import numpy as np

def apply_hamming_window(frame):
    N = len(frame)
    hamming_window = 0.54 - 0.46 * np.cos((2 * np.pi * np.arange(N)) / (N - 1))
    windowed_frame = frame * hamming_window
    return windowed_frame

# Example usage
signal_frame = [0.2, 0.5, 0.8, 0.3, 0.6]
windowed_frame = apply_hamming_window(signal_frame)
print("Windowed frame:", windowed_frame)