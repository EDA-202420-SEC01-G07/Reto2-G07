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
        'movies_by_id': ms.new_map(1000, 1.0),
        'movies_by_language': ms.new_map(1000, 1.0),
        'movies_by_year': ms.new_map(1000, 1.0),
        'movies_by_company': ms.new_map(1000, 1.0),
        'movies_by_title_language': ms.new_map(1000, 1.0),
        'movies_by_status': ms.new_map(1000, 1.0)
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
            movie_status = movie['status'].strip() 
            movie_year = get_year(movie['release_date'])
            movie_language = movie['original_language'].strip().lower()
            movie_companies = json.loads(movie['production_companies'])
            if movie['revenue'] and movie['revenue'] != '0':
                revenue = movie['revenue'] 
            else:
                revenue= "Undefined"
            if movie['budget'] and movie['budget'] != '0': 
                budget = movie['budget'] 
            else:
                budget="Undefined"
            movie['revenue'] = revenue
            movie['budget'] = budget
            if revenue != "Undefined" and budget != "Undefined":
                gain = float(revenue) - float(budget)
            else:
                gain = "Undefined"
            movie['gain'] = gain
            if movie['runtime']: 
                movie['runtime'] = float(movie['runtime']) 
            else:
                movie['runtime'] ="Undefined"

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
            status_list = ms.get(catalog['movies_by_status'], movie_status)
            if status_list is None:
                status_list = sl.new_list()
                ms.put(catalog['movies_by_status'], movie_status, status_list)
            sl.add_last(status_list, movie)
            
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
    return ms.get(catalog, id)

def req_1(catalog, title, original_language):
    key = (title, original_language)
    if ms.contains(catalog['movies_by_title_language'], key):
        return ms.get(catalog['movies_by_title_language'], key)
    else:
        return None
 

def req_2(catalog, language, n):
    inic= get_time()
    movie_list=ms.get(catalog['movies_by_language'], language)
    if movie_list==None:
        return None
    total_movies=sl.size(movie_list)
    if total_movies == 0:
        return None
    movies_info = []
    for i in range(total_movies):
        movie = sl.get_element(movie_list, i)
        if movie != None:
            movie['converted_date'] = datetime.strptime(movie['release_date'], '%Y-%m-%d')
            if movie['revenue'] != '0':
                revenue = movie['revenue'] 
            else:
                revenue="Undefined"
            if movie['budget'] != '0':
                budget = movie['budget'] 
            else:
                budget="Undefined"           
            if revenue != "Undefined" and budget != "Undefined":
                gain = float(revenue) - float(budget)
            else:
                gain = "Undefined"
    
            movie_info = {
                'Fecha de publicación': movie['release_date'],
                'Converted Fecha': movie['converted_date'],
                'Título': movie['title'],
                'Presupuesto': budget,
                'Recaudación': revenue,
                'Ganancia': gain,
                'Duración (minutos)': movie['runtime'],
                'Puntaje de calificación': movie['vote_average'],
                'Estado': movie['status']
            }
            movies_info.append(movie_info)


    linked_movie_list = sl.new_list()
    for movie in movies_info:
        sl.add_last(linked_movie_list, movie)
    sorted_movie_list = sl.merge_sort(linked_movie_list, sort_crit2)
    peliculas = []
    num_peliculas = min(n, sl.size(sorted_movie_list))
    for i in range(num_peliculas):
        pelicula = sl.get_element(sorted_movie_list, i)
        peliculas.append(pelicula)

    return {
        'total_peliculas': total_movies,
        'peliculas': peliculas
    }
def sort_crit2(movie1, movie2):
    return movie1['Converted Fecha'] > movie2['Converted Fecha']

def req_3(catalog, language, start_date_str, end_date_str):
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
    if total_movies > 0:
        average_duration = (total_duration / total_movies) 
    else: 
        average_duration=0
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
    if isinstance(value, str):
        return value
    elif isinstance(value, (int, float)):
        return "{:,}".format(int(value))
    else:
        return "Undefined"

def format_gain(gain):
    if gain == "Undefined":
        return gain
    elif isinstance(gain, (int, float)):
        return "{:,}".format(int(gain))
    else:
        return "Undefined"
        
def sort_crit(movie1, movie2):
    date1 = datetime.strptime(movie1['release_date'], '%Y-%m-%d')
    date2 = datetime.strptime(movie2['release_date'], '%Y-%m-%d')
    return date1 > date2
