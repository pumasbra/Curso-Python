__author__ = 'Brahian Velazquez Tellez '

"""
Diccionarios en Python
"""

# Diccionario es un estructura desordenada que almacena valor del tipo  key:value

# Declarando un diccionario en Python
dic = {'k1': 12, 'k2': 17, 'k3': 18}
print(dic, type(dic))

# Para acceder a un valor lo hacemos por medio de la llave
print(dic.get('k1'))

# Para agregar uno a la lista
dic['k4'] = 'Hola'
print(dic)

# Para borrar se debe poner un bloque Try catch porque si
# no encuentra valor al borrar lanzara una excepcion del tipo: KeyError

try:
    del dic['K6']
except KeyError:
    print("No se encontro al valor")
finally:
    print("Eliminando uno que esta en el diccionario")
    del dic['k2']

print(dic)

# dict comprehension crear diccionariios a partir de estructuras de datos iterables
g = {i: chr(97 + i) for i in range(5)}
print(g)
