__author__ = 'Brahian Velazquez Tellez '

"""
Declarando Funciones en Python
"""
# Todas las funciones llevan la palabra reservada def
def fun():
    print("Hola mundo")

fun()
print(type(fun))

# Funciones con argumentos
def sumar(a, b):
    return a + b

res = sumar(4, 67)
print(res)

# Funciones con Argumentos por default
def sumar2(a, b = 0):
    return a + b

print(sumar2(10, 10))
print(sumar2(10))

# Funciones con keywords arguments: Aquellas que no importa el orden de los argumentos
# ya que si coinciden el nombre del parametro en la definicon y el nombre en el llamado de la funcion
# quedaran enlazados.
def keyword_function(v, l):
    return v + " " + l

print(keyword_function("Hello" ,"Python"))
print(keyword_function(l="Python", v="Hello"))

# Funciones arbitrary arguments : Cuando no se saben el numero de argumentos
# * ->argumento como tupla , ** ->  se para argumento como diccionario

def arbitrary_function(*tup, **dic):
    for i in tup:
        print(i)
    for j in dic:
        print (j, dict[j])

tupla = (1,2,3,'r')
diccionario = {'a': 1, 'b': 2, 'c': 3}
arbitrary_function(tupla, diccionario)
