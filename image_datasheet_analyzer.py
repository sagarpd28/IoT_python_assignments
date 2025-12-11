import os
import csv
from PIL import Image
import matplotlib.pyplot as plt

# Folder path
folder_path = "D:\images"

# List to store image info
image_info = []

# Read all .jpg and .png files
for filename in os.listdir(folder_path):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        img_path = os.path.join(folder_path, filename)

        # Open image
        img = Image.open(img_path)
        width, height = img.size

        # 3. Display image
        plt.imshow(img)
        plt.title(f"{filename} ({width}x{height})")
        plt.axis('off')
        plt.show()

        # ---> ADD THIS PART <---
        img.close()    # closes the file and prevents memory leak
        # ------------------------

        # Store details in dictionary
        image_info.append({
            "filename": filename,
            "width": width,
            "height": height,
            "area": width * height
        })

# Determine largest & smallest images by area
largest_image = max(image_info, key=lambda x: x['area'])
smallest_image = min(image_info, key=lambda x: x['area'])

print("Largest Image:", largest_image)
print("Smallest Image:", smallest_image)

# Save into a CSV file
csv_path = "image_sizes.csv"

with open(csv_path, "w", newline="") as csvfile:
    fieldnames = ["filename", "width", "height", "area"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for info in image_info:
        writer.writerow(info)

print(f"CSV file saved as {csv_path}")
