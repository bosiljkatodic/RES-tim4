import socket
from unicodedata import name

if __name__== "__main__":

    server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #klijentska str tcp
    server.connect((socket.gethostbyname(), 4000))

    #serverska strana tcp
    server2=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server2.bind((socket.gethostbyname(),5000))

    server2.listen(10);