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

if __name__ == '__main__':
    bts = BTS()
    bts.set_canals()
    print(bts.db)
