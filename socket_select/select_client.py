#!/usr/bin/env python
# coding:utf-8
import socket
ip_port = ('127.0.0.1', 8888)

sk = socket.socket()
sk.connect(ip_port)

sk.sendall("data to 8888")

sk.close()