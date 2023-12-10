def calculate_zero_crossing_rate(frame):
    zcr = 0
    for i in range(1, len(frame)):
        if (frame[i-1] >= 0 and frame[i] < 0) or (frame[i-1] < 0 and frame[i] >= 0):
            zcr += 1
    return zcr

# Example usage
signal_frame = [0.2, -0.5, 0.8, -0.3, 0.6]
zcr = calculate_zero_crossing_rate(signal_frame)
print("Zero-crossing rate:", zcr)