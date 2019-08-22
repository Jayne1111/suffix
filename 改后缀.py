#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os

path = r'D:\test'


files = os.listdir(path)  # 列出当前目录下的所有文件

for filename in files:
    portion = os.path.splitext(filename)  # 分离文件名字和后缀

    if portion[1] == ".txt":      # 根据后缀来修改，如无后缀则空
        newname = portion[0]+".mp4"   # 要改的新后缀

        os.chdir(path)
        os.rename(filename,newname)
        print('OK')
