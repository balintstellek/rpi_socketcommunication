# Echo client program
import socket
import sys

HOST = '169.254.140.239'    # The remote host
PORT = 50007        # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        data = s.recv(1024)
        # s.settimeout(0.5)
        direction = data.decode('utf-8')
        sys.stdout.write(direction)