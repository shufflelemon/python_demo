# -*- coding: UTF-8 -*-

import os

# 读取指定目录下的文件，并将文件内容按行读取后，放到列表中。
file_dir = "/Users/liangmengmeng/lmm/cdn/zhihu/preheat_dir/"
for dirpath, dirnames, files in os.walk(file_dir):
    for file in files:
        # file是文件名，如果要打开需要加上前面的路径
        f_in = open(file_dir + file, 'r')
        # splitlines方法可以按照行隔开，并去除每行末尾的换行符
        lines = f_in.read().splitlines()
        print type(lines)
        print lines

        urls = lines
        f_in.close()