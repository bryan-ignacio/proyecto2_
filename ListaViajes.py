from NodeViaje import NodeViaje
import os
from graphviz import Digraph

class ListaViajes:
    def __init__(self):
        self.cabeza: NodeViaje = None

    def insertar_final(self, viaje) -> NodeViaje:
        aux: NodeViaje = self.cabeza
        if aux is None:
            aux = NodeViaje(
                viaje.get_origen(),
                viaje.get_destino(),
                viaje.get_fecha(),
                viaje.get_cliente(),
                viaje.get_vehiculo(),
                viaje.get_ruta_tomada()
            )
            self.cabeza = aux
            return self.cabeza
        while aux.siguiente is not None:
            aux = aux.siguiente
        aux.siguiente = NodeViaje(
            viaje.get_origen(),
            viaje.get_destino(),
            viaje.get_fecha(),
            viaje.get_cliente(),
            viaje.get_vehiculo(),
            viaje.get_ruta_tomada())
        return aux.siguiente


    def buscar(self, id_viaje) -> NodeViaje:
        aux: NodeViaje = self.cabeza
        if aux is None:
            return None
        while aux is not None:
            if aux.get_viaje().get_id() == id_viaje:
                return aux
            aux = aux.siguiente
        return None



    def imprimir(self):
        if self.cabeza is None:
            print("Lista Vacia")
        else:
            aux = self.cabeza
            while aux is not None:
                print(aux.datos_viaje())
                aux = aux.siguiente

    def generar_reporte(self):
        if self.cabeza is None:
            print("La lista está vacía. No hay nada que graficar.")
            return

        dot = Digraph("ListaViajes")
        dot.attr(rankdir="LR")  # Layout horizontal de izquierda a derecha
        dot.attr("node", shape="record")

        aux = self.cabeza
        while aux is not None:
            # Creación de un nodo para cada viaje
            viaje = aux.get_viaje()
            node_label = f"ID: {viaje.get_id()}\\nOrigen: {viaje.get_origen()}\\nDestino: {viaje.get_destino()}"
            dot.node(f"viaje_{viaje.get_id()}", node_label)

            # Conexión al siguiente nodo si existe
            if aux.siguiente is not None:
                dot.edge(f"viaje_{viaje.get_id()}", f"viaje_{aux.siguiente.get_viaje().get_id()}")

            aux = aux.siguiente

        # Guardar el archivo .dot
        dot.render("ListaViajes", format="png", cleanup=True)
        print("Reporte generado exitosamente: ListaViajes.png")

        # Abrir automáticamente la imagen generada
        open("ListaViajes.png")

    # def eliminar_frente(self):
    #     cabeza: Node = self.cabeza
    #     if cabeza is not None:
    #         self.cabeza = cabeza.sig
    #         return self.cabeza

    # def insertar_frente(self, valor) -> Node:
    #     nuevo_nodo: Node = Node(valor)
    #     if self.cabeza is None:
    #         self.cabeza = nuevo_nodo
    #         return self.cabeza
    #     nuevo_nodo.sig = self.cabeza
    #     self.cabeza = nuevo_nodo
    #     return self.cabeza
    #