"""
groupby:uniq 这个函数有点像Unix命令uniq。它可以对来自一个迭代器的重复元素进行分组，只要它们是相邻的，还可以提供另一个函数来执行元素的比较。
否则，将采用标识符比较。groupby的一个应用实例是使用行程长度编码（RLF）来压缩数据。字符串中的每组相邻的重复字符将替换成该字符本身和重复次数。
如果字符没有重复，则使用1
"""

from itertools import groupby

def compress(data):
    return ((len(list(group)),name) for name ,group in groupby(data))

def decompress(data):
    return (car * size for size,car in data)

a = list(compress('get uuuuuuuuuuuuuuuuup'))
compressed = compress('get uuuuuuuuuuuuuup')
b = ''.join(decompress(compressed))
