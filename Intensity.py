import math

def calculate_intensity(power):
    P0 = 1e-5  # Reference threshold pressure (Pa)
    intensity_db = 10 * math.log10(power / P0)
    return intensity_db

# Example usage
sound_power = 0.001  # Assuming a power of 0.001 Watts
sound_intensity = calculate_intensity(sound_power)
print("Sound intensity (dB):", sound_intensity)