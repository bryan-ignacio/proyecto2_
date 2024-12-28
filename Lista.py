from Node import Node


class Lista:
    def __init__(self):
        self.cabeza: Node = None

    def insertar_final(self, valor) -> Node:
        aux: Node = self.cabeza

        if aux is None:
            aux = Node(valor)
            self.cabeza = aux
            return self.cabeza

        while aux.sig is not None:
            aux = aux.sig
        aux.sig = Node(valor)

        return aux.sig

    def buscar(self, valor) -> Node:
        aux: Node = self.cabeza
        if aux is None:
            return None
        while aux is not None:
            if aux.valor.valor == valor.valor:
                return aux
            aux = aux.sig
        return None
