from ArbolBVehiculos import ArbolBVehiculos
from Cliente import Cliente
from ListaAdyacencia import ListaAdyacencia
from ListaClientes import ListaClientes
from ListaViajes import ListaViajes
from NodeCliente import NodeCliente
from Ruta import Ruta
from Vehiculo import Vehiculo
from Viaje import Viaje

if __name__ == '__main__':

    lista_clientes = ListaClientes()
    arbol_vehiculos = ArbolBVehiculos(5)
    lista_rutas = ListaAdyacencia()
    lista_viajes = ListaViajes()

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
            print("datos cargados con exito...")
        if option == 3:
            archivo_tres = open(ruta_archivo_rutas, 'r')
            contenido_archivo_tres = archivo_tres.read()
            particion_linea_tres = contenido_archivo_tres.split('\n')
            for index in range(len(particion_linea_tres)):
                particion_diagonal = particion_linea_tres[index].split('/')
                lista_rutas.insertar(
                    Ruta(particion_diagonal[0], particion_diagonal[1], int(particion_diagonal[2].strip('%'))))
            lista_rutas.generar_reporte()
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
                        print("Ingresa la Nueva Informacion del Cliente")
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
                    in_dpi = str(input(">Ingresa el DPI del cliente: "))
                    node_cliente = lista_clientes.buscar_node_cliente(in_dpi)
                    if node_cliente is not None:
                        print("---------------------------------")
                        print('dpi: ', node_cliente.get_cliente().get_dpi())
                        print('nombres: ', node_cliente.get_cliente().get_nombres())
                        print('apellidos: ', node_cliente.get_cliente().get_apellidos())
                        print('genero: ', node_cliente.get_cliente().get_genero())
                        print('telefono: ', node_cliente.get_cliente().get_telefono())
                        print('direccion: ', node_cliente.get_cliente().get_direccion())
                        print("---------------------------------")
                    else:
                        print("No se puede mostrar informacion del cliente, no existe.")
                if option_clientes == 5:
                    print("Generar Reporte Clientes")
                    lista_clientes.generar_reporte()
                    print("Reporte: Lista Clientes Generado.")
                elif option_clientes == 6:
                    print("Regresó al Menu principal.")
                    exit_clientes = True
        if option == 6:
            exit_vehiculos = False
            while exit_vehiculos == False:
                print(f'''
                --------------------
                   MENU VEHICULOS
                --------------------
                1) Crear Vehiculo.
                2) Modificar Vehiculo.
                3) Eliminar Vehiculo.
                4) Mostrar Informacion Vehiculo.
                5) Generar Reporte Vehiculos.
                6) Regresar.
                ''')
                option_vehiculos = int(input("\t> Selecciona una opcion:"))
                if option_vehiculos == 1:
                    print("Crear Vehiculo:")
                    new_placa = str(input("\t>Ingresa la placa: "))
                    new_marca = str(input("\t>Ingresa la marca: "))
                    new_modelo = str(input("\t>Ingresa el modelo: "))
                    new_precio = str(input("\t>Ingresa el precio: "))
                    arbol_vehiculos.insertar_valor(Vehiculo(new_placa, new_marca, new_modelo, new_precio))
                if option_vehiculos == 2:
                    print("Modificar Vehiculo:")
                    in_vehiculo = str(input("\t>Ingresa la placa del vehiculo a Modificar: "))
                    vehiculo = arbol_vehiculos.buscar(in_vehiculo)
                    if vehiculo is not None:
                        print(vehiculo)
                        print("Ingresa la Nueva Informacion del Cliente")
                        new_placa = str(input("\t>Ingresa la placa: "))
                        new_marca = str(input("\t>Ingresa la marca: "))
                        new_modelo = str(input("\t>Ingresa el modelo: "))
                        new_precio = str(input("\t>Ingresa el precio: "))
                        arbol_vehiculos.modificar(in_vehiculo, new_placa, new_marca, new_modelo, new_precio)
                    else:
                        print("No se pudo modificar, No existe Vehiculo")
                if option_vehiculos == 3:
                    print("Eliminar Vehiculo:")
                    in_placa = str(input("\t>Ingresa la placa del vehiculo a Eliminar: "))
                    vehiculo = arbol_vehiculos.buscar(in_placa)
                    arbol_vehiculos.eliminar(in_placa)
                    print(f"Vehiculo Eliminado: {vehiculo}")
                if option_vehiculos == 4:
                    print("Mostrar Informacion Vehiculo:")
                    in_placa = str(input(">Ingresa la PLACA del Vehiculo: "))
                    vehiculo = arbol_vehiculos.buscar(in_placa)
                    if vehiculo is not None:
                        print("---------------------------------")
                        print("placa:", vehiculo.get_placa())
                        print("marca:", vehiculo.get_marca())
                        print("modelo:", vehiculo.get_modelo())
                        print("precio:", vehiculo.get_precio())
                        print("---------------------------------")
                    else:
                        print("No se puede mostrar informacion del Vehiculo, no existe.")
                if option_vehiculos == 5:
                    print("Generar Reporte Vehiculos:")
                    arbol_vehiculos.generar_reporte()
                    print("Reporte: Arbol Vehiculos Generado.")
                if option_vehiculos == 6:
                    print("Regresó al Menu principal.")
                    exit_vehiculos = True
        if option == 7:
            exit_viajes = False
            while exit_viajes == False:
                print(f'''
                 --------------------
                    MENU VIAJES
                 --------------------
                 1) Crear Viaje.
                 2) Mostrar Informacion Viaje.
                 3) Generar Reporte Viaje.
                 4) Regresar.
                 ''')
                option_viajes = int(input("\t> Selecciona una opcion:"))
                if option_viajes == 1:
                    print("Crear Viaje:")
                    new_origen = str(input("\t>Ingresa el origen: "))
                    new_destino = str(input("\t>Ingresa el destino: "))
                    new_fecha = str(input("\t>Ingresa la fecha: "))
                    new_cliente = str(input("\t>Ingresa el dpi del Cliente a buscar: "))
                    new_vehiculo = str(input("\t>Ingresa la placa del vehiculo a buscar: "))
                    new_ruta = str(input("\t>Ingresa la ruta: "))
                    lista_viajes.insertar_final(
                        Viaje(new_origen, new_destino, new_fecha, new_cliente, new_vehiculo, new_ruta))
                if option_viajes == 2:
                    print("Mostrar Informacion Viaje:")
                    in_id = str(input(">Ingresa el ID del Viaje: "))
                    viaje = lista_viajes.buscar(in_id)
                    if viaje is not None:
                        print("---------------------------------")
                        print("origen:", viaje.get_viaje().get_origen())
                        print("destino:", viaje.get_viaje().get_destino())
                        print("fecha:", viaje.get_viaje().get_fecha())
                        print("cliente:", viaje.get_viaje().get_cliente())
                        print("vehiculo:", viaje.get_viaje().get_vehiculo())
                        print("ruta:", viaje.get_viaje().get_ruta_tomada())
                        print("---------------------------------")
                    else:
                        print("No se puede mostrar informacion del Viaje, no existe.")
                if option_viajes == 3:
                    print("Generar Reporte Viaje:")
                    lista_viajes.generar_reporte()
                    print("Reporte: Lista Viajes Generado.")
                if option_viajes == 4:
                    print("Regresó al Menu Principal.")
                    exit_viajes = True
        elif option == 8:
            print('Finalizo el programa.')
            exit = True
