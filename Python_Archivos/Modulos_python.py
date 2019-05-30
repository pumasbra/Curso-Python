__author__ = 'Brahian Velazquez Tellez '

""" Uso modulos en Python
    Pasa hacer uso de modulos en Python hacemos uso de la palabra import "nombre del modulo "
 """
""" importamos modulo platform """
import platform

print(platform.system())

""" importar definiendo un alias """
import datetime  as fecha
now = fecha.datetime.today()
print(now)

""" importar solo una funcion de un paquete """
from math import pi
print(pi)

"""" Importar clases creadas  para """

from  Clases_python import Animal
r = Animal()

