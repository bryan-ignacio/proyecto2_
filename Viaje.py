class Viaje:

    contador_viajes = 0

    def __init__(self, origen, destino, fecha, cliente, vehiculo, ruta_tomada):
        Viaje.contador_viajes += 1
        self.__id = Viaje.contador_viajes
        self.__origen = origen
        self.__destino = destino
        self.__fecha = fecha
        self.__cliente = cliente
        self.__vehiculo = vehiculo
        self.__ruta_tomada = ruta_tomada

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

    def get_fecha(self):
        return self.__fecha

    def set_fecha(self, fecha):
        self.__fecha = fecha

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
        return (f'Viaje->[id: {self.__id}, origen: {self.__origen}, destino: {self.__destino}, fecha: {self.__fecha}\n'
                f', cliente: {self.__cliente} vehiculo: {self.__vehiculo}, camino: {self.__ruta_tomada}]')
