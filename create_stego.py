from PIL import Image
import numpy as np

input_path = r"C:\Users\VARSHINI\Downloads\WhatsApp Image 2026-10-02 at 9.33.58 AM.jpeg"
output_path = "known_stego_large.png"

message = "STEGO_TEST_" * 10000

image = Image.open(input_path).convert("RGB")
pixels = np.array(image)

data = "".join(format(ord(char), "08b") for char in message)

flat_pixels = pixels.flatten()

for i, bit in enumerate(data):
    flat_pixels[i] = (flat_pixels[i] & 254) | int(bit)

stego_pixels = flat_pixels.reshape(pixels.shape)

stego_image = Image.fromarray(stego_pixels.astype(np.uint8))
stego_image.save(output_path)

print("Large known stego image created successfully.")
print("Message size:", len(message), "characters")
print("Saved as:", output_path)