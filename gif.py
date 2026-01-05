import sys

from PIL import Image
images=[] # This list will store image objects, not filenames, not paths, actual loaded images.
for arg in sys.argv[1:]: #[1:]: slice starting from index 1
#  This removes 'gif.py' and keeps only image filenames
    image=Image.open(arg) # Will open the image file specified by arg this is PIL library thing means it will load the image into memory
    images.append(image)

images[0].save(
    "gif.gif",save_all=True, append_images=images[1:], loop=0,duration=200
)
"""
Line-by-line explanation of the GIF creation script

import sys
- Imports the built-in sys module
- Used to access command-line arguments via sys.argv

from PIL import Image
- Imports the Image class from the PIL module (provided by Pillow)
- Used to open, manipulate, and save images

images = []
- Creates an empty list
- This list will store Image objects (not filenames)

for arg in sys.argv[1:]:
- Loops through command-line arguments starting from index 1
- sys.argv[0] is the script name, so it is skipped
- Each arg is expected to be an image filename

    image = Image.open(arg)
    - Opens the image file specified by arg
    - Loads it into memory as an Image object

    images.append(image)
    - Adds the Image object to the images list

images[0].save(
- Uses the first image as the base frame of the GIF

    "gif.gif",
    - Name of the output GIF file

    save_all=True,
    - Ensures all frames are saved
    - Required for animated GIFs

    append_images=images[1:],
    - Appends the remaining images as additional frames
    - images[1:] is a list of all images except the first

    loop=0,
    - Controls how many times the GIF repeats
    - 0 means infinite looping

    duration=200
    - Time each frame is displayed in milliseconds
    - 200 ms = 0.2 seconds per frame
)
"""
