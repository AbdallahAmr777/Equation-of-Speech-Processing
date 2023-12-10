def calculate_spectral_centroid(magnitudes, center_frequencies):
    centroid = sum(magnitudes * center_frequencies) / sum(magnitudes)
    return centroid

# Example usage
magnitudes = [0.1, 0.3, 0.5, 0.2]  # Magnitudes of frequency bins
center_frequencies = [100, 200, 300, 400]  # Center frequencies of frequency bins
centroid = calculate_spectral_centroid(magnitudes, center_frequencies)
print("Spectral centroid:", centroid)