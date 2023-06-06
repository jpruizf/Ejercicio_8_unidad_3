class Persona:
    __cuil: int
    __dni: int
    __apellido: str
    __nombre: str
    __sueldo_basico: float
    __antiguedad: int
    __porcentaje: float
    def __init__(self):
        self.__cuil = 0
        self.__dni = 0
        self.__apellido = ""
        self.__nombre = ""
        self.__sueldo_basico = 0.0
        self.__antiguedad = 0
        self.__porcentaje = 0.0
    def __get_dni__(self):
        return self.__dni
    def __get_cuil__(self):
        return self.__cuil
    def __get_apellido_nombre__(self):
        return self.__apellido,self.__nombre
    def __get_sueldo__(self, nuevo_basico):
        if nuevo_basico is not None:
            self.__sueldo_basico = nuevo_basico
        return self.__sueldo_basico
    def __get_antiguedad__(self):
        return self.__antiguedad
    def __get_porcentaje__(self,nuevo_porcentaje):
        if nuevo_porcentaje is not None:
            self.__porcentaje = nuevo_porcentaje
        return self.__porcentaje