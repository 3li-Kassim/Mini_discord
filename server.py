import socket
import sys
import threading
import signal

clients = set()
clients_lock = threading.Lock()

def signal_handler(sig,frame):
    print("You pressed ctrl c")
    sys.exit(0)

signal.signal(signal.SIGINT,signal_handler)

host = "127.0.0.1"
port = 5050 
def listen_for_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(3)
        try:
            s.bind((host,port))
        except OSError as message:
            print(f"Bind failed. Error Code: {str(message[0])} Message {str(message[1])}")
            sys.exit()    
        s.listen()
        while True:
            try:
                client,addr = s.accept()
                print(f"accepted connection from {addr}")
                with clients_lock:
                    clients.add(client)
                threading.Thread(target=handle_client,daemon=False, args = (client,)).start()
                
                
            except socket.timeout:
                continue   

def handle_client(sock):
    try:
        while True:
            data = sock.recv(1024).decode()
            if not data:
                break
            else:
                print(repr(data))
                with clients_lock:
                    for c in clients:
                        if c == sock:
                            continue
                        else:
                            c.sendall(data.encode())

    finally:
        with clients_lock:
            clients.remove(sock)
            sock.close()                    
      
threading.Thread(target = listen_for_client, daemon= False).start()

print("Active threads: ", threading.active_count())  
