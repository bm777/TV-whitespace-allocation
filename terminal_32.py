import socket, pickle




if __name__ == '__main__':
    host = "127.0.0.1"
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    for i in range(32):
        s.sendall(b"demand")
    # Receive no more than 1024 bytes
    data = s.recv(2048)

    s.close()

    print("The time got from the bts server is ", pickle.loads(data))

    # for elt in pickle.loads(data):
    #     print("----",elt)