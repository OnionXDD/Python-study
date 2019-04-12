

"""2.1.
    Splitting Strings on Any of Multiple Delimiters
问题：
    当你要分割字符串，串中分隔符并不是一直存在的
解决方法：
    正则分割

"""
line = 'asdf fjdk; afed, fjek, asdf,     foo'
import re
# 输出按正则分割之后的结果
a = re.split(r'[;,\s]\s*', line)
print("list a = ",a)

# 同时输出分隔符
b = re.split(r'(;|,|\s)\s*',line)
print("list b = ",b)

# 将分隔符喝分割后语句重新拼接
values = b[::2]
delimiters = b[1::2]+['']
print(values)
print(delimiters)
print(''.join(v+d for v,d in zip(values,delimiters)))

# non-captured ;? 可以让你放弃掉捕获的第一个分隔符
print(re.split(r'(?:,|;|\s)\s*', line))

