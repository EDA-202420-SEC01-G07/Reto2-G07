import time
import csv
from datetime import time,datetime
from tabulate import tabulate
import json
import os
from DataStructures.List import single_linked_list as sl
from DataStructures.List import array_list as al
from DataStructures.Map import map_separate_chaining as ms
import time

project_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_dir = os.path.join(project_dir, 'Data')

def new_logic():
    """
    Crea el catálogo con una sola estructura de datos (un mapa).
    """
    catalog = {
        'movies_by_id': ms.new_map(1000, 0.7),
        'movies_by_language': ms.new_map(1000, 0.7),
        'movies_by_year': ms.new_map(1000, 0.7),
        'movies_by_company': ms.new_map(1000, 0.7),
        'movies_by_title_language': ms.new_map(1000, 0.7)
    }
    return catalog

def load_data(catalog, filename):
    first_five = []
    last_five = []
    filepath = os.path.join(data_dir, filename)
    
    with open(filepath, encoding='utf-8') as file:
        movies = csv.DictReader(file)
        count = 0
        total_movies = 0

        for movie in movies:
            total_movies += 1
            movie_year = get_year(movie['release_date'])
            movie_language = movie['original_language'].strip().lower()
            movie_companies = json.loads(movie['production_companies'])
            revenue = movie['revenue'] if movie['revenue'] and movie['revenue'] != '0' else "Undefined"
            budget = movie['budget'] if movie['budget'] and movie['budget'] != '0' else "Undefined"
            movie['revenue'] = revenue
            movie['budget'] = budget
            if revenue != "Undefined" and budget != "Undefined":
                gain = float(revenue) - float(budget)
            else:
                gain = "Undefined"
            movie['gain'] = gain
            movie['runtime'] = float(movie['runtime']) if movie['runtime'] else "Undefined"

            key = (movie['title'], movie_language)
            ms.put(catalog['movies_by_title_language'], key, movie)
            year_list = ms.get(catalog['movies_by_year'], movie_year)
            if year_list is None:
                year_list = sl.new_list()
                ms.put(catalog['movies_by_year'], movie_year, year_list)
            sl.add_last(year_list, movie)
            for company in movie_companies:
                company_name = company['name']
                company_list = ms.get(catalog['movies_by_company'], company_name)
                if company_list is None:
                    company_list = sl.new_list()
                    ms.put(catalog['movies_by_company'], company_name, company_list)
                sl.add_last(company_list, movie)
            
            language_list = ms.get(catalog['movies_by_language'], movie_language)
            if language_list is None:
                language_list = sl.new_list()
                ms.put(catalog['movies_by_language'], movie_language, language_list)
            sl.add_last(language_list, movie)
            
            if count < 5:
                first_five.append(movie)
            last_five.append(movie)
            if len(last_five) > 5:
                last_five.pop(0)
            count += 1
    return total_movies, first_five, last_five
    
def get_year(release_date):
    date_obj = datetime.strptime(release_date, '%Y-%m-%d')
    return date_obj.year

def get_data(catalog, id):
    """
    Retorna los datos de una película dado su ID.
    """
    return ms.get(catalog, id)

def req_1(catalog, title, original_language):
    """
    Retorna el resultado del requerimiento 1
    """
    key = (title, original_language)
    
    if ms.contains(catalog['movies_by_title_language'], key):
        return ms.get(catalog['movies_by_title_language'], key)
    else:
        return None

def req_2(catalog):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass

def req_3(catalog, language, start_date_str, end_date_str):
    """
    Lista las películas en un idioma específico dentro de un rango de fechas.

    Parámetros:
        catalog (dict): El catálogo de películas.
        language (str): Idioma original de publicación (ej. 'en', 'fr', 'zh').
        start_date_str (str): Fecha inicial en formato '%Y-%m-%d'.
        end_date_str (str): Fecha final en formato '%Y-%m-%d'.

    Retorna:
        dict: Contiene el número total de películas, tiempo promedio de duración y la lista de películas.
    """
    start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
    end_date = datetime.strptime(end_date_str, '%Y-%m-%d')

    language_list = ms.get(catalog['movies_by_language'], language)
    if language_list is None:
        return {
            "total": 0,
            "average_duration": 0,
            "movies": []
        }

    matching_movies = []
    total_duration = 0
    current = language_list['first']
    while current:
        movie = current['info']
        movie_date = datetime.strptime(movie['release_date'], '%Y-%m-%d')

        if start_date <= movie_date <= end_date:
            matching_movies.append(movie)
            if isinstance(movie['runtime'], (int, float)):
                total_duration += movie['runtime']
        
        current = current['next']
    matching_movies.sort(key=lambda x: x['release_date'], reverse=True)

    total_movies = len(matching_movies)
    average_duration = (total_duration / total_movies) if total_movies > 0 else 0
    if total_movies > 20:
        matching_movies = matching_movies[:10]
    formatted_movies = []
    for movie in matching_movies:
        formatted_movie = {
            "release_date": movie['release_date'],
            "title": movie['title'],
            "budget": format_number(movie['budget']),
            "revenue": format_number(movie['revenue']),
            "gain": format_gain(movie['gain']),
            "runtime": movie['runtime'],
            "vote_average": movie['vote_average'],
            "status": movie['status']
        }
        formatted_movies.append(formatted_movie)

    return {
        "total": total_movies,
        "average_duration": average_duration,
        "movies": formatted_movies
    }
    
def format_number(value):
    """
    Formatea un número con comas como separadores de miles.
    Si el valor es 'Undefined', lo retorna tal cual.
    """
    if isinstance(value, str):
        return value
    elif isinstance(value, (int, float)):
        return "{:,}".format(int(value))
    else:
        return "Undefined"

def format_gain(gain):
    """
    Formatea la ganancia, manejando el caso 'Undefined'.
    """
    if gain == "Undefined":
        return gain
    elif isinstance(gain, (int, float)):
        return "{:,}".format(int(gain))
    else:
        return "Undefined"

    
def req_4(catalog):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(catalog):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(catalog):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


def req_7(catalog):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    pass


def req_8(catalog):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed

