import glob
import src

formats = ['*.jpg', '*.png', '*.bmp', '*.gif', '*.tif', '*.tiff']
wall = src.Wallpaper.Wallpaper()

directory = wall.path()
timer = wall.delay()

# For the images to be displayed indefinitely, the configuration has to be run in an infinite loop.
while 1:
    for format in formats:
        pictureDirectory = glob.glob(directory + format)
        for picture in pictureDirectory:
            wall.run(picture, timer)
