# PROYECTO MIKELSKORP S.L
import json
import logging
import os

# Configuración básica del registro (log)
logging.basicConfig(
    filename='registro_app.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s', # Formato simple: Hora - Mensaje
    datefmt='%H:%M:%S'
)

ARCHIVO = "herramientas.json"

# Funcion Menu con bucle while para que se vaya repitiendo hasta que selecciones la opcion "salir".
# --- MENÚ PRINCIPAL ---

def mi_menu():
    cargar_datos() # Antes de empezar, leemos el fichero
    logging.info("--- Inicio del programa ---")

    while True:
        print("\n=== MIKELSKORP S.L MENU ===")
        print("1. Añadir a Catalogo de Herramientas")
        print("2. Buscar Piezas")
        print("3. Modificar Pieza")
        print("4. Eliminar Pieza")
        print("5. Mostrar todos")
        print("6. Salir")

        opcion = input("Eliga una opción: ")

        if opcion == "1":
            insertar_elemento()
        
        elif opcion == "2":
            buscar_elemento()
        
        elif opcion == "3":
            modificar_elemento()
        
        elif opcion == "4":
            eliminar_elemento()
        
        elif opcion == "5":
            mostrar_todos()
        
        elif opcion == "6":
            print("Saliendo del programa... ")
            logging.info("--- Fin del programa ---")
            break 

        else:
            print("Opción no válida")


# --- ESTRUCTURA DE DATOS(herramientas) ---
# Es una lista que contiene otras listas dentro.
# Cada lista pequeña es: [NOMBRE, DESCRIPCION, UBICACION]
# Posición 0 = Nombre
# Posición 1 = Descripción
# Posición 2 = Ubicación

herramientas = [] 

# --- FUNCIONES JSON ---

def guardar_datos():
    # Abre el fichero en modo escritura (w) y vuelca la lista
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(herramientas, f, indent=4)

def cargar_datos():
    global herramientas
    # Si el archivo existe, lo leemos
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            herramientas = json.load(f)
    else:
        # Si no existe, usamos la lista por defecto
        herramientas = [
            ["martillo", "mango de madera", "pasillo 1"],
            ["llave inglesa", "tamaño grande", "caja 4"],
            ["destornillador", "punta de estrella", "cajon 2"],
            ["taladro", "percutor 500w", "estanteria B"],
            ["gato hidraulico", "soporta 2 toneladas", "zona suelo"],
            ["sierra de calar", "electrica", "armario 3"],
            ["alicates", "corte universal", "panel herramientas"],
            ["cinta metrica", "5 metros", "mesa trabajo"],
            ["juego de vasos", "12 piezas metalicas", "maletin rojo"]
        ]
        guardar_datos() # Creamos el archivo


# ---5 FUNCIONES ---

# ---1 INSERTAR HERRAMIENTAS---
def insertar_elemento():
    print("\n--- AÑADIR HERRAMIENTA ---")
    nombre = input("Dime el nombre: ")
    
    # Si el nombre esta vacio se sale
    if len(nombre) == 0:
        print("Error: El nombre no puede estar vacío.")
        return 

    descripcion = input("Dime la descripción: ")
    ubicacion = input("Dime la ubicación: ")

    # hacemos una minilista con los datos
    nueva_pieza = [nombre, descripcion, ubicacion]
    
    # Y lo guardamos en la lista grande
    herramientas.append(nueva_pieza)
    
    guardar_datos() # Guardamos en JSON
    logging.info(f"Insertado: {nombre}") # Guardamos en Log
    
    print("¡Guardado correctamente!")

# ---2 BUSCAR HERRAMIENTAS---
def buscar_elemento():
    print("\n--- BUSCAR HERRAMIENTA ---")
    nombre_buscar = input("¿Qué nombre buscas?: ")
    
    encontrado = False # Esto es para saber que lo vemos

    for pieza in herramientas:
        # pieza[0] es el NOMBRE
        if pieza[0] == nombre_buscar:
            print("¡ENCONTRADO!")
            print("Nombre:", pieza[0])
            print("Descripción:", pieza[1])
            print("Ubicación:", pieza[2])
            encontrado = True
    
    if encontrado == False:
        print("No he encontrado nada con ese nombre.")
        logging.info(f"Búsqueda fallida: {nombre_buscar}")

# ---3 MODIFICAR HERRAMIENTAS---
def modificar_elemento():
    print("\n--- MODIFICAR HERRAMIENTA ---")
    nombre_buscar = input("Dime el nombre exacto de la pieza a cambiar: ")
    
    for pieza in herramientas:
        if pieza[0] == nombre_buscar:
            print("Pieza encontrada:", pieza)
            print("¿Qué quieres cambiar?")
            print("0 = Nombre")
            print("1 = Descripción")
            print("2 = Ubicación")
            
            try:
                posicion = int(input("Elige un número (0, 1 o 2): "))
                nuevo_dato = input("Escribe el nuevo dato: ")
                
                # Cambiamos el dato en la posición que dijo el usuario
                pieza[posicion] = nuevo_dato
                
                guardar_datos() # Actualizamos el fichero
                logging.info(f"Modificado: {nombre_buscar}")
                
                print("¡Cambio realizado!")
                
            except ValueError:
                # Si no escribes un numero salta el error
                print("ERROR: Debes escribir un NÚMERO, no letras.")
            except IndexError:
                # Si no pones (0, 1 o 2) salta el error
                print("ERROR: Ese número no existe. Solo 0, 1 o 2.")
            
            return 
    print("No encontré esa pieza.")

# ---4 ELIMINAR HERRAMIENTAS---
def eliminar_elemento():
    print("\n--- ELIMINAR HERRAMIENTA ---")
    nombre_borrar = input("Dime el nombre de la pieza a borrar: ")
    
    pieza_a_borrar = [] # Variable vacía para guardar lo que encontremos

    # Buscamos la pieza
    for pieza in herramientas:
        if pieza[0] == nombre_borrar:
            pieza_a_borrar = pieza # La guardamos aquí para borrarla luego
    
    # Si la lista NO está vacía, significa que encontramos algo
    if len(pieza_a_borrar) > 0:
        herramientas.remove(pieza_a_borrar)
        
        guardar_datos() # Actualizamos fichero
        logging.info(f"Eliminado: {nombre_borrar}")
        
        print("La pieza ha sido borrada.")
    else:
        print("No encontré ninguna pieza con ese nombre.")

# ---5 MOSTRAR HERRAMIENTAS---
def mostrar_todos():
    print("\n--- LISTA COMPLETA ---")
    # Recorremos la lista y mostramos los datos 
    for pieza in herramientas:
        print("Nombre:", pieza[0], "| Desc:", pieza[1], "| Ubic:", pieza[2])


# Ejecucion menu
mi_menu()
