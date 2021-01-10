import socket


class BTS():

    def __init__(self, total_range=[173, 862], canal_size=20):
        self.name = "BTS whitespace allocation class"
        self.id_bts = "ad2a2ed2e62ece262ec5e1e1c15e"
        self.total_range = total_range
        self.canal_size = canal_size
        self.canals = [e for e in range(self.total_range[0], self.total_range[1], self.canal_size)]
        self.db = {"unused": [], "used": []}

    def __str__(self):
        return self.name

    def __del__(self):
        del self

    def get_bts(self):
        return self.id_bts
    def get_total(self):
        return self.total_range

    def set_canals(self):
        for i in range(len(self.canals)-2):
            self.db["unused"].append([self.canals[i], self.canals[i+1]-1])

    def consult(self):
        return self.db

    def process(self, request):
        if request == "demand":
            if self.consult()["unused"] != []:
                last =  self.consult()["unused"][-1]
                del self.consult()["unused"][-1]
                self.db["used"].append(last)
                return last
            else:
                return
        else:
            if request in self.consult()["used"]:
                index = self.consult()["used"].index(request)
                revoked = self.consult()["used"][index]
                del self.consult()["used"][index]
                self.consult()["unused"].append(revoked)

if __name__ == '__main__':
    bts = BTS()
    #######################################################""
    host = "127.0.0.1"
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(5)
    print("Server launched ...")

    while True:
        conn, addr = s.accept()
        print('Connected by', addr)
        data = conn.recv(2048)
        if not data:
            break
        print("======= data = ", data.decode())
        #######################################################"

        bts.set_canals()
        print("---", bts.db)
        for i in range(1):
            bts.process("demand")
            print("{}---".format(i), bts.db)

        final = bts.process(bts.db["used"][-1])
        print("----", bts.db)
        data = pickle.dumps(final)

        conn.sendall(data)
