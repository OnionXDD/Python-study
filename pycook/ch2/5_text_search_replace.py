
"""2.5.
    Searching and Replacing Text
问题：
    文本匹配与替代
解决方法：
    str.replace
    re.sub 正则替换
"""
text = 'yeah, but no, but yeah, but no, but yeah'
print(text.replace('yeah','yep'))
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
import re
out = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
print(out)
# 以下是另一种方式，与直接调用re.sub等同
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
print(datepat.sub(r'\3-\1-\2', text))


from calendar import month_abbr
def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))
print(datepat.sub(change_date, text))
# 参数repl可以是一个参数或一个string
newtext, n = datepat.subn(r'\3-\1-\2', text)
print(newtext)
print(n)
# 返回匹配次数

