import csv
import funcionesgenerales
import juego
import json
import time

while True:
    print("*****************************")
    print("   Bienvenidos al programa   ")
    print("*****************************")
    print("1.)Gestion de Juegos")
    print("2.)Consultar y Valoraciones")
    print("0.)Salir")
    try:
        opc = int(input("\nIngresa una opcion: "))
    except ValueError:
        print("\n***ingresa una opcion correcta***")
        time.sleep(2)
        continue
    if opc>0 and opc<3:
        if opc == 1:
            while True:
                print("*****************************")
                print("   Que deseas realizar hoy   ")
                print("*****************************")
                print("1.)Regsitrar Juego")
                print("2.)Modificar Juego")
                print("3.)Eliminar Juego")
                print("0.)Salir")
                try:
                    opc = int(input("\nIngresa una opcion: "))
                except ValueError:
                    print("\n***ingresa una opcion correcta***")
                    time.sleep(2)
                    continue
                if opc == 1:
                    funcionesgenerales.limpiarTerminal()
                    juego.registroJuego()
                elif opc == 2:
                    funcionesgenerales.limpiarTerminal()
                    juego.modificarJuego()
                elif opc == 3:
                    funcionesgenerales.limpiarTerminal()
                    juego.EliminarJuego()
                elif opc == 0:  
                    break 
        elif opc == 2:
            while True:
                print("*****************************")
                print("   Que deseas realizar hoy   ")
                print("*****************************")
                print("1.)Consultar juego")
                print("2.)Valorar Juego")
                print("3.)Top 3 Juegos")
                print("0.)Salir")
                try:
                    opc = int(input("\nIngresa una opcion: "))
                except ValueError:
                    print("\n***ingresa una opcion correcta***")
                    time.sleep(2)
                    continue
                if opc == 1:
                    funcionesgenerales.limpiarTerminal()
                    juego.ConsultarJuego()
                elif opc == 2:
                    funcionesgenerales.limpiarTerminal()
                    juego.ValorarJuego()
                elif opc == 3:
                    funcionesgenerales.limpiarTerminal()
                    juego.TopJuegos()
                elif opc == 0:  
                    break 
        elif opc == 0:  
            break 