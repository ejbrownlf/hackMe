# Reverse Shell Connection

This is a little project that plays with hacking methodology of reverse shells.

The intention is to create scripts in python that will allow one of my devices to gain command line access to another one of my own computers from anywhere.

This is for educational and self learning purposes and not meant for any malicious means.

Steps to test yourself:

1. Make sure you have python installed on your machine
2. Clone this repository to your machine
3. Open two terminal windows
4. On the first terminal input `python3 host.py`
5. On the second terminal input `python3 client.py 127.0.0.1`
6. Return to your first terminal window and you will now have terminal access to the "client" machine
7. type in the command `exit` to close the session 

Running client.py with argument of 127.0.0.1 will just give you access to the machine you are currently using.

If you have more than one machine on your network you can input the private IPv4 Address to access it. You would run host.py on the "host" machine and client.py with the argument of the IP address of the attacker on the "client" machine.
