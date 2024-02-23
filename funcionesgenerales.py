import json
import csv
import os

#Escribir al Json           
def guardarcambiosjson(datos,archivo):
    with open(archivo,'w') as archivonew:
        escritura = json.dumps(datos , indent = 4)
        archivonew.write(escritura)
        print("Tus datos han sido guardados EXITOSAMENTE")
    

#Leer al Json
def CargarDatosjson(archivo): 
    try:   
        with open(archivo,'r') as file:
            respuesta = json.load(file)
            return respuesta
    except Exception:
        return []
    
#Escribir al CSV    

def guardarcambioscsv(datos, archivo):
    try:
        with open(archivo, "a", newline='') as file:  
            pedidos = csv.writer(file, delimiter=',')
            pedidos.writerow(datos)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        print("archivo no encontrado")
    

#Leer al Csv

def CargarDatoscsv(archivo):
    try:
        with open(archivo, "r", newline='') as file:
            datos = [fila for fila in csv.reader(file, delimiter=',') if fila]  
        return datos
    except FileNotFoundError:
        print("Archivo no encontrado")
        return [] 


        
def limpiarTerminal():
    # Verifica si el sistema operativo es Windows
    if os.name == 'nt':
        _ = os.system('cls')  # Limpia la terminal en Windows
    else:
        _ = os.system('clear')  # Limpia la terminal en sistemas Unix (Linux, macOS)
