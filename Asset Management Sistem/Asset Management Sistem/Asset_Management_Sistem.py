import socket 

if __name__ == "__main__":
    server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((socket.gethostbyname(),4000))

    server.listen(10);

    while True:
        clientSocket, address=server.accept()
        print(f"Connesciton from {address} has been established!")
