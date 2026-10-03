import numpy as np
from PIL import Image
from scipy.stats import chi2


def analyze_chi_square(image):
    image = image.convert("RGB")
    pixels = np.array(image)

    channel_names = ["Red", "Green", "Blue"]
    results = {}

    for i, channel in enumerate(channel_names):
        values = pixels[:, :, i].flatten()

        counts = np.bincount(values, minlength=256)

        observed = []
        expected = []

        for j in range(0, 256, 2):
            pair_total = counts[j] + counts[j + 1]

            observed.extend([counts[j], counts[j + 1]])

            expected.extend([
                pair_total / 2,
                pair_total / 2
            ])

        observed = np.array(observed, dtype=float)
        expected = np.array(expected, dtype=float)

        valid = expected > 0

        chi_square = np.sum(
            (observed[valid] - expected[valid]) ** 2
            / expected[valid]
        )

        degrees_of_freedom = np.sum(valid) - 1

        p_value = chi2.sf(
            chi_square,
            degrees_of_freedom
        )

        results[channel] = {
            "chi_square": float(chi_square),
            "p_value": float(p_value)
        }

    return results