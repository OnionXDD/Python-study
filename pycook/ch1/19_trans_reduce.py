
"""1.19
    Transforming and Reducing Data at the Same Time
问题：
    转换与聚集函数

"""
nums = [1, 2, 3, 4, 5]
s = sum(x*x for x in nums)
print(s)

# Determine if any .py exists in a directory
import os
files = os.listdir('dirname')
if any(name.endswith('.py') for name in files):
    print('There be python !')
else:
    print('Sorry, no python.')

# Output a tuple as CSV
s = ('ACME',  50, 123.45)
print(','.join(str(x) for x in s))

# Data reduction across fields of a data structure
portofolio = [
    {'name':'GOOG', 'shares':50},
    {'name':'YHOO', 'shares':75},
    {'name':'AOL', 'shares':20},
    {'name':'SCOX', 'shares':65}
]
min_shares = min(s['shares'] for s in portofolio)
print(min_shares)

# Alternative:Returns {'name': 'AOL', 'shares': 20}
min_shares = min(portofolio, key=lambda s:s['shares'])

