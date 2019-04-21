

"""2.4.
    Matching and Searching for Text Patterns
问题：
    文本匹配
解决方法：
    str.find(),
    str.endswith(),
    str.startswith()
    re
"""
# text = 'yeah, but no, but yeah, but no, but yeah'
# print(text == 'yeah')
# print(text.startswith('yeah'))
# print(text.endswith('no'))
# print(text.find('no'))

text1 = '11/27/2012'
text2 = 'Nov 27, 2012'

import re
# if re.match(r'\d+/\d+/\d+',text1):
#     print('yes')
# else:
#     print('no')
#
# if re.match(r'\d+/\d+/\d', text2):
#     print('yes')
# else:
#     print('no')

datepat1 = re.compile(r'\d+/\d+/\d+')
# 使用单个括号，匹配一个完整语句
integrated_match = datepat1.match(text1)
print(integrated_match.group(0))
datepat2 = re.compile(r'(\d+)/(\d+)/(\d+)')
# 使用多个括号，分别匹配每个括号中的内容,并用一个groups安置
divided_match = datepat2.match(text1)

print('the date is ',divided_match.group(0),
divided_match.group(1), divided_match.group(2),
divided_match.group(3))

month, day , year = divided_match.groups() 

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
all_match = datepat2.findall(text)
print('findall',all_match)
for month, day, year in all_match:
    print('{}-{}-{}'.format(year, month, day))

for m in datepat2.finditer(text):
    print(m.groups())

'''
notice 一般来说使用多个括号就是把整个字符串按括号分开
此时的group(0)表示整体，1、2、3表示每个个体
如果你不用r' '可能需要在' '使用//来定义反斜杠负号
findall 返回一个元组列表， finditer返回迭代器
'''
