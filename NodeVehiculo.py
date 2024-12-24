from Vehiculo import Vehiculo


class NodeVehiculo:
    def __init__(self, hoja:bool = False):
        self.hoja:bool = hoja
        self.claves:list[Vehiculo] = []
        self.hijos: list[NodeVehiculo] = []

    def __str__(self):
        return f'Hoja: {self.hoja} - Claves: {self.claves} - Hijos: {self.hijos}'
