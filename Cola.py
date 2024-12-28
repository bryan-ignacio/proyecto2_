from Lista import Lista
from Node import Node


class Cola(Lista):
    def __init__(self):
        super().__init__()

    def encolar(self, valor):
        Lista.insertar_final(self,valor)

    def desencolar(self) -> Node:
        return Lista.eliminar_frente(self)

