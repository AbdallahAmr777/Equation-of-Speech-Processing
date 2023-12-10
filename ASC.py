import numpy as np

def calculate_audio_spectrum_spread(spectrum, centroid):
    squared_diffs = (np.log10(spectrum) - centroid) ** 2
    spread = np.sqrt(np.sum(squared_diffs) / np.sum(spectrum))
    return spread

# Example usage
spectrum = [0.1, 0.3, 0.5, 0.2]  # Power spectrum values of frequency bins
centroid = 2.5  # Audio Spectrum Centroid

audio_spectrum_spread = calculate_audio_spectrum_spread(spectrum, centroid)
print("Audio Spectrum Spread:", audio_spectrum_spread)