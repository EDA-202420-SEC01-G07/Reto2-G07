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
    filename = input("Ingrese el nombre del archivo CSV: ")
    total, primeras, ultimas = logic.load_data(control, filename)
    print("Total de películas procesadas y cargadas:", total)
    n = 5
    print("\nPrimeras 5 películas cargadas:")
    mostrar_peliculas(primeras)
    print("\nÚltimas 5 películas cargadas:")
    mostrar_peliculas(ultimas)

def mostrar_peliculas(peliculas):
    peliculas_data = []
    for movie in peliculas:
        peliculas_data.append([
            movie['id'],
            movie['title'],
            movie['original_language'],
            movie['release_date'],
            movie['vote_average'],
            movie['vote_count'],
            movie['budget'],
            movie['revenue']
        ])
    headers = ['ID', 'Título', 'Idioma', 'Fecha de Lanzamiento', 'Puntuación', 'Votos', 'Presupuesto', 'Ingresos']
    print(tabulate(peliculas_data, headers=headers, tablefmt='grid'))
    
def print_req_1(control):
    """
    Solicita al usuario el título y el idioma, busca la película y muestra los resultados.
    """
    title = input("Ingrese el título de la película: ")
    language = input("Ingrese el idioma original de la película (ejemplo: 'en', 'fr'): ")

    movie = logic.find_movie_by_title_and_language(control, title, language)

    if movie:
        revenue = movie['revenue']
        budget = movie['budget']
        try:
            if revenue != "Undefined" and budget != "Undefined":
                profit = int(revenue) - int(budget)
            else:
                profit = "Indefinido"
        except ValueError:
            profit = "Indefinido"
            
        headers = ["Título Original", "Idioma Original", "Fecha de Publicación",
                   "Duración (min)", "Presupuesto", "Ingresos Netos",
                   "Ganancia Final", "Puntaje de Calificación"]
        movie_data = [[
            movie['title'],
            movie['original_language'],
            movie['release_date'],
            movie['runtime'],
            movie['budget'],
            movie['revenue'],
            profit,
            movie['vote_average']
        ]]
        print("\nPelícula encontrada:")
        print(tabulate(movie_data, headers=headers, tablefmt='grid'))
    else:
        print("No se encontró ninguna película que cumpla con los criterios proporcionados.")


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
