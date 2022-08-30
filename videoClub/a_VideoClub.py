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

    def eliminar_socio(self, dni):
        for i in range(len(self.socios)):
            if self.socios[i].dni == dni:
                del self.socios[i]
                break
    
    def nueva_pelicula(self):
        codigo = input('Codigo: ')
        titulo = input('Titulo: ')
        genero = input('Genero: ')
        return Pelicula(codigo, titulo, genero)

    def contiene_pelicula(self, codigo):
        for peli in self.pelicula:
            if peli.codigo == codigo:
                return True
        return False

    def agregar_pelicula(self, pelicula):
        self.pelicula.append(pelicula)

    def listar_peliculas(self):
        for pel in self.pelicula:
            print("Código: ",pel.codigo)
            print("Titulo: ",pel.titulo)
            print("Estado: ",pel.alquilada)
            print("##################################")

    def alquilar_pelicula(self, codigo, dni):
        for pel in self.pelicula:
            if pel.codigo == codigo:
                if pel.alquilada == None:
                    pel.alquilada = dni
                    return True
                else:
                    return False
