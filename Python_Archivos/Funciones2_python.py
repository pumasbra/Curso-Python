__author__ = 'Brahian Velazquez Tellez '

"""  Mas Funciones en Python """

""" Funciones que devuelven mas de un argumento """
def funcion_retorna_tres_valores(a):
    return (a*2, a*3 , a*4 )

valor1, valor2, valor3 = funcion_retorna_tres_valores(5)
print(valor1, valor2, valor3)

"""  Se pueden solo obtener una solo variable si asi se requiere """
_ , valor5 , _ = funcion_retorna_tres_valores(5)
print(valor5)

""" Se pueden asignar funciones a otras variables y llamarlas desde estas"""

funcion = funcion_retorna_tres_valores
print(funcion(4))
print(type(funcion))
