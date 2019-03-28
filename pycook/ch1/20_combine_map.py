

"""1.20
    Combining Multiple Mappings into a Single Mapping
问题：
    链式字典映射

"""

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}

from collections import ChainMap
c = ChainMap(a,b)
print(c['x'])
print(c['y'])
print(c['z'])

# 存在重复键值，可以使用new_child 和 parents

values = ChainMap()
values['x'] = 1
values = values.new_child()
values['x'] = 2
values = values.new_child()
values['x'] = 3

print(values)

print(values['x'])
values = values.parents
print(values['x'])
values = values.parents
print(values['x'])

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
# merged = dict(b)
# merged.update(a)
#
# print(merged['x'])
# print(merged['y'])
# print(merged['z'])

# a['x'] = 13
# print(merged['x'])
# update 子集合的改变不会映射到父集合

merged = ChainMap(a,b)
print(merged['x'])
a['x'] = 13
print(merged['x'])

# 链式map，子集合的改变会映射到父集合
