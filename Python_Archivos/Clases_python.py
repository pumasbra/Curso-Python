__author__ = 'Brahian Velazquez Tellez '

"""  Programacion Orientada a Objetos en Python
     se usa la palabra class
"""
class Animal:

    """ Todos los metodos definidos en una clase deben tomar el argumento self """
    def fly(self):
        print("puedo volar")

""" creamos una instancia a la clase  y llamamos al metodo"""
a = Animal()
a.fly()
print(type(a))
