from NodeVehiculo import NodeVehiculo
from Vehiculo import Vehiculo
import os
import subprocess

class ArbolBVehiculos:
    def __init__(self, orden: int):
        self.raiz: NodeVehiculo = NodeVehiculo(True)
        self.orden: int = orden

    def insertar_valor(self, vehiculo: Vehiculo):
        raiz: NodeVehiculo = self.raiz
        self.insertar_valor_no_completo(raiz, vehiculo)
        if len(raiz.claves) > self.orden - 1:
            nodo: NodeVehiculo = NodeVehiculo()
            self.raiz = nodo
            nodo.hijos.insert(0, raiz)
            self.dividir_pagina(nodo, 0)

    def insertar_valor_no_completo(self, raiz: NodeVehiculo, vehiculo: Vehiculo):
        posicion: int = len(raiz.claves) - 1
        if raiz.hoja:
            raiz.claves.append(None)
            # comparar el valor.placa
            while posicion >= 0 and vehiculo.get_placa() < raiz.claves[posicion].get_placa():
                raiz.claves[posicion + 1] = raiz.claves[posicion]
                posicion -= 1
            raiz.claves[posicion + 1] = vehiculo  # [4,5,6]
        else:
            while posicion >= 0 and vehiculo.get_placa() < raiz.claves[posicion].get_placa():
                posicion -= 1
            posicion += 1
            self.insertar_valor_no_completo(raiz.hijos[posicion], vehiculo)
            if len(raiz.hijos[posicion].claves) > self.orden - 1:
                self.dividir_pagina(raiz, posicion)

    def dividir_pagina(self, raiz: NodeVehiculo, posicion: int):
        posicion_media: int = int((self.orden - 1) / 2)

        hijo: NodeVehiculo = raiz.hijos[posicion]
        nodo: NodeVehiculo = NodeVehiculo(hijo.hoja)

        raiz.hijos.insert(posicion + 1, nodo)

        raiz.claves.insert(posicion, hijo.claves[posicion_media])

        nodo.claves = hijo.claves[posicion_media + 1: posicion_media * 2 + 1]
        hijo.claves = hijo.claves[0:posicion_media]
        if not hijo.hoja:
            nodo.hijos = hijo.hijos[posicion_media + 1: posicion_media * 2 + 2]
            hijo.hijos = hijo.hijos[0:posicion_media + 1]

    def imprimir_usuario(self) -> str:
        dot: str = "digraph G {\n\tbgcolor=\"#1A1A1A\";\n\t"
        dot += "fontcolor=white;\n\tnodesep=0.5;\n\tsplines=false\n\t"
        dot += "node [shape=record width=1.2 style=filled fillcolor=\"#313638\""
        dot += "fontcolor=white color=transparent];\n\t"
        dot += "edge [fontcolor=white color=\"#0070C9\"];\n\t"
        dot += self.imprimir(self.raiz)
        dot += "\n}"
        return dot

    def imprimir(self, nodo: NodeVehiculo, id: list[int] = [0]) -> str:
        raiz: NodeVehiculo = nodo
        arbol = f"n{id[0]}[label=\""
        contador: int = 0
        for item in raiz.claves:
            if contador == len(raiz.claves) - 1:
                arbol += f"<f{contador}>|{item}|<f{contador + 1}>"
                break
            arbol += f"<f{contador}>|{item}|"
            contador += 1
        arbol += "\"];\n\t"
        contador: int = 0
        id_padre = id[0]
        for item in raiz.hijos:
            arbol += f"n{id_padre}:f{contador} -> n{id[0] + 1};\n\t"
            id[0] += 1
            arbol += self.imprimir(item, id)
            contador += 1
        return arbol

    def __str__(self):
        return f'{self.raiz}'

    def generar_reporte(self):
        # Paso 1: Generar el contenido DOT
        dot_content = self.imprimir_usuario()
        # Paso 2: Guardar el contenido DOT en un archivo
        dot_file = "arbol_b.dot"
        with open(dot_file, "w", encoding="utf-8") as file:
            file.write(dot_content)

        # Paso 3: Generar la imagen usando Graphviz
        image_file = "arbol_b.png"
        try:
            subprocess.run(["dot", "-Tpng", dot_file, "-o", image_file], check=True)
            print(f"Imagen del árbol B generada: {image_file}")
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

