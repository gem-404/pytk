+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+                           CODE BY GEM-404                           
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

-------------------------------------------------------------------------
# new_wal_res.py

This code is used to create a images with 100x100 resolution
from a source folder to some destination folder. The images are
then used to by a GUI to change the wallpaper of the system.


------------------------------------------------------------------------
# wal.py

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

If you have any improvements on the tkinter module, such as how the module can
be made scrollable, or how the images can be resized to fit the window, or just
any improvements or comments, please let me know.

I would love to hear from you.

-----------------------------------------------------------------------------
                            Thank You 💗💗💗💗💗.
