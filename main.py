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

    exit = False
    while exit == False:
        print(f'''

        LLEGADA RAPIDITO

         1) Carga Masiva De Clientes.
         2) Carga Masiva De Vehiculos.
         3) Carga Masiva De Rutas.
         4) Implementacion Viajes.(Tarea)
         5) Salir.
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
            lista_clientes.generar_reporte()
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
            print("Carga Masiva De Rutas.")
            pass
        if option == 4:
            pass
        elif option == 5:
            print('Finalizo el programa.')
            exit = True
