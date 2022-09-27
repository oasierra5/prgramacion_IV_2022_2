class Carta:

    def __init__(self, tanto, palo):
        self.tanto = tanto
        self.palo = palo

    def __str__(self):
        return "[{}-{}]".format(self.tanto, self.palo)

