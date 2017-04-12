#!/usr/bin/python3
# -*- coding: utf-8 -*-
import imghdr
import os
import sys
import glob
import shutil
import subprocess
def main():
    fd = "images"
    output = "Output"  # PNG画像出力フォルダ
    if not shutil.which("convert"):  # convertコマンドの有効を確認。
        print("The convert command must be valid for execution.\n Please install imagemagick.")
        sys.exit()
    if not os.path.exists(fd):
        os.mkdir(fd)
        print("Please put the bmp image icon for LibreOffice into the image folder you want to convert to the png image icon.")
        sys.exit()
    if not os.path.exists(output):
        os.mkdir(output)    
    output = os.path.join("..",output)    
    os.chdir(fd)  
    for imagefile in glob.iglob("*.*"):
        imagetype = imghdr.what(imagefile)  # 画像の種類を取得。
        if imagetype == "bmp":
            name,ext = os.path.splitext(imagefile)
            args = ["convert"]
            args.extend(["-transparent",'magenta'])  # Magendaは透明にする。
            args.extend([imagefile,os.path.join(output,name + ".png")])
            subprocess.run(args) 
if __name__ == "__main__":
    sys.exit(main())