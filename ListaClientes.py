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
        pass

    def insertar_inicio(self):
        pass

    def imprimir(self):
        pass

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
