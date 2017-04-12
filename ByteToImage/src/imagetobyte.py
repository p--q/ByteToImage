#!/usr/bin/python3
# -*- coding: utf-8 -*-
import binascii
import os
import sys
import imghdr
import glob
def main():
    fd = "images"
    if not os.path.exists(fd):
        os.mkdir(fd)
        print("Please put the image file into the image folder you want to convert to the hexadecimal string.")
        sys.exit()
    os.chdir(fd)  
    for imagefile in glob.iglob("*.*"):
        imagetype = imghdr.what(imagefile)  # 画像の種類の取得。
        if imagetype:
            with open(imagefile,"rb") as fp:
                hexdata = binascii.b2a_hex(fp.read())  # 十六進法のバイト列に変換。
                print("\n" + fp.name)
                print(hexdata)
if __name__ == "__main__":
    sys.exit(main())