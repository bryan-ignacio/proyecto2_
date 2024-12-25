class Vehiculo:
    def __init__(self, placa, marca, modelo, precio):
        self.__placa = placa
        self.__marca = marca
        self.__modelo = modelo
        self.__precio = precio

    def get_placa(self):
        return self.__placa

    def set_placa(self, placa):
        self.__placa = placa

    def get_marca(self):
        return self.__marca

    def set_marca(self, marca):
        self.__marca = marca

    def get_modelo(self):
        return self.__modelo

    def set_modelo(self, modelo):
        self.__modelo = modelo

    def get_precio(self):
        return self.__precio

    def set_precio(self, precio):
        self.__precio = precio

    def __str__(self):
        return f'Vehiculo->[placa:{self.__placa}, marca: {self.__marca}, precio: {self.__precio}]'