def req_4(catalog, estado, inicio, fin):
    start_date = datetime.strptime(inicio, '%Y-%m-%d')
    end_date = datetime.strptime(fin, '%Y-%m-%d')
    status_list = ms.get(catalog['movies_by_status'], estado.strip())
    if status_list == None:
        return {
            "total": 0,
            "average_duration": 0,
            "movies": []
        }

    matching_movies = []
    total_duration = 0
    current = status_list['first']

    while current:
        movie = current['info']
        if 'release_date' in movie and movie['release_date']:
            movie_date = datetime.strptime(movie['release_date'], '%Y-%m-%d')
            if start_date <= movie_date <= end_date:
                matching_movies.append(movie)
                if isinstance(movie['runtime'], (int, float)):
                    total_duration += movie['runtime']
        current = current['next']

    linked_movie_list = sl.new_list()
    for movie in matching_movies:
        sl.add_last(linked_movie_list, movie)
    sorted_movie_list = sl.merge_sort(linked_movie_list, sort_crit)
    total_movies = sl.size(sorted_movie_list)
    if total_movies > 0:
        average_duration = (total_duration / total_movies) 
    else:
        average_duration=0
    if total_movies > 20:
        sorted_movie_list = sl.sub_list(sorted_movie_list, 0, 10)
    formatted_movies = []
    for i in range(sl.size(sorted_movie_list)):
        movie = sl.get_element(sorted_movie_list, i)
        formatted_movie = {
            "release_date": movie['release_date'],
            "title": movie['title'],
            "budget": format_number(movie['budget']),
            "revenue": format_number(movie['revenue']),
            "gain": format_gain(movie.get('gain', "Undefined")),
            "runtime": movie['runtime'],
            "vote_average": movie['vote_average'],
            "status": movie['status'],
            "original_language": movie['original_language'] 
        }
        formatted_movies.append(formatted_movie)
    return {
        "total": total_movies,
        "average_duration": average_duration,
        "movies": formatted_movies
    }

 
def req_5(catalog, budget_range, start_date_str, end_date_str):
    
    start_budget, end_budget = map(int, budget_range.split('-'))
    start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
    end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
    

    matching_movies = []
    total_budget = 0
    total_movies = 0
    

    for year in range(start_date.year, end_date.year + 1):
        year_list = ms.get(catalog['movies_by_year'], year)
        if year_list == None:
            continue
        
        current = year_list['first']
        while current:
            movie = current['info']
            movie_date = datetime.strptime(movie['release_date'], '%Y-%m-%d')
            if start_date <= movie_date <= end_date:
                if movie['budget'] != 'Undefined' and start_budget <= float(movie['budget']) <= end_budget:
                    matching_movies.append(movie)
                    total_budget += float(movie['budget'])
                    total_movies += 1
            current = current['next']
    
 
    matching_movies.sort(key=lambda x: x['release_date'], reverse=True)
    if total_movies > 0:
        average_budget = total_budget / total_movies  
    else: 
        average_budget=0

    if total_movies > 20:
        matching_movies = matching_movies[:10]
    

    formatted_movies = []
    for movie in matching_movies:
        formatted_movie = {
            "release_date": movie['release_date'],
            "title": movie['title'],
            "budget": format_number(movie['budget']),
            "revenue": format_number(movie['revenue']),
            "gain": format_gain(movie.get('gain', "Undefined")),
            "runtime": movie['runtime'],
            "vote_average": movie['vote_average'],
            "original_language": movie['original_language']
        }
        formatted_movies.append(formatted_movie)

    return {
        "total": total_movies,
        "average_budget": average_budget,
        "movies": formatted_movies
    }

def req_6(catalog, language, start_year, end_year):
    start_year = int(start_year)
    end_year = int(end_year)
    result = []

    for year in range(start_year, end_year + 1):
        year_list = ms.get(catalog['movies_by_year'], year)

        total_movies = 0
        total_votes = 0
        total_runtime = 0
        total_gain = 0
        total_earnings = 0
        highest_rated_movie = None
        lowest_rated_movie = None

        if year_list != None:
            current = year_list['first']
            while current:
                movie = current['info']
                if movie['original_language'].lower() == language.lower() and movie['status'] == 'Released':
                    total_movies += 1
                    if 'vote_average' in movie and isinstance(movie['vote_average'], (int, float)):
                        vote_average = float(movie['vote_average'])
                        total_votes += vote_average
                    else:
                        vote_average = 0

                    if isinstance(movie['runtime'], (int, float)):
                        total_runtime += movie['runtime'] 
                    else:
                        total_runtime = 0

                    if isinstance(movie['gain'], (int, float)):
                        total_gain += movie['gain']

                    if isinstance(movie['revenue'], (int, float)):
                        total_earnings += float(movie['revenue'])
                    if highest_rated_movie is None or (isinstance(movie['vote_average'], (int, float)) and vote_average > float(highest_rated_movie['vote_average'])):
                        highest_rated_movie = movie
                    if lowest_rated_movie is None or (isinstance(movie['vote_average'], (int, float)) and vote_average < float(lowest_rated_movie['vote_average'])):
                        lowest_rated_movie = movie

                current = current['next']

        if total_movies > 0:
            avg_votes = total_votes / total_movies
            if total_runtime > 0:
                avg_runtime = total_runtime / total_movies 
            else: 
                avg_runtime="None"
            result.append({
                "year": year,
                "total_movies": total_movies,
                "avg_votes": avg_votes,
                "avg_runtime": avg_runtime,
                "total_gain": total_gain if total_gain > 0 else "Undefined",
                "highest_rated_movie": highest_rated_movie,
                "lowest_rated_movie": lowest_rated_movie
            })

    return result



