class Cuenta:

    def __init__(self, propietario, saldo, moneda):
        self._propietario = propietario
        self._saldo = saldo
        self._moneda = moneda

    def get_Propietario(self):
        return self._propietario

    #Getter para obtener los valores
    def get_Saldo(self):
        return self._saldo

    def get_Moneda(self):
        return self._moneda
    
    #Setter Modificar os valores y validar
    def set_Moneda(self, moneda):
        self._moneda = moneda

cuenta = Cuenta("Oscar Sierra", 50000, "Dollar")
print(cuenta.get_Saldo())
print(cuenta.get_Moneda())
cuenta.set_Moneda("Pesos")
print(cuenta.get_Moneda())
