from Viaje import Viaje


class NodeViaje:
    def __init__(self, origen, destino, fecha, cliente, vehiculo, ruta_tomada):
        self.__viaje: Viaje = Viaje(origen, destino, fecha, cliente, vehiculo, ruta_tomada)
        self.__siguiente = None

    def get_viaje(self):
        return self.__viaje

    def set_viaje(self, origen, destino, fecha, cliente, vehiculo, ruta_tomada):
        self.__viaje.set_origen(origen)
        self.__viaje.set_destino(destino)
        self.__viaje.set_fecha(fecha)
        self.__viaje.set_cliente(cliente)
        self.__viaje.set_vehiculo(vehiculo)
        self.__viaje.set_ruta_tomada(ruta_tomada)

    def get_siguiente(self):
        return self.__siguiente

    def set_siguiente(self, siguiente):
        self.__siguiente = siguiente

    def datos_viaje(self):
        return f'Viaje->[lugar:{self.__viaje} , tiempo: ]'

