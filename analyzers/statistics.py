from PIL import Image
import numpy as np


def analyze_statistics(image):
    image = image.convert("RGB")
    pixels = np.array(image)

    height, width, channels = pixels.shape

    mean_pixel = np.mean(pixels)
    std_pixel = np.std(pixels)

    entropy = 0

    for channel in range(3):
        values, counts = np.unique(
            pixels[:, :, channel],
            return_counts=True
        )

        probabilities = counts / counts.sum()

        entropy += -np.sum(
            probabilities * np.log2(probabilities)
        )

    entropy = entropy / 3

    return {
        "width": int(width),
        "height": int(height),
        "channels": int(channels),
        "mean_pixel": float(mean_pixel),
        "std_pixel": float(std_pixel),
        "entropy": float(entropy)
    }