import sys
import glob
from PIL import Image

files = glob.glob('*.jpg')
image_size = (int)(sys.argv[1])

for f in files:
    Image.open(f).resize((image_size, image_size)).save(f, "JPEG", quality=100, optimize=True)