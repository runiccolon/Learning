"""
    singledispatch 机制的一个显著特征是，你可以在系统的任何地方和任何模块中注册专门函数。
    如果后来在新的模块中定义了新的类型，可 以轻松地添加一个新的专门函数来处理那个类型。
    此外，你还可以为不 是自己编写的或者不能修改的类添加自定义函数。
"""

from functools import singledispatch
from collections import abc
import numbers
import html


@singledispatch
def htmlize(obj):
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)


@htmlize.register(str)
def _(text):
    content = html.escape(text).replace('\n', '<br>\n')
    return '<p>{0}</p>'.format(content)


@htmlize.register(numbers.Integral)
def _(n):
    '''
    为每个需要特殊处理的类型注册一个函数。numbers.Integral 是 int 的虚拟超类。
    :param n:
    :return:
    '''
    return '<pre>{0} (0x{0:x})</pre>'.format(n)


@htmlize.register(tuple)
@htmlize.register(abc.MutableSequence)
def _(seq):
    inner = '</li>\n<li>'.join(htmlize(item) for item in seq)
    return '<ul>\n<li>' + inner + '</li>\n</ul>'


print(htmlize(123))
