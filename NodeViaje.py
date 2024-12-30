from Viaje import Viaje


class NodeViaje:
    def __init__(self,id, origen, destino, cliente, vehiculo):
        self.__viaje: Viaje = Viaje(id,origen, destino, cliente, vehiculo)
        self.siguiente = None

    def get_viaje(self):
        return self.__viaje


    def datos_viaje(self):
        return f'Viaje->[id:{self.__viaje.id}, origen: {self.__viaje.origen}. destino: {self.__viaje.destino}]'
