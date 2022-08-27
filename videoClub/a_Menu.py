from a_Pelicula import Pelicula
from a_Socio import Socio
from a_VideoClub import VideoClub

if __name__=='__main__':
    
    video_club = VideoClub()
    
    opcion = 1
    
    while(0 < opcion and opcion < 7):
        print('***VIDEO CLUB***')
        print('1. Nuevo Socio')
        
        opcion = int(input('Elija una opciÃ³n'))
        
        while(opcion < 1 or opcion > 7):
            opcion = int(input('Elija la opciÃ³n correcta entre 1 y 7'))
            
        if opcion == 1:
            print('Nuevo Socio')
            socio = video_club.nuevo_socio()
            if video_club.contiene_socio(socio.dni):
                print("El socio con DNI {0} ya exisite en el vidoe club".format(socio.dni))
            else:
                video_club.agregar_socio(socio)
        
