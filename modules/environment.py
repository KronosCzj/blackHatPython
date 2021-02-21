#coding=utf-8
import os

#获取环境变量
def run(**args):
    print("[*] In environment module.")
    return str(os.environ)
