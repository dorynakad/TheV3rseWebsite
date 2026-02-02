from PIL import Image
import os

img_path = "glitchcut_000/glitchcut_000.jpg"
if os.path.exists(img_path):
    with Image.open(img_path) as img:
        print(f"Size: {img.size}")
else:
    print("File not found")
