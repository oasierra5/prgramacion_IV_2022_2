class Pelicula:
    
    def __init__(self, codigo, titulo, genero):
        self.codigo = codigo
        self.titulo = titulo
        self.genero = genero
        self.alquilada = None
        
    def __str__(self):
        cadena = 'Cï¿½digo: {0}\nTitulo: {1}\nGï¿½nero: {2}'.format(self.codigo, self.titulo,self.genero)
        if self.alquilada == None:
            cadena = cadena + 'Disponible'
        else:
            cadena = cadena + 'Alquilada a {0}\n'.format(self.alquilada)
        return cadena
