__author__ = 'Brahian Velazquez Tellez '

"""
Tipo de datos Set en Python
"""
# Set es conjunto de elementos que estaran desordenados y no se pueden acceder a los datos mediante indices

set_ejemplo = {"apple", 34, True}
print(set_ejemplo, type(set_ejemplo))

# no se pueden acceder a los elementos directamente solo puedes saber si los elementos existen
print("apple" in set_ejemplo)

# no se pueden modificar valores asignados pero si se pueden agregar mas
set_ejemplo.add('uno mas')
print(set_ejemplo)

# Para eliminar
set_ejemplo.remove(34)
print(set_ejemplo)
