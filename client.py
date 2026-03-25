import socket
import queue
import threading
import client_gui

host = "127.0.0.1"
port = 5050 
msg_queue= queue.Queue()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def calling():
    sock.connect((host,port))    

calling()

def listening(sock):
    while True:
        data = sock.recv(1024).decode()
        if data:
            msg_queue.put(data) 

threading.Thread(target = listening, daemon = False, args=(sock,)).start()

gui = client_gui.MyGUI(msg_queue,sock)  






    

