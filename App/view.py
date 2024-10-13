import sys
import App.logic as logic
from DataStructures.List import array_list as al
from DataStructures.List import single_linked_list as sl
from DataStructures.Map import map_separate_chaining as ms
from tabulate import tabulate

default_limit=1000
sys.setrecursionlimit(default_limit*10)

def new_logic():
    """
        Se crea una instancia del controlador
    """
    control = logic.new_logic()
    return control

def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8 (Bono)")
    print("0- Salir")

def load_data(control):
    """
    Carga los datos y muestra un resumen de las películas.
    """
    filename = str(input("Ingrese el nombre del archivo CSV: "))
    total, loaded = logic.load_data(control, filename)
    
    print('Total de peliculas cargadas: ' + str(total))
    print('Primeras 5 peliculas cargadas:')
    headers = ["Fecha de Publicación", "Título Original", "Idioma Original", 
               "Duración (min)", "Presupuesto", "Ingresos", "Ganancias"]
    first_five_movies = [
        [
            movie['release_date'],
            movie['title'],
            movie['original_language'],
            movie['runtime'],
            movie['budget'],
            movie['revenue'],
            movie['revenue'] - movie['budget']
        ]
        for movie in loaded[:5]
    ]
    print(tabulate(first_five_movies, headers=headers, tablefmt='grid'))

    print("\nÚltimas 5 películas cargadas:")
    last_five_movies = [
        [
            movie['release_date'],
            movie['title'],
            movie['original_language'],
            movie['runtime'],
            movie['budget'],
            movie['revenue'],
            movie['revenue'] - movie['budget']
        ]
        for movie in loaded[-5:]
    ]
    print(tabulate(last_five_movies, headers=headers, tablefmt='grid'))
    

def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    data = logic.get_data(control, id)
    
    if data:
        # Si el dato es una película, imprimimos sus detalles
        print("Información del dato:")
        print("  ID: " + str(data['id']))
        print("  Título: " + str(data['title']))
        print("  Idioma original: " + str(data['original_language']))
        print("  Fecha de lanzamiento: " + str(data['release_date']))
        print("  Presupuesto: " + str(data['budget']))
        print("  Recaudación: " + str(data['revenue']))
        print("  Promedio de votos: " + str(data['vote_average']))
        print("  Número de votos: " + str(data['vote_count']))
    else:
        print("No se encontró ningún dato con ID: " + str(id))

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    pass


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    pass


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    pass


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    pass


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    pass


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    pass


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    pass


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass


# Se crea la lógica asociado a la vista
control = new_logic()

# main del ejercicio
def main():
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1:
            print("Cargando información de los archivos ....\n")
            data = load_data(control)
        elif int(inputs) == 2:
            print_req_1(control)

        elif int(inputs) == 3:
            print_req_2(control)

        elif int(inputs) == 4:
            print_req_3(control)

        elif int(inputs) == 5:
            print_req_4(control)

        elif int(inputs) == 6:
            print_req_5(control)

        elif int(inputs) == 7:
            print_req_6(control)

        elif int(inputs) == 8:
            print_req_7(control)

        elif int(inputs) == 9:
            print_req_8(control)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
