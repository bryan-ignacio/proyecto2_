from Lista import Lista
from Node import Node
from Ruta import Ruta
from Vertice import Vertice
import os
import subprocess


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
            elif os.name == "posix":  # macOS o Linux
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
            aux = aux.sig
        dot += "}"
        return dot