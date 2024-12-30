from Cola import Cola
from Lista import Lista
from Node import Node
from NodeLL import NodeLL
from Ruta import Ruta
from Vertice import Vertice
from copy import copy
import os
import subprocess

class ListaAdyacencia:
    def __init__(self):
        self.vertices:Lista[Vertice] = Lista()

    def insertar(self, ruta: Ruta):
        vertice: Vertice = self.buscar_vertice(ruta.get_origen())
        if vertice is not None:
            vertice.agregar_vecinos(ruta.get_destino(), ruta.get_tiempo())
            return
        vertice = Vertice(ruta.get_origen())
        vertice.agregar_vecinos(ruta.get_destino(), ruta.get_tiempo())
        self.vertices.insertar_frente(vertice)

    def buscar_vertice(self, valor: str)->Vertice:
        aux:NodeLL[Vertice] = self.vertices.cabeza
        while aux is not None:
            if aux.valor.valor == valor:
                return aux.valor
            aux = aux.siguiente
        return None

    def get_ruta(self, origen: str, destino: str)->Lista:
        ruta:Lista[Vertice] = Lista()
        nodos_visitados: Cola = Cola()
        nodos: Cola = Cola()
        origen:Vertice = copy(self.buscar_vertice(origen))
        if origen is None:
            print(f"La Ciudad: {origen} no existe.")
            return
        nodos.encolar(origen)

        resultado: Vertice = self.get_ruta_corta(destino, nodos_visitados, nodos)
        while resultado is not None:
            ruta.insertar_frente(resultado)
            resultado = resultado.padre
        return ruta

    def get_ruta_corta(self, destino: str, nodos_visitados: Cola, nodos: Cola)->Vertice:
        origen: Vertice = nodos.desencolar().valor
        if origen.valor == destino:
            nodos_visitados.encolar(origen)
            return origen
        aux: Node[Vertice] = origen.vecinos.cabeza
        while aux is not None:
            if not self.esta_visitado(nodos_visitados, aux.valor):
                peso:int = aux.valor.peso
                vecino: Vertice = copy(self.buscar_vertice(aux.valor.valor))
                vecino.peso = peso
                vecino.set_peso_acumulado(origen.peso_acumulado + peso)
                vecino.padre = origen
                nodos.encolar(vecino)
            aux = aux.siguiente
        nodos.ordenar()
        nodos_visitados.encolar(origen)
        return self.get_ruta_corta(destino, nodos_visitados, nodos)

    def esta_visitado(self, nodos_visitados: Cola, valor: Vertice)->bool:
        resultado: Node = nodos_visitados.buscar(valor.valor)
        return resultado is not None

    def generar_reporte(self):
        # Paso 1: Generar el contenido DOT
        dot_content = self.imprimir()
        # Paso 2: Guardar el contenido DOT en un archivo
        dot_file = "lista_adyacencia.dot"
        with open(dot_file, "w", encoding="utf-8") as file:
            file.write(dot_content)

        # Paso 3: Generar la imagen usando Graphviz
        image_file = "lista_adyacencia.svg"
        try:
            subprocess.run(["neato", "-Tsvg", dot_file, "-o", image_file], check=True)
            # print(f"Imagen del árbol B generada: {image_file}")
        except FileNotFoundError:
            print("Error: Asegúrate de tener Graphviz instalado y que el comando 'dot' esté disponible en tu sistema.")
            return

        # Paso 4: Abrir automáticamente la imagen generada
        try:
            if os.name == "nt":  # Windows
                os.startfile(image_file)
            elif os.name == "posix":
                subprocess.run(["open" if os.uname().sysname == "Darwin" else "xdg-open", image_file])
        except Exception as e:
            print(f"No se pudo abrir automáticamente la imagen: {e}")

    def imprimir(self)->str:
        dot = 'digraph G {\n\tbgcolor="#1a1a1a"\n\tedge [arrowhead=none fontcolor=white color="#ff5400"];\n\t'
        dot += 'node [shape=circle fixedsize=shape width=0.5 fontsize=7 style=filled fillcolor="#313638" fontcolor=white\n\t'
        dot += 'color=transparent];\n\t'
        aux:Node[Vertice] = self.vertices.cabeza
        while aux is not None:
            if aux is not None:
                dot += str(aux.valor)
            aux = aux.siguiente
        dot += "}"
        return dot
