
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
    # Store the images in the folder images_folder
    # in another folder, with 100x100 resolution
    images_folder = '/home/ephantus/sub_anime'
    destin_folder = '/home/ephantus/new_files'

    store_images(images_folder, destin_folder)


if __name__ == "__main__":
    main()
