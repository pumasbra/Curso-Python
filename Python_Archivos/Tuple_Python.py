__author__ = 'Brahian Velazquez Tellez '

"""
Tipo de datos tuple en Python
"""

# Son un tipo  de Lista que tiene como caracteristica que es inmutable

#Declarando un dato tuple

tupla = (1, 2, 3, 4, [1, 4], False)

print(tupla, type(tupla))
# Igualmente se puede usar slicing
print(tupla[::-1])

# Si queremos modifcar nos mandara un error:

tupla[0] = 3
