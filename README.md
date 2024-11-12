# ParallelImageMask
This script processes JPG images by creating binary masks where pixels are set to 255 if their RGB values exceed 200. Each mask is saved as a lossless PNG, and the total count of these "max" pixels is logged. Using parallel processing, it efficiently handles large datasets by processing images concurrently.
