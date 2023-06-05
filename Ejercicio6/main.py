from claseMenu import Menu
from claseManejadorVehiculos import ManejadorVehiculos
from claseObjectEncoder import ObjectEncoder
# otra forma de hacer pero con showmenu...
if __name__ == '__main__':
    #Creo el manejador y cargo los vehiculos
    miManejador = ManejadorVehiculos()
    encoder = ObjectEncoder()
    lista = encoder.leerJSONArchivo('vehiculos.json')
    miManejador.decodificarLista(lista)

    miMenu = Menu()
    miMenu.define_menu('CONCESIONARIA ESTOY CANSADO.COM',
            ['[1]- Insertar un vehiculo en la coleccion en una posicion determinada.',
            '[2]- Agregar un vehiculo a la coleccion.',
            '[3]- Dada una posicion de la Lista: Mostrar por pantalla que tipo de objeto se encuentra almacenado en dicha posicion.',
            '[4]- Dada la patente de un vehiculo usado, modificar el precio base, y luego mostrar el precio de venta.',
            '[5]- Mostrar todos los datos, incluido el importe de venta, del vehiculo más económico.',
            '[6]- Mostrar para todos los vehiculos que la concesionaria tiene a la venta, modelo, cantidad de puertas e importe de venta.',
            '[7]- Almacenar los objetos de la coleccion Lista en el archivo "vehiculos.json".',
            '[0]- Salir.'])
    
    miMenu.showMenu()
    op = miMenu.selectOption()
    while op != 0:
        if op == 1:
            vehiculo = miManejador.crearVehiculo()
            if vehiculo != None:
                miManejador.showPosDisponibles()
                posicion = input('Ingrese posicion deseada: ')
                miManejador.insertarVehiculo(vehiculo,posicion)
            input('Presione ENTER para continuar...')
        elif op == 2:
            vehiculo = miManejador.crearVehiculo()
            if vehiculo != None:
                miManejador.agregarVehiculo(vehiculo)
            input('Presione ENTER para continuar...')
        elif op == 3:
            miManejador.showPosDisponibles()
            posicion = input('Ingrese posicion deseada: ')
            miManejador.showTipoObjeto(posicion)
            input('Presione ENTER para continuar...')
        elif op == 4:
            miManejador.showPatentes()
            patente = input('Ingrese patente: ')
            vehiculo = miManejador.buscarPorPatente(patente)
            if vehiculo != None:
                precioB = input('Ingrese nuevo precio base: ')
                vehiculo.modificarPrecioBase(precioB)
                importe = vehiculo.calcPrecioVenta()
                print('\nImporte de venta [$]: {0:27}'.format(str(importe)))
            input('Presione ENTER para continuar...')
        elif op == 5:
            miManejador.masEconomico()
            input('Presione ENTER para continuar...')
        elif op == 6:
            miManejador.showAllVehiculos()
            input('Presione ENTER para continuar...')
        elif op == 7:
            lista = miManejador.toJSON()
            encoder.guardarJSONArchivo(lista,'vehiculos.json')
            print('Datos guardados.')
            input('Presione ENTER para continuar...')

        miMenu.showMenu()
        op = miMenu.selectOption()