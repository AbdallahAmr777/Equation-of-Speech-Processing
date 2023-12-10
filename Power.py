def calculate_power(signal):
    N = len(signal)
    power = (1/N) * sum(x**2 for x in signal)
    return power

# Example usage
sound_signal = [2, 4, 6, 8, 10]
signal_power = calculate_power(sound_signal)
print("Signal power:", signal_power)