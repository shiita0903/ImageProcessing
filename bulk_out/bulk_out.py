import os
import sys
import glob
from PIL import Image

files = glob.glob('*.jpg')

for f in files:
    img = Image.open(f)
    ftitle, fext = os.path.splitext(f)
    img.transpose(Image.ROTATE_90).save(ftitle + '_1' + fext, "JPEG", quality=100, optimize=True)
    img.transpose(Image.ROTATE_180).save(ftitle + '_2' + fext, "JPEG", quality=100, optimize=True)
    img.transpose(Image.ROTATE_270).save(ftitle + '_3' + fext, "JPEG", quality=100, optimize=True)

    img = img.transpose(Image.FLIP_LEFT_RIGHT)
    img.save(ftitle + '_4' + fext, "JPEG", quality=100, optimize=True)
    img.transpose(Image.ROTATE_90).save(ftitle + '_5' + fext, "JPEG", quality=100, optimize=True)
    img.transpose(Image.ROTATE_180).save(ftitle + '_6' + fext, "JPEG", quality=100, optimize=True)
    img.transpose(Image.ROTATE_270).save(ftitle + '_7' + fext, "JPEG", quality=100, optimize=True)