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
    # El mapa almacenará las películas bajo su ID.
    catalog = ms.new_map(10000, 0.75)
    return catalog

def load_data(catalog, filename):
    """
    Carga los datos del archivo CSV al catálogo.
    Retorna el número total de películas cargadas y las listas de las primeras y últimas 5 películas.
    """
    data_dir = 'Data'
    filepath = os.path.join(data_dir, filename)
    
    primeras = [] 
    ultimas = [] 
    movies_list = [] 
    total_movies = 0 

    with open(filepath, encoding='utf-8') as file:
        movies = csv.DictReader(file)
        
        for movie in movies:
            total_movies += 1
            process_movie_data(movie)
            catalog[movie['id']] = movie
            movies_list.append(movie)
    if total_movies >= 10:
        primeras = movies_list[:5]
        ultimas = movies_list[-5:]
    else:
        primeras = movies_list[:total_movies//2]
        ultimas = movies_list[total_movies//2:]

    return total_movies, primeras, ultimas

def process_movie_data(movie):
    """
    Procesa y limpia los datos de una película sin usar 'try'.
    """
    fields = ['release_date', 'budget', 'revenue', 'runtime', 'title', 'original_language']
    for field in fields:
        if not movie.get(field):
            movie[field] = "Undefined"
    json_fields = ['production_companies', 'genres']
    for field in json_fields:
        raw_data = movie.get(field, '[]')
        if raw_data.strip() == '' or raw_data.strip() == '[]':
            data_list = []
        else:
            raw_data = raw_data.strip()
            if raw_data[0] == '[' and raw_data[-1] == ']':
                data_list = json.loads(raw_data)
            else:
                data_list = []

        processed_list = []
        for item in data_list:
            if isinstance(item, dict) and 'name' in item and 'id' in item:
                processed_list.append({'name': item['name'], 'id': item['id']})
            else:
                processed_list.append({'name': "Undefined", 'id': "Undefined"})
        movie[field] = processed_list

def get_data(catalog, id):
    """
    Retorna los datos de una película dado su ID.
    """
    return ms.get(catalog, id)

def calcular_gain(budget, revenue):
    """
    Calcula la ganancia de una película a partir del presupuesto y los ingresos.
    """
    if budget != "Undefined" and revenue != "Undefined":
        gain = int(revenue) - int(budget)
    else:
        gain = "Undefined"
    return gain

def req_1(catalog):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    pass


def req_2(catalog):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(catalog):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


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

