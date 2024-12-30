from Viaje import Viaje


class NodeViaje:
    def __init__(self,id, origen, destino, cliente, vehiculo):
        self.__viaje: Viaje = Viaje(id,origen, destino, cliente, vehiculo)
        self.siguiente = None

    def get_viaje(self):
        return self.__viaje

    def set_viaje(self, origen, destino, cliente, vehiculo):
        self.__viaje.set_origen(origen)
        self.__viaje.set_destino(destino)
        self.__viaje.set_cliente(cliente)
        self.__viaje.set_vehiculo(vehiculo)

    def datos_viaje(self):
        return f'Viaje->[id:{self.__viaje.get_id()}, origen: {self.__viaje.get_origen()}. destino: {self.__viaje.get_destino()}]'
