import socket 
import threading
import functionsAMS



if __name__ == "__main__":
    server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((socket.gethostname(),4000))

    server.listen(10)
    t1=threading.Thread(target=functionsAMS.menu())
    t2=threading.Thread(target=functionsAMS.menu(server))
    t1.start()
    t2.start()
    
