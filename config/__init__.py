#!/usr/bin/evn python
# coding=utf-8

#遍历当前文件夹下的所有.py文件，然后用__import__导入到程序中
import os,sys
pro_path = os.path.split(os.path.realpath(__file__))[0]
sys.path.append(pro_path)
for root,dirs,files in os.walk(pro_path):
    # print('*****',root,dirs,files)
    for file in files:
        name,ext = os.path.splitext(file)
        # print('------',name,ext)
        if ext == '.py' and name != '__init__' and pro_path == root:
            __import__(name)

    for dir in dirs:
        # print('dir',dir)
        if dir != '.svn':
            try:
                # print('&&&&',__name__)
                __import__(__name__ + '.' + dir)
            except:
                pass
    break