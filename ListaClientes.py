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


    def buscar_node_cliente(self):
        pass

    def eliminar_inicio(self):
        pass

    def eliminar_final(self):
        pass

    def eliminar_node_cliente(self):
        pass

    def generar_reporte(self):
        pass
