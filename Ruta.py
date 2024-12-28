class Ruta:
    def __init__(self, origen: str, destino: str, tiempo : int):
        self.__origen:str = origen
        self.__destino:str = destino
        self.__tiempo:int = tiempo

    def get_origen(self):
        return self.__origen

    def set_origen(self, origen):
        self.__origen = origen

    def get_destino(self):
        return self.__destino

    def set_destino(self, destino):
        self.__destino = destino

    def get_tiempo(self):
        return self.__tiempo

    def set_tiempo(self, tiempo):
        self.__tiempo = tiempo

    def __str__(self):
        return f'Ruta->[origen: {self.__origen}, destino: {self.__destino}, tiempo:{self.__tiempo}]'
