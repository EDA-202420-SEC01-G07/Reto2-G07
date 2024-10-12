from DataStructures.Map import map_functions as mf
from DataStructures.Map import map_entry as me
from DataStructures.List import array_list as lt
import random

def new_map(num_elements, load_factor, prime=109345121):
    capacity = mf.next_prime(num_elements / load_factor)
    scale = random.randint(1, prime - 1)
    shift = random.randint(0, prime - 1)
    table = lt.new_list()
    table['elements'] = []
    for i in range(capacity):
        lt.add_last(table,{'key': None, 'value': None})
    table['size'] = 0
    map_linear_probing = {
        "prime": prime,
        "capacity": capacity,
        "scale": scale,
        "shift": shift,
        "table": table,
        "current_factor": 0,
        "limit_factor": load_factor,
        "size": 0,
        "type": "PROBING"
    }
    
    return map_linear_probing

def put(my_map, key, value):
    index = mf.hash_value(my_map, key)
    table = my_map["table"]["elements"]
    while me.get_key(table[index]) != None and me.get_key(table[index]) != "__EMPTY__":
        if me.get_key(table[index]) == key:
            me.set_value(my_map, value)
            return my_map
        index = (index + 1) % my_map["capacity"]
    me.set_key(table[index], key)
    me.set_value(table[index], value)
    my_map["size"] += 1
    my_map["current_factor"] = my_map["size"] / my_map["capacity"]
    if my_map["current_factor"] > my_map["limit_factor"]:
        rehash(my_map)
    return my_map


def contains(my_map, key):
    capacity = my_map["capacity"]
    table = my_map["table"]["elements"]
    index = mf.hash_value(my_map,key)
    while me.get_key(table[index]) != None:
        if me.get_key(table[index]) == key:
            return True
        index = (index + 1) % capacity
    return False
def get(my_map, key):
    capacity = my_map["capacity"]
    table = my_map["table"]["elements"]
    index = mf.hash_value(my_map,key)
    while me.get_key(table[index]) != None:
        if me.get_key(table[index]) == key:
            return me.get_value(table[index])
        index = (index + 1) % capacity 
    return None


def rehash(my_map):
    old_table = my_map['table']['elements']
    old_capacity = my_map['capacity']
    new_capacity = 2 * old_capacity + 1
    my_map['capacity'] = new_capacity
    my_map['table'] = lt.new_list()
    my_map['table']['elements'] = []
    for i in range(new_capacity):
        lt.add_last(my_map["table"],{'key': None, 'value': None})
    my_map['table']['size'] = 0
    my_map['size'] = 0 
    for i in old_table:
        if i['key'] != None and i['key'] != "__EMPTY__":
            put(my_map, i['key'], i['value'])
    return my_map

def size(my_map):
    return my_map["size"]
def is_empty(my_map):
    return my_map["size"] == 0
def key_set(my_map):
    rta = lt.new_list()
    for i in my_map["table"]["elements"]:
        if i['key'] != None and i['key'] != "__EMPTY__":
            lt.add_last(rta, i['key'])
    return rta

def remove(my_map, key):
    index = mf.hash_value(my_map, key)
    table = my_map["table"]["elements"]

    while me.get_key(table[index]) != None:
        if me.get_key(table[index]) == key:
            me.set_key(table[index], "__EMPTY__")
            me.set_value(table[index], "__EMPTY__")
            my_map["size"] -= 1  
        index = (index + 1) % my_map["capacity"]
    my_map["current_factor"] = my_map["size"] / my_map["capacity"]
    
    if my_map["current_factor"] > my_map["limit_factor"]:
        rehash(my_map)
    
    return my_map

def value_set(my_map):
    lista_final = lt.new_list()
    table = my_map["table"]["elements"]
    for entry in table:
        key = me.get_key(entry)
        if key != None and key != "__EMPTY__":
            value = me.get_value(entry)
            lt.add_last(lista_final, value)    

    return lista_final

def default_compare(key, element):    
    element_key = me.get_key(element) 
    if key == element_key:
        return 0
    elif key > element_key:
        return 1
    else:
        return -1

def find_slot(my_map, key, hash_value):
    table = my_map["table"]["elements"]
    capacity = my_map["capacity"]
    index = hash_value
    while True:
        entry = table[index]
        entry_key = me.get_key(entry)        
        if entry_key ==  None or entry_key == "__EMPTY__":
            return (False, index) 
        comparacion = default_compare(key, entry)
        if comparacion == 0:
            return (True, index) 
        index = (index + 1) % capacity

def is_available(table,pos):
    entry = table['elements'][pos]
    key = me.get_key(entry)
    if key == None or key == "__EMPTY__" :
        return True
    else:
        return False