class Viaje:
    def __init__(self, origen, destino, fecha, vehiculo, camino):
        self.__origen = origen
        self.__destino = destino
        self.__fecha = fecha
        self.__vehiculo = vehiculo
        self.__camino = camino

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

    def get_vehiculo(self):
        return self.__vehiculo

    def set_vehiculo(self, vehiculo):
        self.__vehiculo = vehiculo

    def get_camino(self):
        return self.__camino

    def set_camino(self, camino):
        self.__camino = camino

    def __str__(self):
        return (f'Viaje->[origen: {self.__origen}, destino: {self.__destino}, \n'
                f'fecha: {self.__fecha}, vehiculo: {self.__vehiculo}, camino: {self.__camino}]')

