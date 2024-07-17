# Image Cropper Driver

import os
from PIL import Image
import image_cropper    # Class

def main():
    # Remove existing files in 'pdf_files' directory
    pdf_directory = 'pdf_files/'
    pdf_files = os.listdir(pdf_directory)
    for filename in pdf_files:
        os.remove(pdf_directory + filename)

    # Crop and convert each image file in 'image_files' directory and save new file in 'pdf_files' directory
    image_directory = 'image_files/'
    image_files = os.listdir(image_directory)
    for filename in image_files:
        if filename[-3:] in ['jpg', 'jpeg']:
            original_image = Image.open(image_directory + filename)
            image_cropper_instance = image_cropper.image_cropper()  # Create an Image Cropper object from Image Cropper class
            new_image = image_cropper_instance.crop(original_image)
            new_image.save(pdf_directory + filename[:-3] + 'pdf')   # Optional: DPI=(x, y)



main()