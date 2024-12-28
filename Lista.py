from Node import Node


class Lista:
    def __init__(self):
        self.cabeza: Node = None
        self.size: int = 0

    def insertar_final(self, valor) -> Node:
        aux: Node = self.cabeza

        if aux is None:
            aux = Node(valor)
            self.cabeza = aux
            return self.cabeza

        while aux.sig is not None:
            aux = aux.sig
        aux.sig = Node(valor)

        self.size += 1
        return aux.sig

    def insertar_frente(self, valor) -> Node:
        nuevo_nodo: Node = Node(valor)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return self.cabeza
        nuevo_nodo.sig = self.cabeza
        self.cabeza = nuevo_nodo
        self.size += 1
        return self.cabeza

    def buscar(self, valor) -> Node:
        aux: Node = self.cabeza
        if aux is None:
            return None
        while aux is not None:
            if aux.valor.valor == valor.valor:
                return aux
            aux = aux.sig
        return None

    def eliminar_frente(self):
        cabeza: Node = self.cabeza
        if cabeza is not None:
            self.cabeza = cabeza.sig
            return self.cabeza
