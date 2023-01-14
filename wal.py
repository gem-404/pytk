# Path: wal.py
"""
Create a new wal module in python, that will output all images
and have the user choose which image to use as wallpaper...
"""

import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


def open_image(image_path):
    """Open the selected image"""
    # code to use the selected image for your purpose
    os.system(f'wal -qi {image_path}')


def select_image(event):
    """Select an image from the GUI"""
    global panel
    global current_image
    current_image = event.widget.cget("text")
    open_image(current_image)


root = tk.Tk()
root.title("Image Viewer")

images_folder = '/home/ephantus/sub_anime'

# Find out how many files in the folder contain .png and .jpg files
num_files = len([f for f in os.listdir(images_folder)
                 if f.endswith('.png') or f.endswith('.jpg')])

# Width of the frame should be 150 * 7
width = 100 * 10

# Height must be 150 * (num_files / 10)
height = round(100 * (num_files / 10)) + 100

root.geometry(f"{width+20}x{height}")

root.resizable(False, False)

# Create a scrollable frame
frame = tk.Frame(root)
frame.grid()

# Create a canvas on the frame
canvas = tk.Canvas(frame)

# Create a scrollbar and associate it with the frame
yscrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)

canvas.configure(yscrollcommand=yscrollbar.set)

yscrollbar.pack(side="right", fill="y")

canvas.configure(yscrollcommand=yscrollbar.set)

canvas.pack(side="left", fill="both", expand=True)

current_image = None

new_counter = 1
row_counter = 0
col_counter = 0


for image_file in os.listdir(images_folder):
    if image_file.endswith('.jpg') or image_file.endswith('.png'):

        new_counter += 1
        # Open the image file
        image = Image.open(os.path.join(images_folder, image_file))

        # Resize the image to fit the GUI window
        image = image.resize((100, 100), Image.Resampling.LANCZOS)

        # Create a PhotoImage object
        photo = ImageTk.PhotoImage(image)

        # Create a label for the image
        label = ttk.Label(canvas, image=photo)
        label.image = photo  # Keep a reference to the image
        label.grid(row=row_counter, column=col_counter)

        # Attach a command to the label
        label.bind("<Button-1>", select_image)
        label.config(text=os.path.join(images_folder, image_file))

        # After the first 10 images, move to the next row
        col_counter += 1

        if new_counter % 10 == 0:
            row_counter += 1
            col_counter = 0


root.mainloop()
