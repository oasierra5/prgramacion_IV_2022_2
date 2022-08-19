class Lapiz:
    """Creamos la clase lapiz de prueba"""
    def __init__(self, color, contiene_borrador, usa_grafito):
        self.color = color
        self.contiene_borrador = contiene_borrador
        self.usa_grafito = usa_grafito

    def dibujar(self):
        print('El lapiz está dibujando')

    def borrar(self):
        if self.es_valido_para_borrar():
            print("El lapiz está borrando")
        else:
            print("No es posible borrar")

    def es_valido_para_borrar(self):
        return self.contiene_borrador

lapiz_generico = Lapiz("Verde", True, True)
print("El lapiz es de color",lapiz_generico.color)
print("El lapiz contiene borrador",lapiz_generico.contiene_borrador)
print("El lapiz usa grafito",lapiz_generico.usa_grafito)
lapiz_generico.dibujar()
lapiz_generico.borrar()
