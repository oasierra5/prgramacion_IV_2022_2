class Producto:

    def __init__(self, costo):
        self._costo = costo
        self._precio_venta = self._calcular_precio_venta()

    def get_Costo(self):
        return self._costo

    def get_Precio_venta(self):
        return self._precio_venta
    
    def set_Costo(self, valor):
        if (valor > 0):
            self._costo = valor
            self._precio_venta = self._calcular_precio_venta()
        else:
            print('Valor Invalido')
            self._costo = 0

    def _calcular_precio_venta(self):
        return self._costo * 1.30

    def __repr__(self):
        return f'Costo=${self._costo}, Precio venta=${self._precio_venta}'

teclado = Producto(15000)
print(teclado)
print("El precio del producto es de:",teclado.get_Costo())
teclado.set_Costo(-2127)
print(teclado)
