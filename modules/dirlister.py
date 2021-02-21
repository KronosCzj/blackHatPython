#coding=utf-8
import os

#列举当前目录下的所有文件
def run(**args):
    print("[*] In dirlister module.")
    files = os.listdir(".")
    return str(files)