from Cola import Cola
from Lista import Lista
from Node import Node
from Ruta import Ruta
from Vertice import Vertice
import os
import subprocess


class ListaAdyacencia:
    def __init__(self):
        self.vertices: Lista = Lista()
        self.ruta_corta: Lista[Vertice] = Lista()

    def insertar(self, ruta: Ruta):

        origen:Vertice = Vertice(ruta.get_origen())
        destino:Vertice = Vertice(ruta.get_destino(), ruta.get_tiempo())

        resultado = self.vertices.buscar(origen)

        if resultado is not None:
            resultado.valor.vecinos.insertar_final(destino)
        else:
            resultado = self.vertices.insertar_final(origen)
            resultado.valor.vecinos.insertar_final(destino)

    def obtener_ruta_corta(self, origen: str, destino: str):
        cola_ruta: Cola = Cola()
        nodo_origen:Node[Vertice] = self.vertices.buscar(Vertice(origen))
        cola_ruta.encolar(nodo_origen.valor)
        self.obtener_ruta_corta_recursiva(Vertice(destino), cola_ruta)


    def obtener_ruta_corta_recursiva(self, destino: Vertice, cola_ruta: Cola):
        nodo_origen: Node[Vertice] = cola_ruta.desencolar()
        if nodo_origen is None:
            print("La Ciudad de Origen no Existe.")
            return

        nodo_origen = self.vertices.buscar(nodo_origen.valor)

        self.ruta_corta.insertar_final(nodo_origen)
        nodo_origen.valor.visitado = True
        if nodo_origen.valor.valor == destino.valor:
            #Ya encontramos el ultimo nodo.
            return

        cabeza_vecinos: Node[Vertice] = nodo_origen.valor.vecinos.cabeza

        while cabeza_vecinos is not None:

            nodo_vecino: Node[Vertice] = self.vertices.buscar(cabeza_vecinos.valor)

            if not nodo_vecino.valor.visitado:
                nodo_vecino.valor.get_peso_acumulado(cabeza_vecinos.valor.peso)
                cola_ruta.encolar(nodo_vecino.valor)
            cabeza_vecinos = cabeza_vecinos.sig
        self.ordenar(cola_ruta)
        self.obtener_ruta_corta_recursiva(destino, cola_ruta)


    def ordenar(self, cola:Cola):
        inicio: Node = cola.cabeza
        aux: Vertice
        while inicio is not None:
            inicio_sig = inicio.sig
            while inicio_sig is not None:
                if inicio.valor.get_peso_acumulado() > inicio_sig.valor.get_peso_acumulado():
                    aux = inicio_sig.valor
                    inicio_sig.valor = inicio.valor
                    inicio.valor = aux.valor
                inicio_sig = inicio_sig.sig
            inicio = inicio.sig


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