"""
This module checks whether there is already a new picture
in the folder sub_anime, that is not yet converted to
a resolution of 100x100, if there is, It converts the image
and stores it in the folder new_files, if there isn't, the wal.py
module runs as usual.

"""

import os

from PIL import Image


def convert_uniq_files(source_folder: str, dest_folder: str) -> None:
    """Checks for unique images in source folder and converts them to a
    resolution of 100x100 and stores them in the destination folder.
    """

    uniq_img_lst: list = [file for file in os.listdir(source_folder)
                          if file not in os.listdir(dest_folder)]

    for image in uniq_img_lst:
        if image.endswith('.png') or image.endswith('.jpg'):

            img = Image.open(f'{source_folder}/{image}')
            img = img.resize((100, 100), Image.Resampling.LANCZOS)
            img.save(f'{dest_folder}/new-{image}.png')


def main():
    """Just the main function"""

    source: str = '/home/ephantus/sub_anime'
    destin: str = '/home/ephantus/new_files'

    convert_uniq_files(source, destin)


if __name__ == "__main__":
    main()
