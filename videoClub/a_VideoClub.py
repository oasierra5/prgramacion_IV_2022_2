from a_Pelicula import Pelicula
from a_Socio import Socio

class VideoClub:
    
    def __init__(self):
        self.socios = []
        self.pelicula = []
        
    def nuevo_socio(self):
        dni = input('DNI: ')
        nombre = input('Nombre: ')
        telefono = input('TelÃ©fono: ')
        domicilio = input('Domicilio: ')
        return Socio(dni, nombre, telefono, domicilio)
    
    def contiene_socio(self, dni):
        for socio in self.socios:
            if (socio.dni == dni):
                return True
        return False
    
    def agregar_socio(self, socio):
        
        self.socios.append(socio)
        
