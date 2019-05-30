__author__ = 'Brahian Velazquez Tellez '

"""  Funcion del metodo __init__ """
class Animal:
    """ Metodo __init__  se ejecuta cada vez que se intancia un objeto
    Para indicar que un atributo pertenece a la clase se usa la palabra self
    """
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


""" creamos una instancia a la clase """
quetzal = Animal("verde", "mediano" , 'ave' , True)
quetzal.imprimir()
quetzal.fly()
print("_________________")
perro = Animal(None,"chico", 'mamifero')
perro.imprimir()
perro.fly()
