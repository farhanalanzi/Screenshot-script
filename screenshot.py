#!/usr/bin/env python3
"""
Screenshot script that captures screen, creates B&W and inverted versions,
and compresses all images into a ZIP file.
"""

from PIL import ImageGrab
import os
from zipfile import ZipFile
from datetime import datetime

# Take full-screen screenshot
screenshot = ImageGrab.grab()

# Generate timestamp for unique filenames
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
original_file = f"original_{timestamp}.png"
bw_file = f"bw_{timestamp}.png"
inverted_file = f"inverted_{timestamp}.png"
zip_file = f"screenshots_{timestamp}.zip"

# Save original image
screenshot.save(original_file)
print(f"Saved original: {original_file}")

# Convert to black and white (grayscale)
bw_image = screenshot.convert("L")
bw_image.save(bw_file)
print(f"Saved B&W: {bw_file}")

# Invert the black and white image
inverted_image = bw_image.point(lambda x: 255 - x)
inverted_image.save(inverted_file)
print(f"Saved inverted: {inverted_file}")

# Compress all three images into a ZIP file
with ZipFile(zip_file, 'w') as zipf:
    zipf.write(original_file)
    zipf.write(bw_file)
    zipf.write(inverted_file)
print(f"Created ZIP: {zip_file}")

# Clean up individual image files
os.remove(original_file)
os.remove(bw_file)
os.remove(inverted_file)
print("Cleaned up individual image files")

print(f"\nDone! All images compressed in: {zip_file}")


