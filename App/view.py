import sys
import os
import App.logic as logic
from DataStructures.List import array_list as al
from DataStructures.List import single_linked_list as sl
from DataStructures.Map import map_separate_chaining as ms
from tabulate import tabulate

default_limit = 1000
sys.setrecursionlimit(default_limit * 10)

def new_logic():
    """
    Se crea una instancia del controlador
    """
    control = logic.new_logic()
    return control

def print_menu():
    print("\nBienvenido")
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
    filename = input("Ingrese el nombre del archivo CSV: ").strip()
    
    if not filename:
        print("Nombre de archivo vacío. Por favor, intente nuevamente.")
        return
    if not os.path.isfile(filename):
        print("Archivo '{}' no encontrado. Por favor, verifique el nombre e intente nuevamente.".format(filename))
        return
    total_movies, first_five, last_five = logic.load_data(control, filename)
    print("\nTotal de películas cargadas: {}".format(total_movies))
    print("\nPrimeras 5 películas cargadas:")
    if first_five:
        print(tabulate([
            (
                movie['title'],
                movie['release_date'],
                movie['original_language'],
                movie['runtime'],
                movie['budget'],
                movie['revenue'],
                movie['gain']
            ) 
            for movie in first_five
        ], headers=[
            "Título", "Fecha", "Idioma", 
            "Duración (min)", "Presupuesto", 
            "Ingresos", "Ganancia"
        ], tablefmt="grid"))
    else:
        print("No hay películas para mostrar en las primeras 5 entradas.")
        
    print("\nÚltimas 5 películas cargadas:")
    if last_five:
        print(tabulate([
            (
                movie['title'],
                movie['release_date'],
                movie['original_language'],
                movie['runtime'],
                movie['budget'],
                movie['revenue'],
                movie['gain']
            ) 
            for movie in last_five
        ], headers=[
            "Título", "Fecha", "Idioma", 
            "Duración (min)", "Presupuesto", 
            "Ingresos", "Ganancia"
        ], tablefmt="grid"))
    else:
        print("No hay películas para mostrar en las últimas 5 entradas.")

def print_req_1(control):
    """
    Solicita al usuario el título y el idioma, busca la película y muestra los resultados.
    """
    title = input("Ingrese el título de la película: ").strip()
    original_language = input("Ingrese el idioma original de la película (ej. 'en' para inglés): ").strip().lower()
    
    if not title or not original_language:
        print("Título o idioma vacío. Por favor, ingrese ambos valores.")
        return

    movie = logic.req_1(control, title, original_language)
    
    if movie:
        print("\nPelícula encontrada:")
        if movie['gain'] != "Undefined":
            gain_formatted = "{:,}".format(int(movie['gain']))
        else:
            gain_formatted = movie['gain']
        movie_info = [[
            movie['title'], 
            movie['release_date'], 
            movie['original_language'], 
            movie['runtime'], 
            movie['budget'], 
            movie['revenue'], 
            gain_formatted, 
            movie['vote_average'], 
            movie['vote_count']
        ]]
        print(tabulate(movie_info, headers=["Título", "Fecha", "Idioma", "Duración", 
                                            "Presupuesto", "Ingresos", "Ganancia", "Calificación", "Votos"], tablefmt="grid"))
    else:
        print("No se encontró ninguna película con el título '{}' en el idioma '{}'.".format(title, original_language))

def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    pass

def print_req_3(control):
    """
    Solicita al usuario el idioma y el rango de fechas, ejecuta el requerimiento 3 y muestra los resultados.
    """
    print("\nEjecutar Requerimiento 3: Listar películas por idioma y periodo de tiempo")
    language = input("Ingrese el idioma original de publicación (ej. 'en', 'fr', 'zh'): ").strip().lower()
    start_date = input("Ingrese la fecha inicial del periodo (formato 'YYYY-MM-DD'): ").strip()
    end_date = input("Ingrese la fecha final del periodo (formato 'YYYY-MM-DD'): ").strip()
    
    if not language or not start_date or not end_date:
        print("Idioma o fechas vacías. Por favor, ingrese todos los valores.")
        return

    result = logic.req_3(control, language, start_date, end_date)
    
    if "error" in result:
        print("Error: {}".format(result['error']))
        return
    
    print("\nNúmero total de películas que cumplen el criterio: {}".format(result['total']))
    if result['total'] > 0:
        print("Tiempo promedio de duración: {:.2f} minutos\n".format(result['average_duration']))
    
    if result['total'] == 0:
        print("No se encontraron películas que cumplan con los criterios especificados.")
        return
    
    print("Películas encontradas:")
    print(tabulate(
        [
            (
                movie['release_date'],
                movie['title'],
                movie['budget'],
                movie['revenue'],
                movie['gain'],
                movie['runtime'],
                movie['vote_average'],
                movie['status']
            ) 
            for movie in result['movies']
        ],
        headers=[
            "Fecha de Publicación",
            "Título Original",
            "Presupuesto",
            "Ingresos",
            "Ganancia",
            "Duración (min)",
            "Calificación",
            "Estado"
        ],
        tablefmt="grid"
    ))

def debug_languages(control):
    """
    Función de depuración para listar todos los idiomas indexados y la cantidad de películas por idioma.
    """
    logic.debug_languages(control)


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
        elif int(inputs) == 10:
            debug_languages(control)
        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
