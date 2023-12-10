import numpy as np

def discrete_fourier_transform(signal):
    N = len(signal)  # Length of the signal
    X = np.zeros(N, dtype=np.complex128)  # Initialize array to store DFT coefficients
    
    for k in range(N):
        for n in range(N):
            X[k] += signal[n] * np.exp(-2j * np.pi * k * n / N)
    
    return X

# Example usage
windowed_signal = np.array([0.1, 0.2, 0.3, 0.4, 0.5])  # Replace with your actual windowed signal

dft_coefficients = discrete_fourier_transform(windowed_signal)

print("DFT coefficients:", dft_coefficients)