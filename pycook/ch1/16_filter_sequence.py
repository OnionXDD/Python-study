

"""1.16
    Filtering Sequence Elements
问题：
    过滤序列元素，想要提取或者过滤序列中的默写元素
解决方法：
    简单：简单列表判别
    专业：使用迭代器，以免占用过多资源
"""
# 简单方法
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
a = [n for n in mylist if n > 0]
b = [n for n in mylist if n < 0]
print(a)
print(b)

# 专业方法
pos = (n for n in mylist if n > 0)
print(pos)
for x in pos:
    print(x)

# 输出序列中满足要求的数字，将不满足的用0替代
clip_pos = [n if n > 0 else 0 for n in mylist]
clip_neg = [n if n < 0 else 0 for n in mylist]

# 字符串条件过滤 itertool-compress
address = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]
from itertools import compress
counts = [0, 3, 10, 4, 1, 7, 6, 1]
more5 = [n > 5 for n in counts]
print(list(compress(address, more5)))




