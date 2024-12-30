from Cliente import Cliente
from Lista import Lista
from ListaAdyacencia import ListaAdyacencia
from NodeLL import NodeLL
from Vehiculo import Vehiculo
from Vertice import Vertice


class Viaje:
    def __init__(self, id: int, origen: str, destino: str, cliente: Cliente, vehiculo: Vehiculo):
        self.__id: int = id
        self.__origen: str = origen
        self.__destino: str = destino
        self.__cliente: Cliente = cliente
        self.__vehiculo: Vehiculo = vehiculo
        self.__ruta: Lista = Lista()

    def get_ruta(self, grafo: ListaAdyacencia):
        self.__ruta = grafo.get_ruta(self.__origen, self.__destino)

    def mostrar_ruta(self) -> str:
        ruta: str = ""
        aux: NodeLL[Vertice] = self.__ruta.cabeza
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


    def __str__(self):
        return (f'Viaje->[id: {self.__id}, origen: {self.__origen}, destino: {self.__destino}\n'
                f', cliente: {self.__cliente} vehiculo: {self.__vehiculo}, camino: {self.__ruta}]')

