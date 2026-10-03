from PIL import Image
import numpy as np


def analyze_lsb(image):
    image = image.convert("RGB")
    pixels = np.array(image)

    lsb = pixels & 1

    total_bits = lsb.size
    ones = np.sum(lsb)
    zeros = total_bits - ones

    ones_ratio = ones / total_bits
    zeros_ratio = zeros / total_bits

    imbalance = abs(ones_ratio - zeros_ratio)

    return {
        "total_bits": int(total_bits),
        "zeros": int(zeros),
        "ones": int(ones),
        "zeros_ratio": float(zeros_ratio),
        "ones_ratio": float(ones_ratio),
        "imbalance": float(imbalance)
    }