from Node import Node
from Vertice import Vertice


class Cola:
    def __init__(self):
        self.cabeza = None

    def encolar(self, valor)->None:
        new_node:Node = Node(valor)
        if self.esta_vacia():
            self.cabeza = new_node
            return
        aux: Node = self.cabeza
        while aux.siguiente is not None:
            aux = aux.siguiente
        aux.siguiente = new_node

    def desencolar(self)->Node:
        if self.esta_vacia():
            print("No hay nada en la Cola.")
            return
        aux: Node = self.cabeza
        self.cabeza = aux.siguiente
        return aux

    def ordenar(self):
        if self.esta_vacia():
            print("No hay nada en la Cola que se pueda ordenar.")
            return
        current: Node[Vertice] = self.cabeza
        while current is not None:
            next:Node[Vertice] = current.siguiente
            while next is not None:
                if current.valor.peso_acumulado > next.valor.peso_acumulado:
                    aux: Vertice = next.valor
                    next.valor = current.valor
                    current.valor = aux
                next = next.siguiente
            current = current.siguiente

    def buscar(self, valor)->Node:
        aux: Node[Vertice] = self.cabeza
        while aux is not None:
            if aux.valor.valor == valor:
                return aux
            aux = aux.siguiente
        return None

    def esta_vacia(self)->bool:
        return self.cabeza is None



# from Lista import Lista
# from Node import Node
#
#
# class Cola(Lista):
#     def __init__(self):
#         super().__init__()
#
#     def encolar(self, valor):
#         Lista.insertar_final(self,valor)
#
#     def desencolar(self) -> Node:
#         return Lista.eliminar_frente(self)
#
