"""
迭代器将消费其处理的序列，但他不会往回处理。tee提供了一个序列之上运行多个迭代器的模式
"""
import itertools

def with_head(iterable, headsize=1):
    a, b = itertools.tee(iterable)
    return list(itertools.islice(a, headsize)) , b

seq = [1, 2, 3, 4]
a, b = with_head(seq, 4)
