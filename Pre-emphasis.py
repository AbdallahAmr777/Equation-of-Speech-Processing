import numpy as np

def pre_emphasis(signal, k):
    # Apply pre-emphasis to the signal
    emphasized_signal = np.append(signal[0], signal[1:] - k * signal[:-1])
    return emphasized_signal

# Example usage
input_signal = np.array([0.1, 0.2, 0.3, 0.4, 0.5])  # Replace with your actual input signal
pre_emphasis_coefficient = 0.5  # Replace with your desired pre-emphasis coefficient

emphasized_signal = pre_emphasis(input_signal, pre_emphasis_coefficient)

print("Input signal:", input_signal)
print("Emphasized signal:", emphasized_signal)