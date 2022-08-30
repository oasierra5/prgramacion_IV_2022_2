from a_Pelicula import Pelicula
from a_Socio import Socio
from a_VideoClub import VideoClub

if __name__=='__main__':
    
    video_club = VideoClub()
    
    opcion = 1
    
    while(0 < opcion and opcion < 10):
        print('***VIDEO CLUB***')
        print('1. Nuevo Socio')
        print('2. Eliminar Socio')
        print('3. Nueva Película')
        print('4. Eliminar Película')
        print('5. Listar Socios')
        print('6. Listar Películas')
        print('7. Alquilar Película')
        print('8. Devolver Película')
        print('9. Salir del Programa')
        
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

        elif opcion == 2:
            print('Eliminar Socio')
            dni = input("Digite el DNI del Socio: ")
            if video_club.contiene_socio(dni):
                video_club.eliminar_socio(dni)
                print("El socio con DNI",dni,"ha sido eliminado")
            else:
                print("El socio con DNI",dni,"no existe")
                print("No se puede dar de baja")

        elif opcion == 3:
            print('Nueva Pelicula')
            pelicula = video_club.nueva_pelicula()
            if video_club.contiene_pelicula(pelicula.codigo):
                print('La pelicula ya esta registrada')
            else:
                video_club.agregar_pelicula(pelicula)

        elif opcion == 6:
            print("Listar las Películas del video club")
            video_club.listar_peliculas()

        elif  opcion == 7:
            print('Alquiler Película')
            codigo = input("Digite el código de la película: ")
            dni = input("Digite el DNI del Socio: ")
            esta_pelicula = video_club.contiene_pelicula(codigo)
            esta_socio = video_club.contiene_socio(dni)
            if (esta_pelicula and esta_socio):
                if (video_club.alquilar_pelicula(codigo, dni)):
                    print("La película ha sido alquilada")
                else:
                    print("La película no esta disponible")
            else:
                if (not esta_pelicula):
                    print("La película no esta disponible")
                if (not esta_socio):
                    print("El socio con DNI",dni,"no esta asociado")

        elif opcion == 9:
            print("Exitos....")
            break
