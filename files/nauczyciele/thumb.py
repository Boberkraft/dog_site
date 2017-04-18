from PIL import Image
import glob, os

size = 250, 250

for infile in glob.glob("img\\*.jpg"):
    file, ext = os.path.splitext(infile)
    im = Image.open(infile)
    im.thumbnail(size)
    im.save("tb\\tb_" + file[4:] + ".png", "PNG")

for infile in glob.glob("img\\*.png"):
    file, ext = os.path.splitext(infile)
    im = Image.open(infile)
    im.thumbnail(size)
    im.save("tb\\tb_"+ file[4:] + ".png", "PNG")