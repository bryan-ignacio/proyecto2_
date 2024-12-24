from Cliente import Cliente


class NodeCliente:
    # declarar un puntero que es un tipo de dato que almacena la dirección de memoria de otra variable
    def __init__(self, dpi, nombres, apellidos, genero, telefono, direccion):
        self.__cliente = Cliente(dpi, nombres, apellidos, genero, telefono, direccion)
        self.__anterior = None
        self.__siguiente = None

    def get_cliente(self):
        return self.__cliente

    def set_cliente(self, dpi, nombres, apellidos, genero, telefono, direccion):
        self.__cliente.set_dpi(dpi)
        self.__cliente.set_nombres(nombres)
        self.__cliente.set_apellidos(apellidos)
        self.__cliente.set_genero(genero)
        self.__cliente.set_telefono(telefono)
        self.__cliente.set_direccion(direccion)

    def get_anterior(self):
        return self.__anterior

    def set_anterior(self, anterior):
        self.__anterior = anterior

    def get_siguiente(self):
        return self.__siguiente

    def set_siguiente(self, siguiente):
        self.__siguiente = siguiente

    def __str__(self):
        return f'Node[ {self.__cliente} ]'
