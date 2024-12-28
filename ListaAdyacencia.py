from Lista import Lista
from Node import Node
from Ruta import Ruta
from Vertice import Vertice


class ListaAdyacencia:
    def __init__(self):
        self.vertices: Lista = Lista()

    def insertar(self, ruta: Ruta):

        origen:Vertice = Vertice(ruta.get_origen())
        destino:Vertice = Vertice(ruta.get_destino(), ruta.get_tiempo())

        resultado = self.vertices.buscar(origen)

        if resultado is not None:
            resultado.valor.vecinos.insertar_final(destino)
        else:
            resultado = self.vertices.insertar_final(origen)
            resultado.valor.vecinos.insertar_final(destino)

    def imprimir(self)->str:
        dot = 'digraph G {\n\tbgcolor="#1a1a1a"\n\tedge [arrowhead=none fontcolor=white color="#ff5400"];\n\t'
        dot += 'node [shape=circle fixedsize=shape width=0.5 fontsize=7 style=filled fillcolor="#313638" fontcolor=white\n\t'
        dot += 'color=transparent];\n\t'
        aux:Node[Vertice] = self.vertices.cabeza
        while aux is not None:
            if aux is not None:
                dot += str(aux.valor)
            aux = aux.sig
        dot += "}"
        return dot