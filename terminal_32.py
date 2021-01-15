import socket, pickle




if __name__ == '__main__':
    for i in range(32):
        host = "127.0.0.1"
        port = 12345
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))

        s.sendall(b"demand")
        data = s.recv(2048)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("received: ", pickle.loads(data))
    
