from Cliente import Cliente
from Lista import Lista
from ListaAdyacencia import ListaAdyacencia
from NodeLL import NodeLL
from Vehiculo import Vehiculo
from Vertice import Vertice

class Viaje:
    contador_viajes = 0
    def __init__(self, origen:str, destino:str, cliente: Cliente, vehiculo: Vehiculo):
            Viaje.contador_viajes += 1
            self.__id = Viaje.contador_viajes
            self.__origen:str = origen
            self.__destino:str = destino
            self.__cliente:Cliente = cliente
            self.__vehiculo:Vehiculo = vehiculo
            self.__ruta_tomada:Lista = None

    def get_ruta(self, grafo: ListaAdyacencia):
        self.__ruta_tomada = grafo.get_ruta(self.__origen, self.__destino)

    def mostrar_ruta(self)->str:
        ruta: str = ""
        aux:NodeLL[Vertice] = self.__ruta_tomada.cabeza
        while aux is not None:
            if aux.valor.peso_acumulado == 0:
                ruta += f"{aux.valor.valor}({aux.valor.peso_acumulado}) -> "
            else:
                ruta += f"{aux.valor.valor}({peso} + {aux.valor.peso} = {aux.valor.peso_acumulado}) -> "
            peso: int = aux.valor.peso_acumulado
            aux = aux.siguiente
        return ruta

    def get_id(self):
        return self.__id

    def get_origen(self):
        return self.__origen

    def set_origen(self, origen):
        self.__origen = origen

    def get_destino(self):
        return self.__destino

    def set_destino(self, destino):
        self.__destino = destino

    def get_cliente(self):
        return self.__cliente

    def set_cliente(self, cliente):
        self.__cliente = cliente

    def get_vehiculo(self):
        return self.__vehiculo

    def set_vehiculo(self, vehiculo):
        self.__vehiculo = vehiculo

    def get_ruta_tomada(self):
        return self.__ruta_tomada

    def set_ruta_tomada(self, ruta_tomada):
        self.__ruta_tomada = ruta_tomada

    def __str__(self):
        return (f'Viaje->[id: {self.__id}, origen: {self.__origen}, destino: {self.__destino}\n'
                f', cliente: {self.__cliente} vehiculo: {self.__vehiculo}, camino: {self.__ruta_tomada}]')


# class Viaje:
#
#     contador_viajes = 0
#
#     def __init__(self, origen, destino, fecha, cliente, vehiculo, ruta_tomada):
#         Viaje.contador_viajes += 1
#         self.__id = Viaje.contador_viajes
#         self.__origen = origen
#         self.__destino = destino
#         self.__fecha = fecha
#         self.__cliente = cliente
#         self.__vehiculo = vehiculo
#         self.__ruta_tomada = ruta_tomada
#
#     def get_id(self):
#         return self.__id
#
#     def get_origen(self):
#         return self.__origen
#
#     def set_origen(self, origen):
#         self.__origen = origen
#
#     def get_destino(self):
#         return self.__destino
#
#     def set_destino(self, destino):
#         self.__destino = destino
#
#     def get_fecha(self):
#         return self.__fecha
#
#     def set_fecha(self, fecha):
#         self.__fecha = fecha
#
#     def get_cliente(self):
#         return self.__cliente
#
#     def set_cliente(self, cliente):
#         self.__cliente = cliente
#
#     def get_vehiculo(self):
#         return self.__vehiculo
#
#     def set_vehiculo(self, vehiculo):
#         self.__vehiculo = vehiculo
#
#     def get_ruta_tomada(self):
#         return self.__ruta_tomada
#
#     def set_ruta_tomada(self, ruta_tomada):
#         self.__ruta_tomada = ruta_tomada
#
#     def __str__(self):
#         return (f'Viaje->[id: {self.__id}, origen: {self.__origen}, destino: {self.__destino}, fecha: {self.__fecha}\n'
#                 f', cliente: {self.__cliente} vehiculo: {self.__vehiculo}, camino: {self.__ruta_tomada}]')
