#!/usr/bin/env python3
# Path: wal.py
"""
This module uses tkinter to output a GUI with the images in the folder
given. The folder has 100x100 resolution images, but those aren't the
images used for the wallpaper. The images used for the wallpaper are
the ones in another folder, same images but they are 1920x1080
resolution images. The ones that are 100x100, contain basically the same
names with the higher resolution ones, but with a prefix and suffix.
The suffixes are .png and are automatically provided by the tkinter
module, even if the images were initially .jpg, or .svg or .jpeg. or
any other format.

The prefix is added by the user, and is the same for all the images in
the folder. The prefix is added to the image name, and the suffix is
added by the tkinter resizing library. To use the images for the wallpaper,
the prefix and suffix are removed from the image name, and the image is
opened with the wal command, only after the folder path with the original
images is added to the image name.

E.g the image name is new/1.jpg.png, and the prefix is new/, and the suffix
is .png. The image name is changed to 1.jpg, and the folder path is added
so that the image now becomes /home/user/Pictures/1.jpg. The image is then
used by wal to change the wallpaper.

The images are selected by clicking on them, and the wallpaper is changed.

@ I am also thinking of adding more core usage on this just to cut the
few ms delay shown. I am thinking of using the multiprocessing module
to run the wal functions in separate processes, and then kill the processes
after the wallpaper is changed. This will reduce the delay, but I am not
sure if it will work. I will try it out and see if it works.

If you have any improvements on the gui module, such as how the module can
be made scrollable, or how the images can be resized to fit the window, or just
any improvements or comments, please let me know.

I would love to hear from you.

Thank You 💗💗💗💗💗.
"""

import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


PATH_SUFFIX = '/home/ephantus/sub_anime/'
# Path to the folder containing the images with the higher resolution

PATH_PREFIX = '/home/ephantus/new_files/new-'
# Path to the folder containing the images with the 100x100 resolution


def open_image(image_path: str):
    """Change the wallpaper"""
    # code to use the selected image for your purpose
    # Here I am using wal because I am on a linux system.
    # The command wal is used to change wallpapers, same as {feh --bg-fill}
    # and others. Don't know the command for windows...
    # Changing wallpapers on windows cmd uses the command os.system("rundll32")
    # Or sth. Don't know, that is generated by Copilot

    os.system(f'wal -qi {image_path}')


def add_and_remove_prefix_and_suffixes(text: str,
                                       prefix_add: str,
                                       prefix_rem: str, suffix: str):
    """Module adds and removes whatever prefixes and suffixes necessary"""
    text = remove_prefix(text, prefix_rem)
    text = add_prefix(text, prefix_add)
    text = remove_suffix(text, suffix)

    return text


def select_image(event):
    """Select an image from the GUI"""
    current_img = event.widget.cget("text")
    curr_img = add_and_remove_prefix_and_suffixes(current_img, PATH_SUFFIX,
                                                  PATH_PREFIX, '.png')

    open_image(curr_img)


# Function to remove the prefix new/ from the image name
def remove_prefix(text: str, prefix: str):
    """Function to remove a prefix from a string value"""
    if text.startswith(prefix):
        return text[len(prefix):]
    return text


# Function to remove suffixes from the image name from the last
def remove_suffix(text: str, suffix: str):
    """Function to remove a suffix from a string value"""
    if text.endswith(suffix):
        return text[:-len(suffix)]
    return text


# Function to add a prefix to image name
def add_prefix(text, prefix):
    """Function to add a prefix to a string value"""
    return prefix + text


root = tk.Tk()
root.title("Image Viewer")

# Folder containing the images with the 100x100 resolution
images_folder: str = '/home/ephantus/new_files'

# Find out how many files in the folder contain .png and .jpg files
num_files: int = len([f for f in os.listdir(images_folder)
                      if f.endswith('.png') or f.endswith('.jpg')])

# Width of the frame should be 150 * 7
width: int = 100 * 10

# Height must be 150 * (num_files / 10)
height: int = round(100 * (num_files / 10)) + 100

# Give the window a width and a height
# And make resizable to be false
root.geometry(f"{width+20}x{height}")
root.resizable(False, False)

# Create a scrollable frame
frame = tk.Frame(root)
frame.grid()

# Create a canvas on the frame
canvas = tk.Canvas(frame)

# I do not think this shit is necessary any more
# ############# FROM HERE ##################################
# But here it shall remain for a while

# Create a scrollbar and associate it with the frame
yscrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)

canvas.configure(yscrollcommand=yscrollbar.set)

yscrollbar.pack(side="right", fill="y")

canvas.configure(yscrollcommand=yscrollbar.set)

# ############# TO HERE ##################################

canvas.pack(side="left", fill="both", expand=True)


NEW_COUNTER = 1
ROW_COUNTER = 0
COL_COUNTER = 0


for image_file in os.listdir(images_folder):
    if image_file.endswith('.jpg') or image_file.endswith('.png'):

        NEW_COUNTER += 1
        # Open the image file
        image = Image.open(os.path.join(images_folder, image_file))

        # Create a PhotoImage object
        photo = ImageTk.PhotoImage(image)

        # Create a label for the image
        label = ttk.Label(canvas, image=photo)
        label.image = photo  # Keep a reference to the image
        # Error on the above line ({on the editor only, not when running}),
        # but it works...
        # The error states 'Cannot assign member "image" for type `label`'
        # Without it, the code fails...

        label.grid(row=ROW_COUNTER, column=COL_COUNTER)

        # Attach a command to the label
        label.bind("<Button-1>", select_image)
        label.config(text=os.path.join(images_folder, image_file))

        # After the first 10 images, move to the next row
        COL_COUNTER += 1

        # Displays 10 images per row
        if NEW_COUNTER % 10 == 0:
            ROW_COUNTER += 1
            COL_COUNTER = 0


root.mainloop()
