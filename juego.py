import json
import funcionesgenerales
import time

#Funcion para ingresar campers

def registroJuego():
    ListaJuegos=funcionesgenerales.CargarDatosjson("juegos.json")
    print("--------------------------------")
    print("-------Registro de Camper-------")
    print("--------------------------------") 
    while True:
        try:
            nombreJuego=input("Escribe el nombre del Juego\n").lower()
            tiempo=int(input("Escribe el tiempo por partida en minutos\n"))
            cantidadJugadores=int(input("Por favor escribe la cantidad de jugadores\n"))
            Existencia=int(input("Escribe Cuantos juegos de este tipo hay disponbiles para el uso\n"))
            ListaJuegos.append({'nombreJuego':nombreJuego, 'Tiempo': tiempo, 'Cantidad de Jugadores':cantidadJugadores, 'Existencia':Existencia})           
            funcionesgenerales.guardarcambiosjson(ListaJuegos,"juegos.json")
            print("Juego creado con exito")
            break
        except ValueError:
            print("El valor seleccionado no es numerico\nintentalo de nuevo")
            time.sleep(2)
            continue
    

def modificarJuego():
    ListaJuegos=funcionesgenerales.CargarDatosjson("juegos.json")
    while True:
        print("----------------------------------------")
        print("-------Lista de Juegos Disponibles-------")
        print("----------------------------------------") 
        for index,juego in enumerate(ListaJuegos):
            nombre=juego.get('nombreJuego','No hay nombre')
            print(f"{index+1}-{nombre}")
        try:
            opc = int(input("\nIngresa el numero indice del juego que quieres modificar:  "))
            
        except ValueError:
            print("\n***ingresa una opcion correcta***")
            time.sleep(2)
            continue
    
        #inicia a modificar el juego
        
        print("*******************************")
        print("¿Que deseas modificar del juego")
        print("*******************************")
        print("1.)Tiempo por partida de juego")
        print("2.)Cantidad de jugadores")
        print("3.)Existencias del juego")
        print("0.)Salir")
        try:
            opc2 = int(input("\nIngresa una opcion: "))
        except ValueError:
            print("\n***ingresa una opcion correcta***")
            time.sleep(2)
            continue
        if opc == 1:
            funcionesgenerales.limpiarTerminal()
            nuevotiempo=int(input("Por favor escribe el nuevo tiempo por partida:  "))
            ListaJuegos[opc-1]['Tiempo']=nuevotiempo
            funcionesgenerales.guardarcambiosjson(ListaJuegos,"juegos.json")
            break
        elif opc == 2:
            funcionesgenerales.limpiarTerminal()
            nuevacantidadjugadores=int(input("Por favor escribe la nueva cantidad de jugadores para este juego:  "))
            ListaJuegos[opc-1]['Cantidad de Jugadores']=nuevacantidadjugadores
            funcionesgenerales.guardarcambiosjson(ListaJuegos,"juegos.json")
            break
        elif opc == 3:
            funcionesgenerales.limpiarTerminal()
            nuevasExistencias=int(input("Por favor escribe la nueva cantidad de juegos:  "))
            ListaJuegos[opc-1]['Existencia']=nuevasExistencias
            funcionesgenerales.guardarcambiosjson(ListaJuegos,"juegos.json")
            break
        elif opc == 0:   
            print("Saliendo...")
            time.sleep(2)
            break
        
        else:
            print("\n***ingresa una opcion correcta***")
            time.sleep(2)
            continue
        
def EliminarJuego():
    ListaJuegos=funcionesgenerales.CargarDatosjson("juegos.json")
    while True:
        print("-------------------------------------------")
        print("-------Lista de Juegos para Eliminar-------")
        print("-------------------------------------------") 
        for index,juego in enumerate(ListaJuegos):
            nombre=juego.get('nombreJuego','No hay nombre')
            print(f"{index+1}-{nombre}")
        try:
            opc = int(input("\nIngresa el numero indice del juego que quieres eliminar:  "))
            
        except ValueError:
            print("\n***ingresa una opcion correcta***")
            time.sleep(2)
            continue
    
        ListaJuegos.pop(opc-1)
        print("Juego Eliminado")
        funcionesgenerales.guardarcambiosjson(ListaJuegos,"juegos.json")
        break
        
