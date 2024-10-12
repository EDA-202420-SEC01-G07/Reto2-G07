from DataStructures.Map import map_functions as mf
from DataStructures.Map import map_entry as me
from DataStructures.List import array_list as lt
import random

def new_map(num_elements, load_factor, prime=109345121):
    """
    Crea un nuevo mapa con separate chaining.
    
    num_elements: número de elementos que puede almacenar inicialmente.
    load_factor: factor de carga máximo de la tabla.
    prime: número primo utilizado en la función hash.
    """
    capacity = mf.next_prime(int(num_elements / load_factor))
    scale = random.randint(1, prime - 1) 
    shift = random.randint(0, prime - 1)
    
    table = lt.new_list()
    for i in range(capacity):
        lt.add_last(table, [])
    
    map_separate_chaining = {
        "prime": prime,
        "capacity": capacity,
        "scale": scale,
        "shift": shift,
        "table": table,
        "current_factor": 0,
        "limit_factor": load_factor,
        "size": 0,
        "type": "CHAINING"
    }
    return map_separate_chaining

def put(my_map, key, value):
    """
    Ingresa una pareja llave-valor en la tabla de hash con separate chaining.
    Si la llave ya existe en la tabla, se reemplaza el valor.
    
    Parameters:
    - my_map (map_separate_chaining): El map a donde se guarda la pareja llave-valor.
    - key (any): La llave asociada a la pareja.
    - value (any): El valor asociado a la pareja.
    
    Returns:
    - El map actualizado con la nueva pareja llave-valor.
    """
    index = mf.hash_value(my_map, key)
    bucket = lt.get_element(my_map['table'], index)

    for pair in bucket:
        if pair['key'] == key:
            pair['value'] = value  
            return my_map 
    bucket.append({'key': key, 'value': value})
    my_map['size'] += 1 
    my_map['current_factor'] = my_map['size'] / my_map['capacity']  
    if my_map['current_factor'] > my_map['limit_factor']:
        rehash(my_map)  

    return my_map

def contains(my_map, key):
    """
    Valida si la llave key se encuentra en el map.
    
    Parameters:
    - my_map (map_separate_chaining): El map donde se guarda la pareja.
    - key (any): La llave asociada a la pareja.
    
    Returns:
    - True si la llave se encuentra en el map, False en caso contrario.
    """
    index = mf.hash_value(my_map, key) 
    bucket = lt.get_element(my_map['table'], index)
    for pair in bucket:
        if pair['key'] == key:
            return True 
    return False  

def get(my_map, key):
    """
    Retorna el valor asociado a la llave key en el map.
    
    Parameters:
    - my_map (map_separate_chaining): El mapa a examinar.
    - key (any): La llave a buscar.
    
    Returns:
    - El valor asociado a la llave key, o None si la llave no está en el mapa.
    """
    index = mf.hash_value(my_map, key) 
    bucket = lt.get_element(my_map['table'], index)

    for pair in bucket:
        if pair['key'] == key:
            return pair['value']
    return None

def remove(my_map, key):
    """
    Elimina la pareja llave-valor del map.
    
    Parameters:
    - my_map (map_separate_chaining): El map a examinar.
    - key (any): La llave a eliminar.
    
    Returns:
    - El map sin la llave key.
    """
    index = mf.hash_value(my_map, key) 
    bucket = lt.get_element(my_map['table'], index) 

    for i, pair in enumerate(bucket):
        if pair['key'] == key:
            bucket.pop(i)  
            my_map['size'] -= 1
            my_map['current_factor'] = my_map['size'] / my_map['capacity']  
            return my_map
    return my_map

def size(my_map):
    """
    Retorna el número de parejas llave-valor en el map.
    
    Parameters:
    - my_map (map_separate_chaining): El map a examinar.
    
    Returns:
    - Número de parejas llave-valor en el map (int).
    """
    return my_map['size']

def is_empty(my_map):
    """
    Indica si el map se encuentra vacío.
    
    Parameters:
    - my_map (map_separate_chaining): El map a examinar.
    
    Returns:
    - True si el map está vacío, False en caso contrario.
    """
    return my_map['size'] == 0

def key_set(my_map):
    """
    Retorna una lista con todas las llaves de la tabla de hash.
    
    Parameters:
    - my_map (map_separate_chaining): El map a examinar.
    
    Returns:
    - Una lista de llaves (array_list).
    """
    keys = lt.new_list()
    for i in range(my_map['capacity']):
        bucket = lt.get_element(my_map['table'], i) 
        for pair in bucket:
            lt.add_last(keys, pair['key'])

    return keys 

def value_set(my_map):
    """
    Retorna una lista con todos los valores de la tabla de hash.
    
    Parameters:
    - my_map (map_separate_chaining): El map a examinar.
    
    Returns:
    - Una lista de valores (array_list).
    """
    values = lt.new_list() 
    for i in range(my_map['capacity']):
        bucket = lt.get_element(my_map['table'], i) 

        for pair in bucket:
            lt.add_last(values, pair['value'])

    return values

def rehash(my_map):
    """
    Hace rehash de todos los elementos de la tabla de hash.
    
    Incrementa la capacidad de la tabla al doble y se hace rehash de todos los elementos de la tabla uno por uno.
    
    Parameters:
    - my_map (map_separate_chaining): El map a hacer rehash.
    
    Returns:
    - El map con la nueva capacidad.
    """
    old_table = my_map['table']
    old_capacity = my_map['capacity']
    new_capacity = mf.next_prime(old_capacity * 2)
    my_map['capacity'] = new_capacity
    
    new_table = lt.new_list()
    for i in range(new_capacity):
        lt.add_last(new_table, [])
    
    my_map['table'] = new_table
    my_map['size'] = 0
    
    for i in range(old_capacity):
        bucket = lt.get_element(old_table, i)
        for pair in bucket:
            put(my_map, pair['key'], pair['value'])
    
    return my_map

def default_compare(key, element):
    """
    Función de comparación por defecto. Compara una llave con la llave de un elemento llave-valor.
    
    Parameters:
    - key (any): La llave a comparar.
    - element (map_entry): El entry (par llave-valor) a comparar.
    
    Returns:
    - 0 si son iguales,
    - 1 si key > la llave del element,
    - -1 si key < la llave del element.
    """
    element_key = element['key']

    if key == element_key:
        return 0 
    elif key > element_key:
        return 1 
    else:
        return -1