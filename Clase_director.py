from zope.interface import Interface #type:ignore
from zope.interface import implementer


class IDirector(Interface):#type:ignore
    def modificar_basico(self,dni, nuevo_basico):
        '''modifica el sueldo basico'''
        pass
    def modificar_porcentaje_por_cargo(self, dni, nuevo_porcentaje):
        pass
    def modificar_porcentaje_por_categoria(self,dni, nuevo_porcentaje):
        pass
    def modificar_importe_extra(self,dni, importe_extra):
        pass