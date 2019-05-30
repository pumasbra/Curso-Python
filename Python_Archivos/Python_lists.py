__author__ = 'Brahian Velazquez Tellez '

"""
Tipo de datos List en Python
"""
# Para declarar una lista en python. No tiene que ser del mismo tipo de dato
lista = ['python', 3, 'in', 'one']

print(lista)
print(len(lista), type(lista))

print(lista[0])

lista.append(True)
lista.append(23)

# borrar  : -> pop(x)
print(lista.pop())
print(lista.pop(0))

# slicing al igual que strings
print(lista[1:])
print(lista[-1])

# List Comprehension : Permite crear listas en una sola linea, basado en otras listas o datos iterables
# Sintaxis: [ expression for item in list if conditional ]
oracion = " dando curso de python"

# obtenemos la longitud de cada letra y lo guardamos en otra lista
longitud_palabra = [len(word) for word in oracion.split()]
print(longitud_palabra)

# obtenemos los elementos pares de una lista
numeros = range(1, 11)  # [1,2,3,4,5,6,7,8,9,10]

pares = [index for index in numeros if index % 2 == 0]
print(pares)
