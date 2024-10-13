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
        gain = movie.get('gain', "Undefined")
        if isinstance(gain, int):
            gain = f"{gain:,}"  # Formatear con comas
        elif gain == 0:
            gain = "Undefined"

        # Formatear 'budget' y 'revenue' si son enteros
        budget = movie.get('budget', "Undefined")
        if isinstance(budget, int):
            budget = f"{budget:,}"
        elif budget == 0:
            budget = "Undefined"

        revenue = movie.get('revenue', "Undefined")
        if isinstance(revenue, int):
            revenue = f"{revenue:,}"
        elif revenue == 0:
            revenue = "Undefined"

        peliculas_data.append([
            movie['id'],
            movie['title'],
            movie['original_language'],
            movie['release_date'],
            movie['vote_average'],
            movie['vote_count'],
            budget,
            revenue,
            gain  # Agregar la ganancia
        ])
    headers = ['ID', 'Título', 'Idioma', 'Fecha de Lanzamiento', 'Puntuación', 'Votos', 'Presupuesto', 'Ingresos', 'Ganancia']
    print(tabulate(peliculas_data, headers=headers, tablefmt='grid'))

def print_all_movies(control):
    """
    Función de depuración para listar todas las películas en el catálogo.
    """
    print("\n--- Lista de Todas las Películas en el Catálogo ---")
    peliculas = []
    for key in control.key_set():
        movie = control.get(key)
        if movie:
            peliculas.append([movie['title'], movie['original_language']])
    headers = ['Título', 'Idioma Original']
    print(tabulate(peliculas, headers=headers, tablefmt='grid'))
    print()

def print_req_1(control):
    """
    Solicita al usuario el título y el idioma, busca la película y muestra los resultados.
    """
    print("\n--- Requerimiento No. 1 ---")
    title = input("Ingrese el título de la película: ").strip()
    language = input("Ingrese el idioma original de publicación (código de dos letras, ej.: 'en', 'fr'): ").strip().lower()

    # Validar entradas
    if not title:
        print("El título de la película no puede estar vacío.\n")
        return
    if not language or len(language) != 2:
        print("El idioma debe ser un código de dos letras (ej.: 'en', 'fr').\n")
        return

    # Buscar la película
    matching_movies = logic.req_1(control, title, language)

    if not matching_movies:
        print("No se encontró ninguna película que coincida con los criterios proporcionados.\n")
        return

    # Preparar datos para la visualización
    peliculas_data = []
    for movie in matching_movies:
        runtime = movie.get('runtime', "Undefined")
        if isinstance(runtime, int):
            runtime = f"{runtime} minutos"
        elif runtime == 0:
            runtime = "Undefined"

        release_date = movie.get('release_date', "Undefined")
        title_original = movie.get('title', "Undefined")

        budget = movie.get('budget', "Undefined")
        if isinstance(budget, int):
            budget = f"{budget:,}"
        elif budget == 0:
            budget = "Undefined"

        revenue = movie.get('revenue', "Undefined")
        if isinstance(revenue, int):
            revenue = f"{revenue:,}"
        elif revenue == 0:
            revenue = "Undefined"

        gain = movie.get('gain', "Undefined")
        if isinstance(gain, int):
            gain = f"{gain:,}"
        elif gain == 0:
            gain = "Undefined"

        vote_average = movie.get('vote_average', "Undefined")
        if isinstance(vote_average, float) or isinstance(vote_average, int):
            vote_average = f"{vote_average}"
        else:
            vote_average = "Undefined"

        original_language = movie.get('original_language', "Undefined")

        peliculas_data.append([
            runtime,
            release_date,
            title_original,
            budget,
            revenue,
            gain,
            vote_average,
            original_language
        ])

    headers = [
        'Duración',
        'Fecha de Publicación',
        'Título Original',
        'Presupuesto',
        'Ingresos Netos',
        'Ganancia',
        'Puntaje de Calificación',
        'Idioma Original'
    ]

    print("\nResultados de la búsqueda:")
    print(tabulate(peliculas_data, headers=headers, tablefmt='grid'))
    print()

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
