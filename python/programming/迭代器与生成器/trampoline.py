"""
协同程序是可以挂起、恢复，并且有多个进入点的函数。在python中，协同程序的替代者是线程，它可以实现代码块之间的交互，但是线程表现的是一种抢先式的风格，
所以必须注意资源锁，而协同程序不需要。这样代码可能变得相当复杂，难以创建和调试。但是生成器几乎就是协同程序
在协同程序之间的协作，最经典的例子就是接受来自到个客户的查询，并将每个查询委托给对此作出响应的新线程的服务器应用程序。要使用协同程序来实现这一模式，
首先要编写一个负责接受查询的协同程序（服务器），以及另外一个处理他们的协同程序（句柄）
"""
# -*- coding:utf-8 -*-
from __future__ import with_statement
from contextlib import closing
import socket
import multitask


def client_handler(sock):
    with closing(sock):
        while True:
            data = (yield multitask.recv(sock, 1024))
            if not data:
                break
            yield multitask.send(sock, data)


def echo_server(hostname, port):
    addrinfo = socket.getaddrinfo(hostname, port, socket.AF_UNSPEC, socket.SOCK_STREAM)
    (family, socktype, proto, cannoname, sockaddr) = addrinfo[0]
    with closing(socket.socket(family, socktype, proto)) as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(sockaddr)
        sock.listen(5)
        while True:
            multitask.add(client_handler((yield multitask.accept(sock))[0]))

if __name__=='__main__':
    import sys
    hostname = None
    port = 11111
    if len(sys.argv) >1:
        hostname = sys.argv[1]
    if len(sys.argv) > 2:
        port = int(sys.argv[2])
    multitask.add(echo_server(hostname, port))
    try:
        multitask.run()
    except KeyboardInterrupt:
        pass
