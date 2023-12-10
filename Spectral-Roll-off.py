def calculate_spectral_roll_off(magnitudes, total_energy, roll_off_percentage):
    roll_off_energy = roll_off_percentage * total_energy
    cumulative_energy = 0.0
    roll_off_index = 0

    for i, magnitude in enumerate(magnitudes):
        cumulative_energy += magnitude
        if cumulative_energy >= roll_off_energy:
            roll_off_index = i
            break

    roll_off_frequency = roll_off_index / len(magnitudes)
    return roll_off_frequency

# Example usage
magnitudes = [0.1, 0.3, 0.5, 0.2]  # Magnitudes of frequency bins
total_energy = sum(magnitudes)  # Total energy of the spectrum
roll_off_percentage = 0.85  # Percentage of the energy below the roll-off frequency

roll_off_frequency = calculate_spectral_roll_off(magnitudes, total_energy, roll_off_percentage)
print("Spectral roll-off frequency:", roll_off_frequency)