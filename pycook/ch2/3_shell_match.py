

"""2.3.
    Matching Strings Using Shell Wildcard Patterns
问题：
    unix shell 通配符匹配
解决方法：
    fnmatch(), fnmatchcase()

"""

from fnmatch import fnmatch, fnmatchcase

# match a filename
print(fnmatch('foo.txt', '*.txt'))
print(fnmatch('foo.txt', '?oo.txt'))
print(fnmatch('Dat45.csv', 'Dat[0-9]*'))

names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
print([name for name in names if fnmatch(name, 'Dat*.csv')])

addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY',
]
a = [addr for addr in addresses if fnmatchcase(addr, '* ST')]
print(a)
b = [addr for addr in addresses if fnmatchcase(addr, '54[0-9][0-9] *CLARK*')]
print(b)
'''
    fnmatch 和 fnmatchcase 的区别是一个靠底层调用来匹配（可能会有大小写问题）
    fnmatchcase严格按照所提供的大小写匹配
'''

