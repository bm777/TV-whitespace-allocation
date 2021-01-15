import socket, pickle, time
from cryptography.fernet import Fernet

class BTS():

    def __init__(self, total_range=[173, 862], canal_size=20):
        self.name = "BTS whitespace allocation class"
        self.id_bts = Fernet.generate_key()
        self.total_range = total_range
        self.canal_size = canal_size
        self.canals = [e for e in range(self.total_range[0], self.total_range[1], self.canal_size)]
        self.db = {"unused": [], "used": []}


    def __str__(self):
        return self.name

    def present(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("\t\t\t----GENERAL INFORMATION----")
        print("Class :", self.__str__())
        print("UNUSED range : {} - USED range : {}".format(self.size()[0], self.size()[1]))
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    def size(self):
        return [len(self.db["unused"]), len(self.db["used"])]

    def set_canals(self):
        for i in range(len(self.canals)-2):
            self.db["unused"].append([self.canals[i], self.canals[i+1]-1])

    def consult(self):
        return self.db

    def process(self, request):
        if request == "demand":
            if self.db["unused"] != []:
                last =  self.db["unused"][0]
                del self.db["unused"][0]
                self.db["used"].append(last)

                return last
            else:
                return []
        else:
            if request in self.db["used"]:
                index = self.db["used"].index(request)
                revoked = self.db["used"][index]
                del self.db["used"][index]
                self.db["unused"].append(revoked)
                return []

if __name__ == '__main__':
    start = time.time()
    bts = BTS()
    #######################################################""
    host = "127.0.0.1"
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(5)

    bts.set_canals()
    bts.present()
    print("Server launched ...")
    while True:
        conn, addr = s.accept()
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
        print('Connected by', addr)
        data = conn.recv(2048)
        if not data:
            break
        if type(data.decode()) == type("str")
        f = bts.process(pickle.load(data))
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        data = pickle.dumps(f)
        time.sleep(1.0)

        bts.present()
        conn.sendall(data)
        # conn.close()
