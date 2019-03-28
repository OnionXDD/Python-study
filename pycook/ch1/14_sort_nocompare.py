
"""1.14 Sorting Objects Without Native Comparison Support
    
    排序那些不支持自然比较的对象
    解决方法：在对象中增加一个可以callable 的键值
    
"""
class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)

users = [User(23), User(3), User(99)]

# 解法一
# sorted(users, key=lambda u: u.user_id)
# 解法二
from operator import attrgetter
sorted(users, key=attrgetter('user_id'))
print(users)
"""一般来说对对象使用attrgetter, 对字典使用itemgetter"""
