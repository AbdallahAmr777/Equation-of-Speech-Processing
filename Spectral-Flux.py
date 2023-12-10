def calculate_spectral_flux(current_frame, previous_frame):
    flux = sum((current_frame - previous_frame) ** 2)
    return flux

# Example usage
current_frame = [0.1, 0.3, 0.5, 0.2]  # Magnitudes of frequency bins for the current frame
previous_frame = [0.2, 0.4, 0.6, 0.1]  # Magnitudes of frequency bins for the previous frame

spectral_flux = calculate_spectral_flux(current_frame, previous_frame)
print("Spectral flux:", spectral_flux)