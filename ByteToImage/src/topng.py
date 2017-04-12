#!/home/pq/anaconda3/bin/python
# -*- coding: utf-8 -*-
from PIL import Image
import imghdr
import os
import sys
import glob
def main():
    fd = "images"
    output = "Output"
    if not os.path.exists(fd):
        os.mkdir(fd)
        print("Please put the image file into the image folder you want to convert to the other image format.")
        sys.exit()
    if not os.path.exists(output):
        os.mkdir(output)    
    output = os.path.join("..",output)    
    os.chdir(fd)  
    for imagefile in glob.iglob("*.*"):
        imagetype = imghdr.what(imagefile)
        if imagetype:
            img = Image.open(imagefile)
            name,ext = os.path.splitext(imagefile)
            img.save(os.path.join(output,name + ".png"),"png")
if __name__ == "__main__":
    sys.exit(main())