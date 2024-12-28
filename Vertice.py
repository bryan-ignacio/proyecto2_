from Lista import Lista


class Vertice:
    def __init__(self, valor: str, peso: int = 0):
        self.valor: str = valor
        self.vecinos: Lista[Vertice] = Lista()
        self.peso: int = peso
        self.peso_acumulado: int = 0
        self.visitado: bool = False

    def get_peso_acumulado(self, peso: int):
        self.peso_acumulado += peso

    def __str__(self):
        aux = self.vecinos.cabeza
        dot: str = ""
        while aux is not None:
            dot += f'edge[label={aux.valor.peso} fontsize=5];\n\t{self.valor} -> {aux.valor.valor};\n\t'
            aux = aux.sig
        return dot
