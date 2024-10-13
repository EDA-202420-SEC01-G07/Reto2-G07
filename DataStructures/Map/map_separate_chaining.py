from DataStructures.Map import map_functions as mf
from DataStructures.Map import map_entry as me
from DataStructures.List import single_linked_list as sl
from DataStructures.List import array_list as lt
import random

def new_map(num_elements, load_factor, prime=109345121):
    capacity = mf.next_prime(int(num_elements / load_factor))
    scale = random.randint(1, prime - 1) 
    shift = random.randint(0, prime - 1)
    
    table = sl.new_list()
    for _ in range(capacity):
        bucket = sl.new_list()  
        sl.add_last(table, bucket)
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
    index = mf.hash_value(my_map, key)
    bucket = sl.get_element(my_map['table'], index)
    
    current = bucket['first']
    while current is not None:
        if current['info']['key'] == key:
            current['info']['value'] = value
            return my_map
        current = current['next']
    new_node = {
        'info': {'key': key, 'value': value},
        'next': bucket['first']
    }
    bucket['first'] = new_node 
    my_map['size'] += 1
    my_map['current_factor'] = my_map['size'] / my_map['capacity']
    if my_map['current_factor'] > my_map['limit_factor']:
        rehash(my_map)
    return my_map


def contains(my_map, key):
    index = mf.hash_value(my_map, key)
    bucket = sl.get_element(my_map['table'], index)
    if bucket is None or sl.size(bucket) == 0:
        return False
    current = sl.get_element(bucket, 0)
    if current is None:
        return False
    while current is not None:
        if current['key'] == key:
            return True
        current = sl.next(bucket, current)
    return False

def get(my_map, key):
    index = mf.hash_value(my_map, key)
    bucket = sl.get_element(my_map['table'], index)
    current = bucket['first'] if bucket is not None else None
    while current is not None:
        pair = current['info']
        if pair['key'] == key:
            return pair['value']
        current = current['next']
    return None

def remove(my_map, key):
    index = mf.hash_value(my_map, key)
    bucket = sl.get_element(my_map['table'], index)
    current = bucket['first'] if bucket is not None else None
    previous = None

    while current is not None:
        pair = current['info']
        if pair['key'] == key:
            if previous is None:
                bucket['first'] = current['next']
            else:
                previous['next'] = current['next']

            my_map['size'] -= 1
            my_map['current_factor'] = my_map['size'] / my_map['capacity']
            return my_map
        previous = current
        current = current['next']

    return my_map

def size(my_map):
    return my_map['size']

def is_empty(my_map):
    return my_map['size'] == 0

def key_set(my_map):
    keys = lt.new_list()  
    for i in range(my_map['capacity']):
        bucket = sl.get_element(my_map['table'], i) 
        current = bucket['first'] if bucket is not None else None 

        while current is not None: 
            pair = current['info']  
            lt.add_last(keys, pair['key']) 
            current = current['next']  

    return keys 

def value_set(my_map):
    values = lt.new_list() 
    for i in range(my_map['capacity']):
        bucket = sl.get_element(my_map['table'], i)  
        current = bucket['first'] if bucket is not None else None  

        while current is not None:  
            pair = current['info']  
            lt.add_last(values, pair['value']) 
            current = current['next']  

    return values

def rehash(my_map):
    old_table = my_map['table']
    old_capacity = my_map['capacity']
    new_capacity = mf.next_prime(old_capacity * 2)
    my_map['capacity'] = new_capacity

    new_table = sl.new_list()
    for i in range(new_capacity):
        sl.add_last(new_table, sl.new_list())  # Use sl.new_list() instead of lt.new_list()
    my_map['table'] = new_table
    my_map['size'] = 0  

    for i in range(old_capacity):
        bucket = sl.get_element(old_table, i)
        current = bucket['first'] if bucket is not None else None

        while current is not None:
            pair = current['info']
            put(my_map, pair['key'], pair['value'])
            current = current['next']

    return my_map