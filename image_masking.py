import cv2
import os
import glob
import numpy as np
from concurrent.futures import ThreadPoolExecutor

# Set up input and output directories
input_dir = r'Online-test'
output_dir = r'Online-test/mask'
os.makedirs(output_dir, exist_ok=True)

threshold_value = 200 
mask_pixel_value = 255  

# Function to process each image
def process_image(file_path):
    # Read image
    image = cv2.imread(file_path)
    if image is None:
        print(f"Image not found at {file_path}")
        return 0 

    mask = cv2.inRange(image, (threshold_value, threshold_value, threshold_value), (255, 255, 255))
    print(file_path)

    filename = os.path.basename(file_path)
    mask_filename = os.path.join(output_dir, os.path.splitext(filename)[0] + '_mask.png')
    cv2.imwrite(mask_filename, mask)
    
    return np.count_nonzero(mask == mask_pixel_value)

jpg_files = glob.glob(os.path.join(input_dir, '*.jpg'))

# Process images in parallel and sum up the 'max' pixel counts
with ThreadPoolExecutor() as executor:
    total_max_pixels = sum(executor.map(process_image, jpg_files))

print(f"Total 'max' pixels across all images: {total_max_pixels}")
