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
    catalog = ms.new_map(10000, 0.75)
    return catalog

def load_data(catalog, filename):
    """
    Carga los datos del archivo CSV al catálogo.
    Retorna el número total de películas cargadas, las listas de las primeras y últimas 5 películas,
    incluyendo la ganancia de cada una.
    """
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
            gain = calcular_gain(movie['budget'], movie['revenue'])  # Calcular la ganancia
            movie['gain'] = gain  # Agregar la ganancia al diccionario de la película
            ms.put(catalog, movie['id'], movie)  # Usar ms.put para insertar en el mapa
            movies_list.append(movie)
            if movie['title'].lower() == 'scoop' and movie['original_language'].lower() == 'en':
                print(f"Película encontrada durante la carga: {movie}")
    if total_movies >= 10:
        primeras = movies_list[:5]
        ultimas = movies_list[-5:]
    else:
        primeras = movies_list[:total_movies//2]
        ultimas = movies_list[total_movies//2:]

    return total_movies, primeras, ultimas

def process_movie_data(movie):
    """
    Procesa y limpia los datos de una película utilizando 'try-except' para la validación numérica.
    Asigna 'Undefined' si 'budget' o 'revenue' son 0 o no numéricos.
    """
    fields = ['release_date', 'budget', 'revenue', 'runtime', 'title', 'original_language']
    for field in fields:
        value = movie.get(field, "").strip()
        if not value:
            movie[field] = "Undefined"
        else:
            # Convertir a entero si es posible para budget y revenue
            if field in ['budget', 'revenue']:
                try:
                    numeric_value = int(float(value))
                    movie[field] = "Undefined" if numeric_value == 0 else numeric_value
                except ValueError:
                    movie[field] = "Undefined"
            else:
                movie[field] = value

    json_fields = ['production_companies', 'genres']
    for field in json_fields:
        raw_data = movie.get(field, '[]').strip()
        if not raw_data or raw_data == '[]':
            data_list = []
        else:
            if raw_data.startswith('[') and raw_data.endswith(']'):
                try:
                    data_list = json.loads(raw_data)
                except json.JSONDecodeError:
                    data_list = []
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
    Asigna 'Undefined' si budget, revenue o gain son 0 o no definidos.
    """
    if isinstance(budget, int) and isinstance(revenue, int):
        gain = revenue - budget
        if gain == 0:
            return "Undefined"
        return gain
    else:
        return "Undefined"

def normalize_text(text):
    """
    Normaliza el texto eliminando espacios adicionales y caracteres especiales.
    """
    text = text.strip().lower()
    return text

def req_1(catalog, title, language):
    """
    Retorna la información de una película que coincide con el título y el idioma original.
    
    Parámetros:
    - catalog: Mapa que contiene las películas.
    - title: Título de la película a buscar.
    - language: Idioma original de publicación de la película.
    
    Retorna:
    - Una lista con las películas que coinciden con los criterios.
    """
    matching_movies = []
    normalized_title = normalize_text(title)
    normalized_language = language.lower()

    for key in ms.key_set(catalog):
        movie = ms.get(catalog, key)
        if movie is None:
            continue  # Saltar si movie es None
        # Verificar que las claves existan y sean strings
        if ('title' in movie and isinstance(movie['title'], str) and
            'original_language' in movie and isinstance(movie['original_language'], str)):
            movie_title_normalized = normalize_text(movie['title'])
            movie_language_normalized = movie['original_language'].lower()
            if normalized_title == movie_title_normalized and movie_language_normalized == normalized_language:
                matching_movies.append(movie)
        else:
            continue  # Saltar si los campos no están presentes o no son del tipo esperado

    return matching_movies

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
