import cv2
import numpy as np


def analyze_dct(image):
    image = np.array(image.convert("RGB"))

    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    height, width = gray.shape

    height = height - (height % 8)
    width = width - (width % 8)

    gray = gray[:height, :width]

    coefficients = []
    high_frequency = []

    for y in range(0, height, 8):
        for x in range(0, width, 8):
            block = np.float32(gray[y:y + 8, x:x + 8])

            dct_block = cv2.dct(block)
            magnitude = np.abs(dct_block)

            coefficients.extend(magnitude.flatten())

            high_frequency.extend(
    		magnitude[2:, 2:].flatten()
	    )

    coefficients = np.array(coefficients)
    high_frequency = np.array(high_frequency)

    total_energy = np.sum(coefficients ** 2)
    high_frequency_energy = np.sum(high_frequency ** 2)

    high_frequency_ratio = (
        high_frequency_energy / total_energy
        if total_energy > 0
        else 0
    )

    return {
        "mean_dct": float(np.mean(coefficients)),
        "std_dct": float(np.std(coefficients)),
        "max_dct": float(np.max(coefficients)),
        "high_frequency_ratio": float(high_frequency_ratio)
    }