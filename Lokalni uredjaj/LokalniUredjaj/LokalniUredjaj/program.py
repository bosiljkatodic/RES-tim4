import socket
from unicodedata import name

if __name__ == "__main__":
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostbyname(),4000))
    msg=s.recv(1024)
