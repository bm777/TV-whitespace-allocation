import socket, pickle




if __name__ == '__main__':

    host = "127.0.0.1"
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    s.sendall(pickle.dumps(["demand"]))
    data = s.recv(2048)
    tmp = pickle.loads(data)
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("received: ", tmp)
    s.close()

    # sent received for revoking
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    s.sendall(pickle.dumps(tmp))
    revoked = s.recv(2048)
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("received: ", pickle.loads(revoked))
