

"""2.6.
    Searching and Replacing Case-Insensitive Text
问题：
    搜索替换大小写不敏感的文本

解决方法：
    使用re.IGNORECASE flag to various operations.

"""
import re
text = 'UPPER PYTHON, lower python, Mixed Python'
print(re.findall('python', text, flags=re.IGNORECASE))
print(re.sub('python', 'snake', text, flags=re.IGNORECASE))

# 想要按原来的方式设置替换后的单词格式。
def matchcase(word):
    def replace(m): # 这里的m表达的是匹配到的一整个序列
        text = m.group()
        print(text)
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace # return 函数名 重复执行该函数。


print(re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE))

