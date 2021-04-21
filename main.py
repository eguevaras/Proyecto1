
# base_de_datos.json
import json

# lista_estudiantes = []

try:
    with open("base_de_datos.json", "r") as archivo_db:
        print("Leyendo base de datos...")
        lista_estudiantes = json.load(archivo_db)
        print("Base de datos cargada exitosamente")
except:
    print("Creando nueva base de datos...")
    lista_estudiantes = []

def calcular_promedio(lista_notas_estudiante):
    total_suma = 0
    # sumar todas las notas
    for nota in lista_notas_estudiante:
        total_suma = total_suma + nota
    # obtener cantidad de notas
    cantidad_notas = len(lista_notas_estudiante)
    # calcular promedio
    promedio = total_suma / cantidad_notas
    # retornar el promedio
    return promedio

def ingresar_nuevo_estudiante():

    # pedir datos de estudiante
    nombre = input("Ingrese nombre: ")
    carnet = input("Ingrese carnet: ")

    # agregar notas
    lista_notas = []
    opcion_notas = input("Desea ingresar una nota? (y / n): ")
    while opcion_notas == 'y' or opcion_notas == 'Y':
        nueva_nota = input("Ingrese la nota: ")

        # convertir en entero
        nueva_nota = int(nueva_nota)
        lista_notas.append(nueva_nota)
        opcion_notas = input("Desea ingresar otra nota? (y / n): ")
    
    # llamar al calculo de promedio
    promedio_estudiante = calcular_promedio(lista_notas)

    # crear al nuevo estudiante
    estudiante = {
        'NOMBRE:': nombre,
        'CARNET:': carnet,
        'NOTAS:': lista_notas,
        'PROMEDIO': promedio_estudiante,
        'CURSOS:': len(lista_notas)
 
    }
    # agregar el nuevo estudiante a la lista
    lista_estudiantes.append(estudiante)
    return


def mostrar_cantidad_estudiantes():
    cantidad = len(lista_estudiantes)
    print(f'Hay {cantidad} estudiantes')
    return

def mostrar_lista_estudiantes():
    print(lista_estudiantes)
    return

def mostrar_menu():
    mensaje_menu = """
'----------------------------------------------'
    Ingrese la opcion deseada:\n
    1. Ingresar un nuevo usuario\n
    2. Buscar un usuario\n
    3. Mostrar lista de estudiantes\n
    0. Salir\n
'----------------------------------------------'    
    > 
    """

    opcion = input(mensaje_menu)
    opcion = int(opcion)

    if opcion == 1:
        # ingresar un nuevo estudiante
        ingresar_nuevo_estudiante()
    
    if opcion == 2:
        # mostrar cantidad de estudiante
        mostrar_cantidad_estudiantes()

    if opcion == 3:
        # mostrar lista estudiantes
        mostrar_lista_estudiantes() 
           
    if opcion == 0:
        #*************************************************************************************************
        # mostrar opciones guardar y salir // salir sin guardar
        seleccionsalir = """1. Salir y Guardar\n
2. Salir sin guardar\n"""

        opcionsalir = input (seleccionsalir)
        opcionsalir = int(opcionsalir)
        
        if opcionsalir == 1:
            with open("base_de_datos.json", "w") as archivo_db:
                print("Guardando base de datos...")
                json.dump(lista_estudiantes, archivo_db)
            return
        if opcionsalir == 2:
            return    
        #******************************************************************************************************
    mostrar_menu()
    return

mostrar_menu()