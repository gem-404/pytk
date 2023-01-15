#!usr/bin/env python3
"""
This code is used to create a images with 100x100 resolution
from a source folder to some destination folder. The images are
then used to by a GUI to change the wallpaper of the system.
"""

import os
from PIL import Image


# Store the images in images_folder in another folder,
# with 100x100 resolution, but add the word new/
# to their original name
def store_images(image_folder: str, dest_folder: str):
    """Store the images in another folder with 100x100 resolution"""
    for image in os.listdir(image_folder):
        if image.endswith('.png') or image.endswith('.jpg'):
            img = Image.open(f'{image_folder}/{image}')
            img = img.resize((100, 100), Image.Resampling.LANCZOS)
            img.save(f'{dest_folder}/new-{image}.png')


def main():
    """Just the main function, nothing special"""
    # Store the images in the folder images_folder
    # in another folder, with 100x100 resolution

    images_folder: str = '/home/ephantus/sub_anime'  # Source folder
    destin_folder: str = '/home/ephantus/new_files'  # Destination folder

    store_images(images_folder, destin_folder)


if __name__ == "__main__":
    main()
