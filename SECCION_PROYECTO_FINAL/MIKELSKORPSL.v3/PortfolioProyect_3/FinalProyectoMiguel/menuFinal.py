# PROYECTO MIKELSKORP S.L
import json
import logging
import os

# Configuración básica del registro (log)
logging.basicConfig(
    filename='registro_app.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s', 
    datefmt='%H:%M:%S'
)

ARCHIVO = "herramientas.json"

# Funcion Menu con bucle while para que se vaya repitiendo hasta que selecciones la opcion "salir".
# --- MENÚ PRINCIPAL ---

def mi_menu():
    cargar_datos() 
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


# --- CLASES (PROGRAMACIÓN ORIENTADA A OBJETOS) ---

# 1. Clase Base (Elemento principal)
class Herramienta:
    def __init__(self, nombre, descripcion, ubicacion):
        self.nombre = nombre
        self.descripcion = descripcion
        self.ubicacion = ubicacion

    def mostrar(self):
        return f"Nombre: {self.nombre} | Desc: {self.descripcion} | Ubic: {self.ubicacion}"

    def a_diccionario(self):
        return {
            "tipo": "Normal",
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "ubicacion": self.ubicacion
        }

# 2. Subclase (Usa Herencia y añade un dato extra)
class HerramientaElectrica(Herramienta):
    def __init__(self, nombre, descripcion, ubicacion, potencia):
        super().__init__(nombre, descripcion, ubicacion)
        self.potencia = potencia 

    def mostrar(self):
        return f"Nombre: {self.nombre} | Desc: {self.descripcion} | Ubic: {self.ubicacion} | Potencia: {self.potencia}"

    def a_diccionario(self):
        dicc = super().a_diccionario()
        dicc["tipo"] = "Electrica"
        dicc["potencia"] = self.potencia
        return dicc

# --- ESTRUCTURA DE DATOS(herramientas) ---
# La lista ahora guarda instancias (objetos) de las clases
herramientas = [] 

# --- FUNCIONES JSON ---

def guardar_datos():
    lista_guardar = []
    for pieza in herramientas:
        lista_guardar.append(pieza.a_diccionario())

    try:
        with open(ARCHIVO, "w", encoding="utf-8") as f:
            json.dump(lista_guardar, f, indent=4)
    except Exception as e:
        logging.error(f"Error al guardar: {e}")

def cargar_datos():
    global herramientas
    if os.path.exists(ARCHIVO):
        try:
            with open(ARCHIVO, "r", encoding="utf-8") as f:
                datos_json = json.load(f)
                
                for dato in datos_json:
                    if isinstance(dato, dict) and dato.get("tipo") == "Electrica":
                        herramientas.append(HerramientaElectrica(dato["nombre"], dato["descripcion"], dato["ubicacion"], dato["potencia"]))
                    elif isinstance(dato, dict):
                        herramientas.append(Herramienta(dato["nombre"], dato["descripcion"], dato["ubicacion"]))
                    else:
                        # Por si lee el formato viejo de listas
                        herramientas.append(Herramienta(dato[0], dato[1], dato[2]))
        except Exception as e:
            logging.error(f"Error al cargar: {e}")
            herramientas = []
    else:
        # Datos iniciales instanciando los objetos
        herramientas = [
            Herramienta("martillo", "mango de madera", "pasillo 1"),
            HerramientaElectrica("taladro", "percutor", "estanteria B", "500w")
        ]
        guardar_datos()

# ---5 FUNCIONES ---

# ---1 INSERTAR HERRAMIENTAS---
def insertar_elemento():
    print("\n--- AÑADIR HERRAMIENTA ---")
    
    print("¿Qué tipo de herramienta es?")
    print("1. Normal")
    print("2. Eléctrica (Especial)")
    eleccion = input("Elige (1 o 2): ")

    nombre = input("Dime el nombre: ")
    if len(nombre) == 0:
        print("Error: El nombre no puede estar vacío.")
        return 

    descripcion = input("Dime la descripción: ")
    ubicacion = input("Dime la ubicación: ")

    if eleccion == "2":
        potencia = input("Dime la potencia (ej. 1000W): ")
        nueva_pieza = HerramientaElectrica(nombre, descripcion, ubicacion, potencia)
    else:
        nueva_pieza = Herramienta(nombre, descripcion, ubicacion)
    
    herramientas.append(nueva_pieza)
    guardar_datos()
    logging.info(f"Insertado: {nombre}")
    print("¡Guardado correctamente!")

# ---2 BUSCAR HERRAMIENTAS---
def buscar_elemento():
    print("\n--- BUSCAR HERRAMIENTA ---")
    nombre_buscar = input("¿Qué nombre buscas?: ")
    encontrado = False 

    for pieza in herramientas:
        if pieza.nombre == nombre_buscar:
            print("¡ENCONTRADO!")
            print(pieza.mostrar())
            encontrado = True
    
    if not encontrado:
        print("No he encontrado nada con ese nombre.")
        logging.info(f"Búsqueda fallida: {nombre_buscar}")

# ---3 MODIFICAR HERRAMIENTAS---
def modificar_elemento():
    print("\n--- MODIFICAR HERRAMIENTA ---")
    nombre_buscar = input("Dime el nombre exacto de la pieza a cambiar: ")
    
    for pieza in herramientas:
        if pieza.nombre == nombre_buscar:
            print("Pieza encontrada:")
            print(pieza.mostrar())
            
            print("¿Qué quieres cambiar?")
            print("0 = Nombre")
            print("1 = Descripción")
            print("2 = Ubicación")
            if isinstance(pieza, HerramientaElectrica):
                print("3 = Potencia")
            
            opcion = input("Elige un número: ")
            nuevo_dato = input("Escribe el nuevo dato: ")
            
            if opcion == "0": pieza.nombre = nuevo_dato
            elif opcion == "1": pieza.descripcion = nuevo_dato
            elif opcion == "2": pieza.ubicacion = nuevo_dato
            elif opcion == "3" and isinstance(pieza, HerramientaElectrica):
                pieza.potencia = nuevo_dato
            else:
                print("Opción no válida.")
                return
                
            guardar_datos()
            logging.info(f"Modificado: {nombre_buscar}")
            print("¡Cambio realizado!")
            return 
    print("No encontré esa pieza.")

# ---4 ELIMINAR HERRAMIENTAS---
def eliminar_elemento():
    print("\n--- ELIMINAR HERRAMIENTA ---")
    nombre_borrar = input("Dime el nombre de la pieza a borrar: ")
    
    pieza_a_borrar = None
    for pieza in herramientas:
        if pieza.nombre == nombre_borrar:
            pieza_a_borrar = pieza 
            break
    
    if pieza_a_borrar:
        herramientas.remove(pieza_a_borrar)
        guardar_datos()
        logging.info(f"Eliminado: {nombre_borrar}")
        print("La pieza ha sido borrada.")
    else:
        print("No encontré ninguna pieza con ese nombre.")

# ---5 MOSTRAR HERRAMIENTAS---
def mostrar_todos():
    print("\n--- LISTA COMPLETA ---")
    for pieza in herramientas:
        print(pieza.mostrar())

# ---FUNCIONES EXAMEN 2 FEBRERO---
def generar_reporte():
    print("\n--- LISTA DE ELEMENTOS ORDENADA POR LONGITUD DEL NOMBRE ---")
    ordenado_por_longitud = sorted(herramientas, key=lambda x: len(x.nombre))
    for pieza in ordenado_por_longitud:
        print(pieza.mostrar())

# Ejecucion menu
mi_menu()
