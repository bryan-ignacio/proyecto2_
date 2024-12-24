from NodeVehiculo import NodeVehiculo


class ArbolBVehiculos:
    def __init__(self, orden: int):
        self.raiz: NodeVehiculo = NodeVehiculo(True)
        self.orden: int = orden

    def insertar_valor(self):
        pass

    def insertar_valor_no_completo(self):
        pass

    def dividir_pagina(self):
        pass

    def imprimir_usuario(self):
        pass

    def imprimir(self):
        pass

    def __str__(self):
        return f'{self.raiz}'

    def generar_reporte(self):
        pass