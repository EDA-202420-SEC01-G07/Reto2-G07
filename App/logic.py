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
    Crea el catalogo para almacenar las estructuras de datos
    """
    catalog = {
        'movies': ms.new_map(100, 0.75), 
        'movies_by_language': ms.new_map(100, 0.75), 
        'movies_by_genre': ms.new_map(100, 0.75), 
    }
    return catalog


def load_data(catalog, filename):
    """
    Carga los datos del reto
    """
    filepath = os.path.join(data_dir, filename)
    total = 0
    loaded = []
    with open(filepath, encoding='utf-8') as file:
        movies = csv.DictReader(file)

        for movie in movies:
            genres_list = json.loads(movie["genres"])
            for genre in genres_list:
                genre_id = genre["id"]
                genre_name = genre["name"]
                if not ms.contains(catalog['movies_by_genre'], genre_id):
                    ms.put(catalog['movies_by_genre'], genre_id, genre_name)

            language = movie["original_language"]
            if not ms.contains(catalog['movies_by_language'], language):
                ms.put(catalog['movies_by_language'], language, movie["title"])

            movie_id = movie['id']
            if not ms.contains(catalog['movies'], movie_id):
                movie_data = {
                    'title': movie['title'],
                    'original_language': movie['original_language'],
                    'release_date': movie['release_date'],
                    'revenue': float(movie['revenue']) if movie['revenue'] else 0.0,
                    'budget': float(movie['budget']) if movie['budget'] else 0.0,
                    'runtime': float(movie['runtime']) if movie['runtime'] else 0.0,
                    'status': movie['status'],
                    'vote_average': float(movie['vote_average']) if movie['vote_average'] else 0.0,
                    'vote_count': int(movie['vote_count']) if movie['vote_count'] else 0,
                    'genres': genres_list,
                    'production_companies': json.loads(movie['production_companies']),
                }
                ms.put(catalog['movies'], movie_id, movie_data)
                loaded.append(movie_data)
                total += 1
    return total, loaded

def get_data(catalog, id):
    """
    Retorna los datos de una película dado su ID.

    Args:
    - catalog: Estructura que contiene el mapa con las películas.
    - id: ID de la película que se desea consultar.

    Returns:
    - Los datos de la película si existe, de lo contrario None.
    """
    if ms.contains(catalog['movies'], id):
        return ms.get(catalog['movies'], id)
    else:
        return None
    
def get_first_and_last_movies(movies_map, n):
    """
    Retorna las primeras y últimas 'n' películas en el mapa.
    """
    # Obtener todas las claves del mapa y convertirlas a lista
    keys = list(ms.key_set(movies_map))  # Convertir a lista para poder usar slicing
    size = ms.size(movies_map)
    
    # Seleccionar las primeras 'n' y las últimas 'n' claves
    first_keys = keys[:n]  # Primeras 'n' películas
    last_keys = keys[-n:]  # Últimas 'n' películas

    # Crear una lista para almacenar las películas seleccionadas
    selected_movies = []

    # Agregar las primeras 'n' películas
    for key in first_keys:
        movie = ms.get(movies_map, key)
        if movie:
            selected_movies.append({"key": key, "value": movie})
    
    # Agregar las últimas 'n' películas
    for key in last_keys:
        movie = ms.get(movies_map, key)
        if movie:
            selected_movies.append({"key": key, "value": movie})
    
    return selected_movies

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
