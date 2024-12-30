from Cliente import Cliente
from Lista import Lista
from ListaAdyacencia import ListaAdyacencia
from NodeLL import NodeLL
from Vehiculo import Vehiculo
from Vertice import Vertice


class Viaje:
    def __init__(self, id: int, origen: str, destino: str, cliente: Cliente, vehiculo: Vehiculo):
        self.id: int = id
        self.origen: str = origen
        self.destino: str = destino
        self.cliente: Cliente = cliente
        self.vehiculo: Vehiculo = vehiculo
        self.ruta: Lista = None

    def get_ruta(self, grafo: ListaAdyacencia):
        self.ruta = grafo.get_ruta(self.origen, self.destino)

    def mostrar_ruta(self) -> str:
        ruta: str = ""
        aux: NodeLL[Vertice] = self.ruta.cabeza
        while aux is not None:
            if aux.valor.peso_acumulado == 0:
                ruta += f"{aux.valor.valor}({aux.valor.peso_acumulado}) -> "
            else:
                ruta += f"{aux.valor.valor}({peso} + {aux.valor.peso} = {aux.valor.peso_acumulado}) -> "
            peso: int = aux.valor.peso_acumulado
            aux = aux.siguiente
        return ruta



    # def __str__(self):
    #     return (f'Viaje->[id: {self.id}, origen: {self.origen}, destino: {self.destino}\n'
    #             f', cliente: {self.cliente} vehiculo: {self.vehiculo}, camino: {self.ruta}]')

