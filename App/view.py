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
    total_movies, first_five, last_five = logic.load_data(control, filename)
    print("\nTotal de películas cargadas: "+str(total_movies))
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
    title = input("Ingrese el título de la película: ").strip()
    original_language = input("Ingrese el idioma original de la película (ej. 'en' para inglés): ").strip().lower()
    
    if not title or not original_language:
        print("Título o idioma vacío. Por favor, ingrese ambos valores.")
        return

    movie, total_time = logic.req_1(control, title, original_language)
    
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
        print("No se encontró ninguna película con ese título y en ese idioma")



def print_req_2(control):
    n = int(input("El número (N) de ofertas a listar (ej.: 3, 5, 10 o 20): "))
    idioma = input("Ingrese el idioma original de la película (ej. 'en' para inglés): ").lower()  
    resultado,total_time = logic.req_2(control, idioma, n)
    if resultado == None:
        print("No se encontraron películas en ese idioma")
    total_peliculas = resultado['total_peliculas']
    peliculas = resultado['peliculas']
    headers = ["Fecha de publicación", "Título", "Presupuesto", "Recaudación", "Ganancia", "Duración (minutos)", "Puntaje", "Estado"]
    table_data = [
        [
            movie['Fecha de publicación'], 
            movie['Título'], 
            movie['Presupuesto'], 
            movie['Recaudación'], 
            movie['Ganancia'], 
            movie['Duración (minutos)'], 
            movie['Puntaje de calificación'],
            movie['Estado']
        ]
        for movie in peliculas
    ]
    print("Total de películas en el idioma: "+str(total_peliculas))
    print("El tiempo de ejecución es de "+str(total_time)+"(ms)")
    print(tabulate(table_data, headers, tablefmt="grid"))


def print_req_3(control):
    language = input("Ingrese el idioma original de publicación (ej. 'en', 'fr', 'zh'): ").strip().lower()
    start_date = input("Ingrese la fecha inicial del periodo (formato 'YYYY-MM-DD'): ").strip()
    end_date = input("Ingrese la fecha final del periodo (formato 'YYYY-MM-DD'): ").strip()
    if not language or not start_date or not end_date:
        print("Idioma o fechas vacías. Por favor, ingrese todos los valores.")
    result,total_time = logic.req_3(control, language, start_date, end_date)
    
    print("\nNúmero total de películas que cumplen el criterio: "+str(result['total']))
    if result['total'] > 0:
        print("Tiempo promedio de duración:"+ str(result['average_duration'])+"(mins)")
    
    if result['total'] == 0:
        print("No se encontraron películas que cumplan con los criterios especificados.")
    print("El tiempo de ejecución es de "+str(total_time)+"(ms)")
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

def print_req_4(control):
    estado = input("Ingrese el estado de producción de la película (ej.: 'Released', 'Rumored', etc): ").strip()
    start_date = input("Ingrese la fecha inicial del periodo (formato 'YYYY-MM-DD'): ").strip()
    end_date = input("Ingrese la fecha final del periodo (formato 'YYYY-MM-DD'): ").strip()
    
    if not estado or not start_date or not end_date:
        print("Estado o fechas vacías")
    result,total_time = logic.req_4(control, estado, start_date, end_date)
    
    if result is None:
        print("No se encontraron películas con ese estado")
    
    print("\nNúmero total de películas que cumplen el criterio: "+str(result['total']))
    if result['total'] > 0:
        print("Tiempo promedio de duración: "+str(result['average_duration'])+" minutos\n")
    if result['total'] == 0:
        print("No se encontraron películas que cumplan con los criterios especificados.")
        return
    print("El tiempo de ejecución es de "+str(total_time)+"(ms)")
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
                movie['original_language']
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
            "Idioma"
        ],
        tablefmt="grid"
    ))



def print_req_5(control):
    budget_range = input("Ingrese el rango de presupuesto (ej. '1000-1999'): ").strip()
    start_date = input("Ingrese la fecha inicial del periodo (formato 'YYYY-MM-DD'): ").strip()
    end_date = input("Ingrese la fecha final del periodo (formato 'YYYY-MM-DD'): ").strip()
    
    result,total_time = logic.req_5(control, budget_range, start_date, end_date)
    
    print("Número total de películas que cumplen el criterio: " + str((result['total'])))
    if result['total'] > 0:
        print("Presupuesto promedio: " + str((result['average_budget'])))
    print("El tiempo de ejecución es de "+str(total_time)+"(ms)")
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
                movie['original_language']
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
            "Idioma"
        ],
        tablefmt="grid"
    ))
