"""
    1.set() 函数中会先调用对象的 __hash__() 方法，获取 hash 结果；
    2.如果 hash 结果相同，用比较操作符 == （也就是调用函数 __eq__()）判断二者的值是否相等；
    3.如果都相等，去重；否则，set() 认为二者不同，两个都保留到结果中。
"""


class Person(object):
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    def __eq__(self, other):    # other为另一个比较的对象
        print(other)
        return self.name == other.name and self.sex == other.sex and self.age == other.age

    def __hash__(self):  # 实现此方法的对象才是可hashable对象
        return hash((self.name, self.sex, self.age))


p0 = Person('Levis', 'male', 25)
p1 = Person('Levis', 'male', 25)
print(id(p0), id(p1))  # 4309287360 4309513216
print(hash(p0) == hash(p1))  # True
print(set([p0, p1]))  # {<__main__.Person object at 0x100da81c0>}
