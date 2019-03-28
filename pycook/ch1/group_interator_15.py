

"""1.15
    Grouping Records Together Based on a Field
    分组迭代
    解决方法:使用itertools.groupby()
"""

rows = [
        {'address': '5412 N CLARK', 'date': '07/01/2012'},
        {'address': '5148 N CLARK', 'date': '07/04/2012'},
        {'address': '5800 E 58TH', 'date': '07/02/2012'},
        {'address': '2122 N CLARK', 'date': '07/03/2012'},
        {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
        {'address': '1060 W ADDISON', 'date': '07/02/2012'},
        {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
        {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

from operator import itemgetter
from itertools import groupby
# Sort by the desired field first
# 先按标签‘date’分类排序
rows.sort(key=itemgetter('date'))
print(rows)
for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in items:
        print('   ',i)
# 类似sql语句，先将列表中字典按date排序，然后遍历每个date的item

from collections import defaultdict
rows_by_date = defaultdict(list)
for row in rows:
    rows_by_date[row['date']].append(row)

for r in rows_by_date['07/01/2012']:
    print(r)
"""这里使用defaultdict, 我们可以使字典中的
    一个键值对应一个列表，并且向列表里添加元素
"""
