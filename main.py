"""
Create a new Tk module in python, that will output all images
and have the user choose which image to use as wallpaper...
"""

import os
import tkinter as tk
from PIL import Image, ImageTk

def open_image(image_path):
    """Open the selected image"""
    pass # code to use the selected image for your purpose

def select_image(event):
    """Select an image from the GUI"""
    global panel
    global current_image
    current_image = event.widget.cget("text")
    open_image(current_image)

root = tk.Tk()
root.title("Image Viewer")

images_folder = 'path/to/folder/with/images'

current_image = None

for image_file in os.listdir(images_folder):
    if image_file.endswith('.jpg') or image_file.endswith('.png'):
        # Open the image file
        image = Image.open(os.path.join(images_folder, image_file))

        # Resize the image to fit the GUI window
        image = image.resize((150, 150), Image.ANTIALIAS)

        # Create a PhotoImage object
        photo = ImageTk.PhotoImage(image)

        # Create a label for the image
        label = tk.Label(root, image=photo)
        label.image = photo  # Keep a reference to the image
        label.pack()

        # Attach a command to the label
        label.bind("<Button-1>", select_image)
        label.config(text=os.path.join(images_folder, image_file))

root.mainloop()