def ConsultarJuego():
    ListaJuegos=funcionesgenerales.CargarDatosjson("juegos.json")
    while True:
        print("*****************************")
        print("¿Cuanto tiempo quieres Jugar?")
        print("*****************************")
        print("1.)menos de 5 minutos")
        print("2.)entre 5 y 15 minutos")
        print("3.)entre 15 y 30 minutos")
        print("4.)entre 30 y 60 minutos")
        print("0.)Salir")
        try:
            opc = int(input("\nIngresa una opcion de tiempo: "))
        except ValueError:
            print("\n***ingresa una opcion correcta***")
            time.sleep(2)
            
        
        if opc == 1:
            for x in ListaJuegos:
                if x.get('Tiempo') <= 5:
                    print(f"{x.get('nombreJuego')}")
                         
        elif opc == 2:
            for x in ListaJuegos:
                if x.get('Tiempo') > 5 and x.get('Tiempo') <= 15:
                    print(f"{x.get('nombreJuego')}")
        elif opc == 3:
            for x in ListaJuegos:
                if x.get('Tiempo') > 15 and x.get('Tiempo') <= 30:
                    print(f"{x.get('nombreJuego')}")
        elif opc == 4:
            for x in ListaJuegos:
                if x.get('Tiempo') > 30 and x.get('Tiempo') <= 60:
                    print(f"{x.get('nombreJuego')}")
        elif opc == 0:   
            print("Saliendo....")
            break
        else:
            print("\n***ingresa una opcion correcta***")
            time.sleep(2)
            continue
        

def ValorarJuego():
    ListaJuegos=funcionesgenerales.CargarDatosjson("juegos.json")
    while True:
        print("**********************************")
        print("   Lista de Juegos para Valorar   ")
        print("**********************************") 
        for index,juego in enumerate(ListaJuegos):
            nombre=juego.get('nombreJuego','No hay nombre')
            print(f"{index+1}-{nombre}")
        try:
            opc = int(input("\nIngresa el numero indice del juego que quieres valorar:  "))
            NombreJuegoValorado=ListaJuegos[opc-1].get('nombreJuego','No hay nombre')
            valoracion=int(input(f"\nCuanto puntaje le darías al juego {NombreJuegoValorado} de 1 a 100:  "))
            if valoracion>0 and valoracion<100:
                ListaValoracion=[NombreJuegoValorado,valoracion]
                funcionesgenerales.guardarcambioscsv(ListaValoracion,"juegos.csv")
                break
            else:
                print("El valor ingresado no está dentro del rango\nintentalo nuevamente")
        except ValueError:
            print("\n***ingresa una opcion numerica***")
            time.sleep(2)
            continue
        
        

def TopJuegos():
    ListaValoracion = funcionesgenerales.CargarDatoscsv("juegos.csv")
    
    # Crear un diccionario para almacenar la cantidad de valoraciones de cada juego
    cantidad_valoraciones = {}

    # Contar la cantidad de valoraciones para cada juego
    for juego,a in ListaValoracion:
        if juego in cantidad_valoraciones:
            cantidad_valoraciones[juego] += 1
        else:
            cantidad_valoraciones[juego] = 1

    # Ordenar los juegos por la cantidad de valoraciones y seleccionar los tres con más valoraciones
    top_tres = sorted(cantidad_valoraciones.items(), key=lambda x: x[1], reverse=True)[:3]

    # Imprimir los tres juegos con más valoraciones
    print("Los tres juegos con más valoraciones son:")
    for juego, cantidad in top_tres:
        print(f"{juego}: {cantidad}")
  
        
