"""
islice 窗口迭代器，islice将返回一个运行在序列的子分组之上的迭代器。
下面的实例将按照从标准输入中读取信息，并且输出从第5行开始的每行元素，只要该行的元素超过4个
"""

import itertools

def starting_at_five():
    value= input().strip()
    while value != '':
        for el in itertools.islice(value.split(),4,None):
            yield el
        value=input.strip()

iter=starting_at_five()
