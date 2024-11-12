Parallel Image Masking Tool
This repository provides a Python script that processes JPG images in bulk by creating binary masks based on RGB thresholds. It saves each mask as a PNG file and logs the total count of "max" pixels, using parallel processing for efficiency.

Features
Binary Mask Generation: Creates a mask where pixels are set to 255 if their RGB values exceed 200.
Lossless Output: Saves each mask image as a PNG.
Pixel Counting: Logs the total count of "max" pixels across all images.
Parallel Processing: Handles large datasets efficiently with multi-threading.
Requirements
Python 3.x
OpenCV (cv2)
NumPy
Install dependencies:

bash
Copy code
pip install opencv-python numpy
Usage
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/ParallelImageMaskingTool.git
cd ParallelImageMaskingTool
Prepare Input Directory: Place your JPG images in an input folder.

Run the Script:

bash
Copy code
python image_masking.py
Check Output: Mask images are saved as PNG files in the specified output folder. The script logs the total number of "max" pixels.

Script Overview
The script performs the following steps:

Reads each image and checks if all RGB channels exceed the threshold of 200.
Creates a binary mask for qualifying pixels.
Saves the mask image in PNG format to retain quality.
Logs the count of pixels that meet the threshold across all images.
Example
Input: JPG images in input_folder/
Output: PNG masks in output_folder/ and a log of total "max" pixels.
