from Clase_nodo import Nodo
from Clase_director import IDirector
from Clase_tesorero import ITesorero
@implementer(IDirector)
@implementer(ITesorero)

class Lista:
    __comienzo: Nodo
    __actual: Nodo
    __indice: int
    __tope: int
    def __init__(self):
        self.__comienzo = None
        self.__actual = None
        self.__tope = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice += 1
            dato = self.__actual.get_datos()
            self.__actual = self.__actual.get_siguiente()
            return dato
    def agregar_persona(self, persona):
        nodo = Nodo(persona)
        nodo.set_siguiente(self.__comienzo)
        self.__comienzo = nodo
        self.__actual = nodo
        self.__tope += 1
    def gastos_sueldos_por_empleado(self,dni):
        aux = self.__comienzo
        encontrado = False
        if aux.__get_datos__().__get_dni__() == int(dni):
            encontrado = True
            print("¡DNI encontrado!")
            print(f"{aux.__get_datos__()}")
            self.__comienzo = aux.__get_siguiente__()
            self.__tope -= 1
        else:
            anterior = aux
            aux = aux.__get_siguiente__()
            while not encontrado and aux is not None:
                if aux.__get_datos__().__get_dni__() == dni:
                    encontrado = True
                    print("¡DNI encontrado!")
                else:
                    anterior = aux
                    aux = aux.__get_siguiente__()
            if encontrado:
                print("¡DNI encontrado!")
                print(f"{aux.__get_datos__()}")
                anterior.set_siguiente(aux.__get_siguiente__())
                self.__tope -= 1
            else:
                print(f"El DNI {dni}, no se encuentra en la lista")
    def tesorero(self):
        agente = int(input("Ingrese el DNI de un agente >> "))
        interface_tesorero = ITesorero.gastos_sueldos_por_empleado(agente)
        if interface_tesorero == None:
            print(f"DNI {agente}, no encontrado o invalido")
        else:
            print(agente)
    def modificar_basico(self,dni,nuevo_basico):
        aux = self.__comienzo
        encontrado = False
        if aux.__get_datos__().__get_dni__() == int(dni):
            encontrado = True
            print("¡DNI encontrado!")
            aux.__get_datos__().__get_sueldo__(nuevo_basico) #type:ignore
            self.__comienzo = aux.__get_siguiente__()
            self.__tope -= 1
        else:
            anterior = aux
            aux = aux.__get_siguiente__()
            while not encontrado and aux is not None:
                if aux.__get_datos__().__get_dni__() == dni:
                    encontrado = True
                    print("¡DNI encontrado!")
                else:
                    anterior = aux
                    aux = aux.__get_siguiente__()
            if encontrado:
                print("¡DNI encontrado!")
                aux.__get_datos__().__get_sueldo__(nuevo_basico) #type:ignore
                anterior.set_siguiente(aux.__get_siguiente__())
                self.__tope -= 1
            else:
                print(f"El DNI {dni}, no se encuentra en la lista")
    def director(self):
        agente = 0
        agente = int(input("Ingrese el DNI de un agente >> "))
        nuevo_basico = float(input("Ingrese el nuevo sueldo basico >> "))
        interface_director = IDirector.modificar_basico(agente, nuevo_basico)
        if interface_director == None:
            print(f"DNI {agente}, no encontrado o invalido")
        else:
            print(agente)
    def modificar_porcentaje_por_cargo(self, dni, nuevo_porcentaje):
        aux = self.__comienzo
        encontrado = False
        if aux.__get_datos__().__get_dni__() == int(dni):
            encontrado = True
            print("¡DNI encontrado!")
            aux.__get_datos__().__get_porcentaje__(nuevo_porcentaje) #type:ignore
            self.__comienzo = aux.__get_siguiente__()
            self.__tope -= 1
        else:
            anterior = aux
            aux = aux.__get_siguiente__()
            while not encontrado and aux is not None:
                if aux.__get_datos__().__get_dni__() == int(dni):
                    encontrado = True
                    print("¡DNI encontrado!")
                else:
                    anterior = aux
                    aux = aux.__get_siguiente__()
            if encontrado:
                print("¡DNI encontrado!")
                aux.__get_datos__().__get_porcentaje__(nuevo_porcentaje) #type:ignore
                anterior.set_siguiente(aux.__get_siguiente__())
                self.__tope -= 1
            else:
                print(f"El DNI {dni}, no se encuentra en la lista")
    def interface_director(self):
        agente = 0
        agente= int(input("Ingrese el DNI de un agente >> "))
        nuevo_porcentaje = float(input("Ingrese el nuevo porcentaje >>"))
        interface_director = IDirector.modificar_porcentaje_por_cargo(agente,nuevo_porcentaje)
    def modificar_importe_extra(self, dni, nuevo_importe_extra):
        aux = self.__comienzo
        encontrado = False
        if aux.__get_datos__().__get_dni__() == int(dni):
            encontrado = True
            print("¡DNI encontrado!")
            aux.__get_datos__().__get_importe__(nuevo_importe_extra)
            self.__comienzo = aux.__get_siguiente__()
            self.__tope -= 1
        else:
            ant = aux
            aux = aux.__get_siguiente__()
            while not encontrado and aux is not None:
                if aux.__get_datos__().__get_dni__() == int(dni):
                    encontrado = True
                    print("¡DNI encontrado!")
                else:
                    ant = aux
                    aux = aux.__get_siguiente__()
            if encontrado:
                print("¡DNI encontrado!")
                aux.__get_datos__().__get_importe__(nuevo_importe_extra)
                ant.set_siguiente(aux.__get_siguiente__())
                self.__tope -= 1
    def interface_director(self):
        agente = 0
        agente= int(input("Ingrese el DNI de un agente >> "))
        nuevo_importe = float(input("Ingrese el nuevo importe extra >>"))
        interface_director = IDirector.modificar_importe_extra(agente,nuevo_importe)
    def insetar_persona(self, persona, posicion):

        if posicion < 0 or posicion > self.__tope:
            raise ValueError("Posicion de insercion no valida")
        nuevo_nodo = Nodo(persona)

        if posicion == 0:
            nuevo_nodo.set_siguiente(self.__comienzo)
            self.__comienzo = nuevo_nodo
        else:
            nodo_anterior = self.__comienzo
            for _ in range(posicion - 1):
                nodo_anterior = nodo_anterior.__get_siguiente__()
            
            nuevo_nodo.set_siguiente(nodo_anterior.set_siguiente())
            nodo_anterior.__get_siguiente__(nuevo_nodo)
        self.__tope += 1
    def mostrar_persona_por_posicion(self, posicion):
        if posicion < 0 or posicion > self.__tope:
            raise ValueError("Posicion de insercion no valida")
        aux = self.__comienzo
        nuevo = Nodo(posicion)
        if posicion is not None:
            print(f"Persona almacenada en la posicion ingresada >> {aux.__get_datos__()}")
            nuevo.__get_siguiente__()
    def listar_datos_docente_investigadores(self, carrera):
        aux = self.__comienzo
        while aux is not None:
            if aux.__get_datos__().__get_carrera__().lower() == carrera.lower():
                if aux.__get_datos__().__get_cargo__().lower() == 'docente investigador':
                    print(aux.__get_datos__().__get_apellido_nombre__())
                    aux = aux.__get_siguiente__()
    def contar_docentes_investidor_por_area(self, area):
        aux = self.__comienzo
        cant = 0
        while aux is not None:
            if aux.__get_datos__().__get_area_investigacion__().lower() == area.lowe():
                cant += 1
                aux = aux.__get_siguiente__()
        if cant > 0 :
            print(f"Total investigadores que trabajan en el area ingresada >> {cant}")
    def listado_persona(self):
        aux = self.__comienzo
        while aux is not None:
            print(f"Tipo de agente >> {aux.__get_datos__().__get_cargo__()}")
            print(f"Nombre >> {aux.__get_datos__().__get_apellido_nombre__()}")
            print(f"Sueldo >> {aux.__get_datos__().__get_sueldo__()}")
            aux = aux.__get_siguiente__()
    def listado_investigadores(self, categoria):
        aux = self.__comienzo
        total = 0.0
        while aux is not None:
            if categoria == str(aux.__get_datos__().__get_categoria__()):
                total += aux.__get_datos__().__get_importe__()
                print(f"Nombre >> {aux.__get_datos__().__get_apellido_nombre__()}")
                print(f"Importe extra >> {aux.__get_datos__().__get_importe__()}")
                print(f"Importe total >> {total}")
    def cartel(self):
        print("< Archivo json registrado satisfactoriamente >")
