class Cliente:
    def __init__(self, dpi, nombres, apellidos, genero, telefono, direccion):
        self.__dpi = dpi
        self.__nombres = nombres
        self.__apellidos = apellidos
        self.__genero = genero
        self.__telefono = telefono
        self.__direccion = direccion

    def get_dpi(self):
        return self.__dpi

    def set_dpi(self, dpi):
        self.__dpi = dpi

    def get_nombres(self):
        return self.__nombres

    def set_nombres(self, nombres):
        self.__nombres = nombres

    def get_apellidos(self):
        return self.__apellidos

    def set_apellidos(self, apellidos):
        self.__apellidos = apellidos

    def get_genero(self):
        return self.__genero

    def set_genero(self, genero):
        self.__genero = genero

    def get_telefono(self):
        return self.__telefono

    def set_telefono(self, telefono):
        self.__telefono = telefono

    def get_direccion(self):
        return self.__direccion

    def set_direccion(self, direccion):
        self.__direccion = direccion


    def __str__(self):
        return f'Cliente->[dpi: {self.get_dpi()}, nombres: {self.get_nombres()}]'