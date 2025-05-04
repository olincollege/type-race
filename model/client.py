"""
Networking code using socket for the client device.
"""

import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 5555))
while True:

    s.send("0".encode())
    data = s.recv(1024)
    print(f"Received {data!r}")
    time.sleep(0.1)
