__author__ = 'Brahian Velazquez Tellez '

""" Sobreescritura de metodos en Python  """
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

class C(A,B):
    def __init__(self , a, b , c = None):
        print("Metodo __init__ clase C")
        if c is not None:
            B.__init__(self, c)

        A.__init__(self, a, b)

    def mensaje(self):
        print("Mensaje desde clase C")

    """ Se sobrecarga metodo """
    def sumar(self):
        return self.a + self.b  + 1;

    """ Acceder al  metodo Padre """
    def sumar_metodo_padre(self):
        return A.sumar(self)

""" creamos una instancia de clase C"""
print(C(2, 4).sumar())
print(C(2, 4).sumar_metodo_padre())
