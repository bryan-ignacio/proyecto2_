from Cliente import Cliente


class NodeCliente:
    # declarar un puntero que es un tipo de dato que almacena la dirección de memoria de otra variable
    def __init__(self,dpi, nombres, apellidos, genero, telefono, direccion ):
        self.cliente = Cliente(dpi, nombres, apellidos, genero, telefono, direccion)
        self.anterior = None
        self.siguiente =None

    def get_cliente(self):
        return self.cliente

    def set_cliente(self,dpi, nombres, apellidos, genero, telefono, direccion):
        self.cliente.set_dpi(dpi)
        self.cliente.set_nombres(nombres)
        self.cliente.set_apellidos(apellidos)
        self.cliente.set_genero(genero)
        self.cliente.set_telefono(telefono)
        self.cliente.set_direccion(direccion)

    