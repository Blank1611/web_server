#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket
import select
import time
ip_port1 = ('127.0.0.1',8888)
ip_port2 = ('127.0.0.1',8889)

sk1 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sk1.bind(ip_port1)
sk1.listen(5)
sk1.setblocking(False)

sk2 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sk2.bind(ip_port2)
sk2.listen(5)
sk2.setblocking(False)

inputs = [sk1, sk2]
while True:
    rlist, wlist, eList = select.select(inputs,[], [], 1)
    print("inputs:", inputs)
    print("rlist:", rlist)
    for r in rlist:
        conn, address = r.accept()
        data = conn.recv(1024)
        print data, "from:", address
        conn.close()
    print "---"


