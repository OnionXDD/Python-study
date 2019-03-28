
"""1.17
    Extracting a Subset of a Dictionary
问题：
    从字典中抽取子集
解决方法：
    简单：简单字典判别（dictionary comprehension）
"""
prices ={
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
p1 = {key:value for key, value in prices.items() if value > 200}
tch_name = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
p2 = {key:value for key, value in prices.items() if key in tch_name}

print(p1)
print(p2)

