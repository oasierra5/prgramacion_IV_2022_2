'''
Códigos de los carácteres de las barajas
pica = \u2660, corazon = \u2665 diamante = \u2666, trébol = \2663
'''
from carta import Carta

class Baraja:

    def __init__(self):
        palos = ["\u2660", "\u2665", "\u2666", "\2663"]
        tantos = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "k"]

        self.mazo = []
        for t in tantos:
            for p in palos:
                carta = Carta(t, p)
                self.mazo.append(carta)

    def mostrar_baraja(self):
        print()
        for num, carta in enumerate(self.mazo):
            if (num-3) % 4 != 0:
                print(carta, end=" ")
            else:
                print(carta)
        print()
