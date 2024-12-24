from Cliente import Cliente
from ListaClientes import ListaClientes
from NodeCliente import NodeCliente
from Vehiculo import Vehiculo

if __name__ == '__main__':

    lista_clientes = ListaClientes()

    ruta_archivo_clientes = "carga_clientes.txt"
    exit = False
    while exit == False:
        print(f'''

        LLEGADA RAPIDITO

         1) Cargar Clientes.
         2) Salir.
          ''')
        option = int(input("\t> Selecciona una opcion:"))
        if option == 1:
            archivo = open(ruta_archivo_clientes, 'r')
            contenido_archivo = archivo.read()
            # print(contenido_archivo)
            particion_linea = contenido_archivo.split('\n')
            # print(particion_linea)
            for index in range(len(particion_linea)):
                particion_comas = particion_linea[index].split(',')
                lista_clientes.insertar_inicio(
                    Cliente(particion_comas[0], particion_comas[1],
                            particion_comas[2], particion_comas[3],
                            particion_comas[4], particion_comas[5].strip(';')))
            print("\n")
            lista_clientes.generar_reporte()
        elif option == 2:
            print('Finalizo el programa.')
            exit = True
