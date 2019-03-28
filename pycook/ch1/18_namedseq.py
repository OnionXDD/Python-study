

"""1.18
    Mapping Names to Sequence Elements
问题：
    通过名字匹配序列元素
解决方法：
    使用collections.namedtuple()
"""
from collections import namedtuple

Subscriber = namedtuple('Subscriber',['addr', 'joined'])
sub = Subscriber('jonesy@example.com', joined='2012-10-19')
print(sub.addr)
print(sub.joined)

addr, joined = sub

Stock = namedtuple('Stock', ['name', 'shares', 'price'])

def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        print(s.shares)
        print(s.price)
        total += s.shares * s.price
    return total

a = [('IBM', 50, 60)]
print(compute_cost(a))
# compute_cost need argument like [()] or [[]]

s = Stock('AC<E', 100, 123.45)
print(s)
# change the element in the tuple, you can't change it like s.shares = 60

s = s._replace(shares=60)
print(s)



Stock = namedtuple('Stock', ['name', 'shares', 'price',
                             'date', 'time'])
# Create a prototype instance
stock_prototype = Stock('', 0, 0.0, None, None)

# Function to convert a dictionary to a Stock
def dict_to_stock(s):
    return stock_prototype._replace(**s)
a = {'name':'ACME', 'shares':100, 'price':123.45}
print(dict_to_stock(a))
b = {'name':'ACME', 'shares':100, 'price':123.45, 'date':'12/17/2012'}
print(dict_to_stock(b))



