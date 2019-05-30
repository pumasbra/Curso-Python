__author__ = 'Brahian Velazquez Tellez '

"""  Herencia en Python Clase Padre """
class Animal:
    def __init__(self , color, tamanio , tipo , vuela = False):
        self.color = color
        self.tamanio = tamanio
        self.tipo = tipo
        self.vuela = vuela

    def imprimir(self):
        print("Color :", self.color )
        print("Tamanio :", self.tamanio )
        print("Tipo :", self.tipo )

    def fly(self):
        if self.vuela:
            print("puedo volar")
        else:
            print("no puedo volar")

"""  Herencia en Python Clase Hija
    Para heredar de una clase solo declarar la clase y poner entre parentesis
    la clase de la cual hereda.   """

class Perro(Animal):

    """ Se debe llamar al methodo __init__ de la clase padre (Opcional)
        Para usar con herencia multiple """
    def __init__(self, color, tamanio, tipo):
        Animal.__init__(self, color, tamanio, tipo)

    def ladra(self):
        print("Woof!")


d = Perro("negro", " grande" , "canino")
d.imprimir()
print("------")
d.fly()
d.ladra()
