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

    def buscar(self, placa: str, nodo: NodeVehiculo = None):
        if nodo is None:
            nodo = self.raiz
        # Buscar la placa en las claves del nodo actual
        for vehiculo in nodo.claves:
            if vehiculo.get_placa() == placa:
                return vehiculo
        # Si no es una hoja, continuar buscando en los hijos correspondientes
        if not nodo.hoja:
            for i, vehiculo in enumerate(nodo.claves):
                if placa < vehiculo.get_placa():
                    return self.buscar(placa, nodo.hijos[i])
            return self.buscar(placa, nodo.hijos[-1])
        # Si llegamos aquí y no encontramos la placa
        return None

    def modificar(self, placa: str, new_placa: str, new_marca: str, new_modelo: str, new_precio: str):
        vehiculo = self.buscar(placa)
        if vehiculo is not None:
            vehiculo.set_placa(new_placa)
            vehiculo.set_marca(new_marca)
            vehiculo.set_modelo(new_modelo)
            vehiculo.set_precio(new_precio)
        else:
            print(f"No se encontró un vehículo con la placa '{placa}'.")

    def eliminar(self, placa: str):
        self.eliminar_recursivo(self.raiz, placa)
        # Si la raíz queda vacía y tiene hijos, cambiar la raíz
        if len(self.raiz.claves) == 0 and not self.raiz.hoja:
            self.raiz = self.raiz.hijos[0]

    def eliminar_recursivo(self, nodo: NodeVehiculo, placa: str):
        posicion = 0
        # Buscar la clave en el nodo actual
        while posicion < len(nodo.claves) and placa > nodo.claves[posicion].get_placa():
            posicion += 1

        # Caso 1: La clave está en este nodo
        if posicion < len(nodo.claves) and nodo.claves[posicion].get_placa() == placa:
            if nodo.hoja:
                # Caso 1.1: Eliminar directamente si es un nodo hoja
                nodo.claves.pop(posicion)
            else:
                # Caso 1.2: Eliminar de un nodo interno
                self.eliminar_clave_interna(nodo, posicion)
        else:
            # Caso 2: La clave no está en este nodo
            if nodo.hoja:
                # Si es hoja, no está en el árbol
                print(f"No se encontró el vehículo con la placa '{placa}'.")
                return

            # Verificar si el hijo tiene suficientes claves para descender
            if len(nodo.hijos[posicion].claves) < (self.orden // 2):
                self.reestructurar(nodo, posicion)

            # Intentar eliminar en el hijo apropiado
            self.eliminar_recursivo(nodo.hijos[posicion], placa)

    def eliminar_clave_interna(self, nodo: NodeVehiculo, posicion: int):
        # Obtener los hijos izquierdo y derecho
        hijo_izquierdo = nodo.hijos[posicion]
        hijo_derecho = nodo.hijos[posicion + 1]

        if len(hijo_izquierdo.claves) >= (self.orden // 2):
            # Caso 2.1: Reemplazar con el predecesor
            predecesor = self.obtener_maximo(hijo_izquierdo)
            nodo.claves[posicion] = predecesor
            self.eliminar_recursivo(hijo_izquierdo, predecesor.get_placa())
        elif len(hijo_derecho.claves) >= (self.orden // 2):
            # Caso 2.2: Reemplazar con el sucesor
            sucesor = self.obtener_minimo(hijo_derecho)
            nodo.claves[posicion] = sucesor
            self.eliminar_recursivo(hijo_derecho, sucesor.get_placa())
        else:
            # Caso 2.3: Fusionar hijos y eliminar la clave
            self.fusionar(nodo, posicion)
            self.eliminar_recursivo(hijo_izquierdo, nodo.claves[posicion].get_placa())

    def reestructurar(self, nodo: NodeVehiculo, posicion: int):
        hijo = nodo.hijos[posicion]
        if posicion > 0 and len(nodo.hijos[posicion - 1].claves) >= (self.orden // 2):
            # Caso 3.1: Tomar prestado del hermano izquierdo
            hermano = nodo.hijos[posicion - 1]
            hijo.claves.insert(0, nodo.claves[posicion - 1])
            nodo.claves[posicion - 1] = hermano.claves.pop(-1)
            if not hijo.hoja:
                hijo.hijos.insert(0, hermano.hijos.pop(-1))
        elif posicion < len(nodo.hijos) - 1 and len(nodo.hijos[posicion + 1].claves) >= (self.orden // 2):
            # Caso 3.2: Tomar prestado del hermano derecho
            hermano = nodo.hijos[posicion + 1]
            hijo.claves.append(nodo.claves[posicion])
            nodo.claves[posicion] = hermano.claves.pop(0)
            if not hijo.hoja:
                hijo.hijos.append(hermano.hijos.pop(0))
        else:
            # Caso 3.3: Fusionar con un hermano
            if posicion < len(nodo.hijos) - 1:
                self.fusionar(nodo, posicion)
            else:
                self.fusionar(nodo, posicion - 1)

    def fusionar(self, nodo: NodeVehiculo, posicion: int):
        hijo_izquierdo = nodo.hijos[posicion]
        hijo_derecho = nodo.hijos[posicion + 1]

        # Fusionar la clave del padre y todas las claves del hermano derecho
        hijo_izquierdo.claves.append(nodo.claves.pop(posicion))
        hijo_izquierdo.claves.extend(hijo_derecho.claves)

        if not hijo_izquierdo.hoja:
            hijo_izquierdo.hijos.extend(hijo_derecho.hijos)

        # Eliminar el hermano derecho
        nodo.hijos.pop(posicion + 1)

    def obtener_maximo(self, nodo: NodeVehiculo) -> Vehiculo:
        # Descender hasta la hoja más a la derecha
        while not nodo.hoja:
            nodo = nodo.hijos[-1]
        return nodo.claves[-1]

    def obtener_minimo(self, nodo: NodeVehiculo) -> Vehiculo:
        # Descender hasta la hoja más a la izquierda
        while not nodo.hoja:
            nodo = nodo.hijos[0]
        return nodo.claves[0]

    def imprimir_usuario(self) -> str:
        dot: str = "digraph G {\n\t"
        # Cambiar el color de fondo del gráfico
        dot += "bgcolor=\"#ffffff\";\n\t"  # Fondo oscuro
        # Cambiar el color del texto (fuentes)
        dot += "fontcolor=black;\n\t"
        # Cambiar el color de las líneas entre nodos (bordes)
        dot += "edge [fontcolor=white color=\"#FF6347\"];\n\t"  # Color de los bordes (rojo)
        # Cambiar el estilo de los nodos (forma, color de fondo, color de borde)
        dot += "node [shape=record width=1.2 style=filled fillcolor=\"#bfdbf7\" fontcolor=black color=\"#e1e5f2\"];\n\t"  # Nodo verde
        # Aquí estamos llamando al métod imprimir() para obtener la estructura del árbol
        dot += self.imprimir(self.raiz)
        dot += "\n}"
        return dot

    def imprimir(self, nodo: NodeVehiculo, id: list[int] = [0]) -> str:
        raiz: NodeVehiculo = nodo
        arbol = f"n{id[0]}[label=\""
        contador: int = 0
        for item in raiz.claves:
            if contador == len(raiz.claves) - 1:
                # Imprimir solo la placa del vehículo
                arbol += f"<f{contador}>|{item.get_placa()}|<f{contador + 1}>"
                break
            arbol += f"<f{contador}>|{item.get_placa()}|"
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
        image_file = "arbol_b.svg"
        try:
            subprocess.run(["dot", "-Tsvg", dot_file, "-o", image_file], check=True)
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
