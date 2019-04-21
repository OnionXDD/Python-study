
"""2.2.
    Matching Text at the Start or End of a String
问题：
    匹配头部字符串或尾部字符串
解决方法：
    str.startswith()  or  str.endswith()
    或者使用切片，正则表达式匹配

"""
filename = 'file: spam.txt'

print(filename.endswith('.txt'))
print(filename.startswith('file:'))

url = 'http://www.python.org'
print(url.startswith('http'))

import os
# os.listdir  list你指定目录下的文件与文件夹
# filename = os.listdir('.').这里我们直接将值赋予给filenames
filenames = ['Makefile', 'foo.c', 'bar.py', 'spam.c', 'spam.h']
print([name for name in filenames if name.endswith(('.c','.h'))])
print(any(name.endswith('.py') for name in filenames))

'''read_data:
    if the path is url, open it and return read
    else open file of the path
'''
from urllib.request import urlopen
def read_data(name):
    if name.startswith(('http:', 'https:', 'ftp:')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()

#startswith or endswith only use tuple to convert variable

