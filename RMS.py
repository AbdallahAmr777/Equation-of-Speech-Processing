import math

def calculate_rms(data):
    N = len(data)
    sum_of_squares = sum(x ** 2 for x in data)
    mean_squared = sum_of_squares / N
    rms = math.sqrt(mean_squared)
    return rms

# Example usage
waveform = [2, 4, 6, 8, 10]
rms_amplitude = calculate_rms(waveform)
print("RMS amplitude:", rms_amplitude)