def req_7(catalog, company_name, start_year, end_year):
    start_year = int(start_year)
    end_year = int(end_year)
    result = []
    
    for year in range(start_year, end_year + 1):
        year_list = ms.get(catalog['movies_by_year'], year)
        if year_list is not None:
            total_movies = 0
            total_votes = 0
            total_runtime = 0
            total_gain = 0
            highest_rated_movie = None
            lowest_rated_movie = None

            current = year_list['first']
            while current:
                movie = current['info']

                production_companies = json.loads(movie['production_companies'])
                for company in production_companies:
                    if company['name'].lower() == company_name.lower():
                        total_movies += 1
        
                        if 'vote_average' in movie and isinstance(movie['vote_average'], (int, float)):
                            vote_average = float(movie['vote_average'])
                            total_votes += vote_average
                        else:
                            vote_average = 0

                        if isinstance(movie['runtime'], (int, float)):     
                            total_runtime += movie['runtime'] 
                    
                        if isinstance(movie['gain'], (int, float)):
                            total_gain += movie['gain']
                        
                        if highest_rated_movie is None or (isinstance(movie['vote_average'], (int, float)) and vote_average > float(highest_rated_movie['vote_average'])):
                            highest_rated_movie = movie
                        
                       
                        if lowest_rated_movie is None or (isinstance(movie['vote_average'], (int, float)) and vote_average < float(lowest_rated_movie['vote_average'])):
                            lowest_rated_movie = movie

                current = current['next']

            if total_movies > 0:
                avg_votes = total_votes / total_movies
                if total_runtime > 0: 
                    avg_runtime = total_runtime / total_movies 
                else:
                    avg_runtime="Undefined"
                result.append({
                    "year": year,
                    "total_movies": total_movies,
                    "avg_votes": avg_votes,
                    "avg_runtime": avg_runtime,
                    "total_gain": total_gain if total_gain > 0 else "Undefined",
                    "highest_rated_movie": highest_rated_movie,
                    "lowest_rated_movie": lowest_rated_movie
                })

    return result



def req_8(catalog, year, genre):

    year = int(year)
    genre = genre.lower()
    year_list = ms.get(catalog['movies_by_year'], year)

    if not year_list:
        return {
            "total": 0,
            "avg_vote": 0,
            "avg_duration": 0,
            "total_revenue": 0,
            "highest_rated_movie": None,
            "lowest_rated_movie": None
        }
    total_movies = 0
    total_votes = 0
    total_duration = 0
    total_revenue = 0
    highest_rated_movie = None
    lowest_rated_movie = None
    current = year_list['first']
    while current:
        movie = current['info']
        movie_genres = [g['name'].lower() for g in json.loads(movie['genres'])]
        if genre in movie_genres and movie['status'] == 'Released':
            total_movies += 1
            vote_average = float(movie['vote_average']) if movie['vote_average'] else 0
            total_votes += vote_average
            total_duration += movie['runtime'] if isinstance(movie['runtime'], (int, float)) else 0
            gain = movie.get('gain', 0)
            total_revenue += gain if isinstance(gain, (int, float)) else 0
            if highest_rated_movie == None or vote_average > float(highest_rated_movie['vote_average']):
                highest_rated_movie = movie
            if lowest_rated_movie == None or vote_average < float(lowest_rated_movie['vote_average']):
                lowest_rated_movie = movie

        current = current['next']

    avg_vote = total_votes / total_movies if total_movies > 0 else 0
    avg_duration = total_duration / total_movies if total_movies > 0 else 0

    return {
        "total": total_movies,
        "avg_vote": avg_vote,
        "avg_duration": avg_duration,
        "total_revenue": total_revenue,
        "highest_rated_movie": highest_rated_movie,
        "lowest_rated_movie": lowest_rated_movie
    }

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
