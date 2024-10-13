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
            movie_language = movie['original_language']
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
    
def process_movie_data(movie):
    """
    Procesa y limpia los datos de una película.
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

def req_1(catalog, title, original_language):
    """
    Retorna el resultado del requerimiento 1
    """
    key = (title, original_language)
    
    # Buscar la película en el mapa usando la clave compuesta
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
