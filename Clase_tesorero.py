from zope.interface import Interface
from zope.interface import implementer

class ITesorero(Interface):
    def gastos_sueldos_por_empleado(self,dni):
        pass