__author__ = 'Brahian Velazquez Tellez '

"""  Herencia Multiple en Python  """
class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        print("Metodo __init__ clase A")

    def sumar(self):
        return self.a + self.b

class B:
    def __init__(self, c):
        self.c = c
        print("Metodo __init__ clase B")

    def al_cuadrado(self):
        return self.c ** 2

""" Clase C hereda de la clase A y B """
class C(A,B):
    def __init__(self , a, b , c = None):
        print("Metodo __init__ clase C")
        if c is not None:
            B.__init__(self, c)

        A.__init__(self, a, b)

    def mensaje(self):
        print("Mensaje desde clase C")

""" creamos una instancia de clase C"""
c = C(4,5,6)
print(c.sumar())
print(c.al_cuadrado())
c.mensaje()

print("------")
c2 = C(4,5, 6)

c2.al_cuadrado()
