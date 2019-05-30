__author__= 'Brahian Velazquez Tellez '

"""
Tipos de Datos Nativos en Python. Son los que vienen por default
"""

# Tipos de Dato :  int
a = 1
print(a, type(a))

b = 0x10
print(b, type(b))

# Tipo de Dato  : float
c = 1.2
print(c, type(c))
d = .5
print(d, type(d))

g = .314e1
print(g, type(g))

# Tipo de dato : complejo
e = 1 + 2j
f = complex(1, 2)
print(e, f)
print(type(e))


"""
Casteos entre los diferentes tipos
"""
# integer/string  -> float : float(x)
b2 = float(b)
print(b2, type(b2))

numero_String = "12"
numero_float = float(numero_String)
print(numero_float, type(numero_float))

# float/string -> integer  : int(x)  ,int(x,base=x)
print(int(3.14))
print(int("5"))
print(int("1010", base=2))

""" 
Principales operadores con  +, -, * , /, ** , % 
"""
print(1 + 2)
print(2 - 2)
print(3 * 3)
print(5 / 4)
print(2 ** 10)
print(5 % 4)


"""
String manejo de String
"""

nombre = "Brahian"
print(nombre, type(nombre))
print("La longitud del String %s" % nombre + " es %d" % len(nombre))

# un string multi-linea
datos = '''
Brahian
Velazquez
Tellez
'''
print(datos)

# Slicing : obtener de los indices 0:3
print(nombre[0:3])

# Slicing : obtener string seleccionando indices salteados
print(nombre[::2])

# Slicing :  obtener string invertido
print(nombre[::-1])

# Casteo de String   -> str(x)
print(str(3.14))
print(str([1, 2, 3]))


"""
Tipos de Datos Byte , Boolean y None
"""
# tipo bytes
byt = b'abc'
print(type(byt))

# Tipo Boolean y none
verdadero = True
falso = False

print(verdadero, type(verdadero))
print(falso, type(falso))

nada = None
print(nada, type(nada))
print(nada is None)



