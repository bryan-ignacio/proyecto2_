from ArbolBVehiculos import ArbolBVehiculos
from Cliente import Cliente
from ListaClientes import ListaClientes
from NodeCliente import NodeCliente
from Vehiculo import Vehiculo

if __name__ == '__main__':

    lista_clientes = ListaClientes()
    arbol_vehiculos = ArbolBVehiculos(5)

    ruta_archivo_clientes = "carga_clientes.txt"
    ruta_archivo_vehiculos = "carga_vehiculos.txt"
    ruta_archivo_rutas = "carga_rutas.txt"

    exit = False
    while exit == False:
        print(f'''
        --------------------
          LLEGADA RAPIDITO
        --------------------
         1) Carga Masiva De Clientes.
         2) Carga Masiva De Vehiculos.
         3) Carga Masiva De Rutas.
         4) Implementacion Viajes.(Tarea)
         5) Menu Clientes.
         6) Menu Vehiculos. 
         7) Menu Viajes.
         8) Salir.
          ''')
        option = int(input("\t> Selecciona una opcion:"))
        if option == 1:
            archivo = open(ruta_archivo_clientes, 'r')
            contenido_archivo = archivo.read()
            particion_linea = contenido_archivo.split('\n')
            for index in range(len(particion_linea)):
                particion_comas = particion_linea[index].split(',')
                lista_clientes.insertar_inicio(
                    Cliente(particion_comas[0], particion_comas[1],
                            particion_comas[2], particion_comas[3],
                            particion_comas[4], particion_comas[5].strip(';')))
            print("\n")
        if option == 2:
            archivo_dos = open(ruta_archivo_vehiculos, 'r')
            contenido_archivo_dos = archivo_dos.read()
            particion_linea_dos = contenido_archivo_dos.split('\n')
            for index in range(len(particion_linea_dos)):
                particion_puntocoma = particion_linea_dos[index].split(':')
                arbol_vehiculos.insertar_valor(
                    Vehiculo(particion_puntocoma[0],
                             particion_puntocoma[1],
                             particion_puntocoma[2],
                             particion_puntocoma[3].strip(';'))
                )
                arbol_vehiculos.generar_reporte()
            print("\n")
        if option == 3:
            archivo_tres = open(ruta_archivo_rutas, 'r')
            contenido_archivo_tres = archivo_tres.read()
            particion_linea_tres = contenido_archivo_tres.split('\n')
            for index in range(len(particion_linea_tres)):
                particion_diagonal = particion_linea_tres[index].split('/')
                print(particion_diagonal[0])
                print(particion_diagonal[1])
                print(particion_diagonal[2].strip('%'))
        if option == 4:
            print("Los Viajes se almacenaran en una Lista Simple.")
        if option == 5:
            exit_clientes = False
            while exit_clientes == False:
                print(f'''
                --------------------
                    MENU CLIENTES
                --------------------
                1) Crear Cliente.
                2) Modificar Cliente.
                3) Eliminar Cliente.
                4) Mostrar Informacion Cliente.
                5) Generar Reporte Clientes.
                6) Regresar.
                ''')
                option_clientes = int(input("\t> Selecciona una opcion:"))
                if option_clientes == 1:
                    print("Crear Cliente")
                    new_dpi = str(input(">Ingresa el DPI: "))
                    new_nombres = str(input(">Ingresa los Nombres: "))
                    new_apellidos = str(input(">Ingresa los Apellidos: "))
                    new_genero = str(input(">Ingresa el Genero: "))
                    new_telefono = str(input(">Ingresa el Telefono: "))
                    new_direccion = str(input(">Ingresa la Direccion: "))
                    lista_clientes.insertar_inicio(
                        Cliente(new_dpi, new_nombres, new_apellidos, new_genero, new_telefono, new_direccion))
                if option_clientes == 2:
                    print("Modificar Cliente")
                    in_dpi = str(input(">Ingresa el DPI a modificar: "))
                    if lista_clientes.buscar_node_cliente(in_dpi) is not None:
                        node_cliente = lista_clientes.buscar_node_cliente(in_dpi)
                        print(node_cliente.get_cliente())
                        print("Ingresa la Nueva Inforamcion del Cliente")
                        new_dpi = str(input(">Ingresa el DPI: "))
                        new_nombres = str(input(">Ingresa los Nombres: "))
                        new_apellidos = str(input(">Ingresa los Apellidos: "))
                        new_genero = str(input(">Ingresa el Genero: "))
                        new_telefono = str(input(">Ingresa el Telefono: "))
                        new_direccion = str(input(">Ingrese la Direccion:"))
                        lista_clientes.modificar_node_cliente(in_dpi, new_dpi, new_nombres, new_apellidos, new_genero,
                                                              new_telefono, new_direccion)
                    else:
                        print("No se pudo modificar, No existe Cliente")
                if option_clientes == 3:
                    print("Eliminar Cliente")
                    in_dpi = str(input(">Ingresa el DPI a eliminar: "))
                    if lista_clientes.buscar_node_cliente(in_dpi) is not None:
                        node_cliente = lista_clientes.buscar_node_cliente(in_dpi)
                        print(node_cliente.get_cliente())
                        lista_clientes.eliminar_node_cliente(in_dpi)
                    else:
                        print("Este Cliente no se puede eliminar, no existe")
                if option_clientes == 4:
                    print("Mostrar Informacion Cliente")
                if option_clientes == 5:
                    print("Generar Reporte Clientes")
                    lista_clientes.generar_reporte()
                    print("Reporte: Lista Clientes Generado.")
                elif option_clientes == 6:
                    print("Regresó al Menu principal.")
                    exit_clientes = True
        if option == 6:
            print("Menu Vehiculos.")
        if option == 7:
            print("Menu Viajes.")
        elif option == 8:
            print('Finalizo el programa.')
            exit = True
