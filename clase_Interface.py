from zope.interface import Interface
from zope.interface import implementer

class IColeccion(Interface):
    def insertarElemento(self, elemento, posicion):
        pass
    def agregarElemento(self, elemento):
        pass
    def mostrarElemento(self, posicion):
        pass

@implementer(IColeccion)
class Coleccion(object):
    __coleccion: list
    def __init__(self):
        self.__coleccion = []
    def insertarElemento(self, elemento, posicion):
        try:
            assert 0 <= posicion <= len(self.__coleccion)
            self.__coleccion.insert(posicion, elemento)
        except AssertionError as e:
            print(e)
    
    def agregarElemento(self, elemento):
        self.__coleccion.append(elemento)
    def mostrarElemento(self, posicion):
        try:
            assert 0 <= posicion < len(self.__coleccion)
            print(self.__coleccion[posicion])
        except AssertionError as e:
            print(e)