def print_req_6(control):
    language = input("Ingrese el idioma original de publicación (ej. 'en', 'fr', 'zh'): ").strip().lower()
    start_year = input("Ingrese el año inicial del periodo (ej.: '1998'): ").strip()
    end_year = input("Ingrese el año final del periodo (ej.: '2024'): ").strip()
    result, total_time = logic.req_6(control, language, start_year, end_year)
    if not result:
        print("No se encontraron películas en el idioma " + str(language) + " entre los años " + str(start_year) + " y " + str(end_year))
        return
    print("El tiempo de ejecución es de " + str(total_time) + " ms")
    print("Películas en el idioma " + str(language) + " entre los años " + str(start_year) + " y " + str(end_year))
    table_data = []
    for item in result:
        if item["highest_rated_movie"]:
            highest_movie_title = item["highest_rated_movie"].get('title', 'None')
        else:
            highest_movie_title ='None'
        if item["highest_rated_movie"]:
            highest_movie_vote = item["highest_rated_movie"].get('vote_average', 'None')
        else: 
            highest_movie_vote = 'None'
        if item["lowest_rated_movie"]:
            lowest_movie_title = item["lowest_rated_movie"].get('title', 'None')
        else: lowest_movie_title = 'None'
        if item["lowest_rated_movie"]:
            lowest_movie_vote = item["lowest_rated_movie"].get('vote_average', 'None')
        else: 
            lowest_movie_vote = 'None'
        table_data.append([
            item["year"],
            item["total_movies"],
            item['avg_votes'],
            item["total_gain"],
            item["avg_runtime"],
            highest_movie_title,
            highest_movie_vote,
            lowest_movie_title,
            lowest_movie_vote
        ])
    headers = [
        "Año", "Total Películas", "Votación Promedio", "Ganancia Total", "Tiempo Promedio",
        "Película Mejor Votada", "Puntaje Mejor Votación", 
        "Película Peor Votada", "Puntaje Peor Votación"
    ]
    print(tabulate(table_data, headers, tablefmt="simple_grid"))

def print_req_7(control):
    company_name = input("Ingrese el nombre de la compañía productora: ").strip()
    start_year = input("Ingrese el año inicial del periodo (ej.: '1998'): ").strip()
    end_year = input("Ingrese el año final del periodo (ej.: '2024'): ").strip()

    if  company_name == None or start_year == None or end_year == None:
        print("Compañía o años vacíos. Por favor, ingrese todos los valores.")
        return

    result,total_time = logic.req_7(control, company_name, start_year, end_year)

    if  result == None:
        print("No se encontraron películas producidas por esa compañía entre los años brindados")
  

    print("Películas producidas por" + str(company_name) + " entre los años " + str(start_year) + " y " + str(end_year))
    print("El tiempo de ejecución es de "+str(total_time)+"(ms)")
    table_data = []
    for item in result:
        highest_movie_title = "None"
        highest_movie_vote = "None"
        lowest_movie_title = "None"
        lowest_movie_vote = "None"
        
        if item["highest_rated_movie"]:
            highest_movie_title = item["highest_rated_movie"]['title']
            highest_movie_vote = item["highest_rated_movie"]['vote_average']
        
        if item["lowest_rated_movie"]:
            lowest_movie_title = item["lowest_rated_movie"]['title']
            lowest_movie_vote = item["lowest_rated_movie"]['vote_average']

        table_data.append([
            item["year"],
            item["total_movies"],
            item["avg_votes"],
            item["total_gain"],
            item["avg_runtime"],
            highest_movie_title,
            highest_movie_vote,
            lowest_movie_title,
            lowest_movie_vote
        ])
    headers = ["Año", "Total Películas", "Votación Promedio", "Ganancia Total", "Tiempo Promedio",
               "Película Mejor Votada", "Puntaje Mejor Votación", 
               "Película Peor Votada", "Puntaje Peor Votación"]
    print(tabulate(table_data, headers, tablefmt="grid"))

def print_req_8(control):
    year = input("Ingrese el año (formato: YYYY): ").strip()
    genre = input("Ingrese el género de la película: ").strip().lower()
    result, total_time = logic.req_8(control, year, genre)
    print("El tiempo de ejecución es de:"+str(total_time)+"(ms)")
    total_movies = result['total']
    avg_vote = result['avg_vote']
    avg_duration = result['avg_duration']
    total_revenue = result['total_revenue']

    highest_rated_movie = "N/A"
    highest_vote = "N/A"
    if result['highest_rated_movie']:
        highest_rated_movie = result['highest_rated_movie']['title']
        highest_vote = result['highest_rated_movie']['vote_average']

    lowest_rated_movie = "N/A"
    lowest_vote = "N/A"
    if result['lowest_rated_movie']:
        lowest_rated_movie = result['lowest_rated_movie']['title']
        lowest_vote = result['lowest_rated_movie']['vote_average']

    data = [
        ["Total de películas", total_movies],
        ["Promedio de votación", avg_vote],
        ["Promedio de duración (min)", avg_duration],
        ["Ganancias acumuladas (USD)", total_revenue],
        ["Película con mejor votación", highest_rated_movie],
        ["Puntaje mejor votación", highest_vote],
        ["Película con peor votación", lowest_rated_movie],
        ["Puntaje peor votación", lowest_vote]
    ]
    print(tabulate(data, headers=["Descripción", "Valor"], tablefmt="grid"))


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
