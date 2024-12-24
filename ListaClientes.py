from Cliente import Cliente
from NodeCliente import NodeCliente


class ListaClientes:
    def __init__(self):
        self.__primero = None
        self.__ultimo = None

    def get_primero(self):
        return self.__primero

    def set_primero(self, primero):
        self.__primero = primero

    def get_ultimo(self):
        return self.__ultimo

    def set_ultimo(self, ultimo):
        self.__ultimo = ultimo

    def esta_vacia(self) -> bool:
        return self.__primero is None and self.__ultimo is None

    def insertar_inicio(self, cliente):  # Crear el nuevo nodo cliente
        new_node_cliente = NodeCliente(
            cliente.get_dpi(),
            cliente.get_nombres(),
            cliente.get_apellidos(),
            cliente.get_genero(),
            cliente.get_telefono(),
            cliente.get_direccion()
        )
        if self.esta_vacia():
            # Primera inserción, el nodo apunta a sí mismo
            new_node_cliente.set_siguiente(new_node_cliente)
            new_node_cliente.set_anterior(new_node_cliente)
            self.__primero = self.__ultimo = new_node_cliente
        else:
            # Conectamos el nuevo nodo al inicio y al final
            new_node_cliente.set_siguiente(self.__primero)
            new_node_cliente.set_anterior(self.__ultimo)
            self.__primero.set_anterior(new_node_cliente)
            self.__ultimo.set_siguiente(new_node_cliente)
            self.__primero = new_node_cliente

    def imprimir(self):
        if self.esta_vacia():
            print("La lista está vacía.")
            return
        actual = self.__primero
        elementos = []
        while True:
            cliente = actual.get_cliente()
            elementos.append(f'[{cliente.get_dpi()} - {cliente.get_nombres()}]')
            actual = actual.get_siguiente()
            if actual == self.__primero:  # Se ha completado un ciclo
                break

        print(" --> ".join(elementos))

    def buscar_node_cliente(self, dpi_cliente):
        if self.esta_vacia():
            print("La lista esta vacia.")
        else:
            node_cliente: Cliente
            actual = self.__primero
            while True:
                node_cliente = actual.get_cliente()
                if node_cliente.get_dpi() == dpi_cliente:
                    print("se encontro el cliente", node_cliente.get_dpi())
                    return actual
                actual = actual.get_siguiente()
                if actual == self.__primero:
                    break
            return None

    def modificar_node_cliente(self, dpi_cliente, new_dpi, new_nombres, new_apellidos, new_genero, new_telefono,
                               new_direccion):
        node_cliente: NodeCliente = self.buscar_node_cliente(dpi_cliente)
        if node_cliente is None:
            print("No se encontro el cliente", dpi_cliente)
            return False
        else:
            node_cliente.get_cliente().set_dpi(new_dpi)
            node_cliente.get_cliente().set_nombres(new_nombres)
            node_cliente.get_cliente().set_apellidos(new_apellidos)
            node_cliente.get_cliente().set_genero(new_genero)
            node_cliente.get_cliente().set_telefono(new_telefono)
            node_cliente.get_cliente().set_direccion(new_direccion)
            return True

    def eliminar_inicio(self):
        if self.esta_vacia():
            print("La lista esta vacia, no se puede eliminar")
        elif self.__primero == self.__ultimo:
            self.__primero = None
            self.__ultimo = None
        else:
            temp: NodeCliente = self.__primero.get_siguiente()
            self.__ultimo.set_siguiente(temp)
            temp.set_anterior(self.__ultimo)
            self.__primero = temp

    def eliminar_final(self):
        pass

    def eliminar_node_cliente(self):

        pass

    def generar_reporte(self):
        pass
