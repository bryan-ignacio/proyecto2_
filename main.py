from Cliente import Cliente
from ListaClientes import ListaClientes
from Vehiculo import Vehiculo

if __name__ == '__main__':
    c1 = Cliente("3461925281601",
                 "Bryan Cristhopher",
                 "Ignacio Xoy",
                 "M",
                 "30817780",
                 "52 calle 16-00 zona 12")

    c2 = Cliente("3748291048602",
                 "María",
                 "López",
                 "F",
                 "32017654",
                 "Avenida Las Rosas 12-45 zona 5")

    c3 = Cliente("3905617392403",
                 "Carlos",
                 "Hernández",
                 "M",
                 "31098765",
                 "Boulevard Los Próceres 8-22 zona 10")

    c4 = Cliente("3059284736104",
                 "Ana",
                 "Martínez",
                 "F",
                 "31987654",
                 "Colonia El Prado 3-14 zona 7")

    c5 = Cliente("3284015629305",
                 "Jorge",
                 "Gómez",
                 "M",
                 "32234567",
                 "Residenciales Las Flores 2-18 zona 11")

    lista_clientes = ListaClientes()
    lista_clientes.insertar_inicio(c1)
    lista_clientes.insertar_inicio(c2)
    lista_clientes.insertar_inicio(c3)
    lista_clientes.insertar_inicio(c4)
    lista_clientes.insertar_inicio(c5)
    lista_clientes.imprimir()
    lista_clientes.buscar_node_cliente("3059284736104")
    lista_clientes.modificar_node_cliente("123", "123456789",
                                          "NewNombre", "NewApellido",
                                          "M", "12345678",
                                          "Residenciales Nueva Direccion")
    lista_clientes.imprimir()