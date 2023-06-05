import re
from claseLista import Lista
from claseVehiculo import Vehiculo
from claseVehiculoNuevo import VehiculoNuevo
from claseVehiculoUsado import VehiculoUsado

class ManejadorVehiculos:
    __vehiculos = None

    def __init__(self):
        self.__vehiculos = Lista()

    def decodificarLista(self,ListaVehiculos):
        for i in range(len(ListaVehiculos)):
            dVehiculo = ListaVehiculos[i]
            class_name = dVehiculo.pop('__class__')
            class_=eval(class_name)
            atributos = dVehiculo['__atributos__']
            unVehiculo = class_(**atributos)
            self.__vehiculos.agregarElemento(unVehiculo)

    def agregarVehiculo(self,vehiculo):
        if isinstance(vehiculo,Vehiculo):
            self.__vehiculos.agregarElemento(vehiculo)
        else:
            print('Error: No se puede agregar el vehiculo.')
    
    def insertarVehiculo(self,vehiculo,posicion):
        if isinstance(vehiculo,Vehiculo):
            self.__vehiculos.insertarElemento(vehiculo,posicion)
        else:
            print('Error: No se puede agregar el vehiculo.')

    #Muestro las posiciones disponibles para ayudar al usuario
    def showPosDisponibles(self):
        print('Posiciones disponibles: [1 - {0}]'.format(self.__vehiculos.len()))

    def showTipoObjeto(self,posicion):
        vehiculo = self.__vehiculos.mostrarElemento(posicion)
        if vehiculo != None:
            if isinstance(vehiculo,VehiculoNuevo):
                tipo = 'VEHICULO NUEVO'
            else:
                tipo = 'VEHICULO USADO' 
            print('Tipo de objeto almacenado en posicion {}: {}'.format(posicion,tipo))
   
    def crearVehiculo(self):
        newVehiculo = None
        try:
            header = '+' + '-'*50 + '+'
            print(header)
            print('|{0:^50}|'.format('DATOS NUEVO VEHICULO'))
            print(header)
            #Solicito datos vehiculo (clase padre)
            modelo = input('Modelo: ')
            cantP = input('Cantidad de puertas: ')
            color = input('Color: ')
            precioB = input('Precio base: ')
            marca = input('Marca: ')
            tipo = input('Nuevo o usado [N][U]: ')
            #Convierto datos a tipo correcto
            cantP = int(cantP)
            precioB = int(precioB)

            #Solicito datos vehiculo nuevo o usado (subclases)
            while tipo.lower() != 'n' and tipo.lower() != 'u':
                print('Tipo no admitido, reintente.')
                tipo = input('Nuevo o usado [N][U]: ')
            if tipo.lower() == 'n':
                version = input('Version [Full][Base]: ')
                while version.lower() != 'full' and version.lower() != 'base':
                    print('Version no valida, reintente.')
                    version = input('Version [Full][Base]: ')
                newVehiculo = VehiculoNuevo(modelo,cantP,color,precioB,marca,version)
            elif tipo.lower() == 'u':
                patente = input('Patente: ')
                patente = patente.upper()
                #Valido patente con expresion regular (solo admite patente moderna XX111XX):
                while re.search(r'^[A-Z]{2}[\d]{3}[A-Z]{2}$',patente) == None:
                    print('Error al ingresar la patente, esta debe tener formato AA111AA')
                    patente = input('Patente: ')
                    patente = patente.upper()
                anio = input('Año: ')
                km = input('Kilometraje: ')
                anio =int(anio)
                km = int(km)
                newVehiculo = VehiculoUsado(modelo,cantP,color,precioB,marca,patente,anio,km)
        except ValueError:
            print('Error: No se pudo crear el vehiculo') 
        return newVehiculo
    
    #Muestro patentes para que el usuario sepa las que estan disponibles
    def showPatentes(self):
        header = '+' + '-'*50 + '+'
        print(header)
        print('|{0:^50}|'.format('PATENTES DE AUTOS USADOS'))
        print(header)
        for vehiculo in self.__vehiculos:
            if isinstance(vehiculo,VehiculoUsado):
                print('| {0:49}|'.format(vehiculo.getPatente()))
        print(header)

    #Solo para usados
    def buscarPorPatente(self,patente):
        miVehiculo = None
        patente = patente.upper()
        if re.search(r'^[A-Z]{2}[\d]{3}[A-Z]{2}$',patente) != None:
            i = 0
            esta = False
            while i < self.__vehiculos.len() and not esta:
                vehiculo = self.__vehiculos.mostrarElemento(i+1)
                if isinstance(vehiculo,VehiculoUsado):
                    if patente == vehiculo.getPatente():
                        esta = True
                        miVehiculo = vehiculo
                i +=1
            if not esta:
                print('La patente no corresponde a un vehiculo usado')
        else:
            print('Error al ingresar la patente, esta debe tener formato AA111AA')
        return miVehiculo
    
    def masEconomico(self):
        #Encuentro el mas economico
        vehiculo = self.__vehiculos.mostrarElemento(1)
        min = vehiculo.calcPrecioVenta() 
        for vehiculo in self.__vehiculos:
            importe = vehiculo.calcPrecioVenta()
            if min > importe:
                min = importe
                vEconomico = vehiculo
        #Muestro los datos
        header = '+' + '-'*50 + '+'
        print(header)
        print('|{0:^50}|'.format('VEHICULO MAS ECONOMICO'))
        print(header)
        print('| Importe de venta [$]: {0:27}|'.format(str(importe)))
        print(header)
        modelo = vEconomico.getModelo()
        cantPuertas = vEconomico.getCantP()
        color = vEconomico.getColor()
        precioBase = vEconomico.getPbase()
        marca = vEconomico.getMarca()
        print('| Modelo: {:41}|'.format(modelo))
        print('| Cantidad de puertas: {:28}|'.format(str(cantPuertas)))
        print('| Color: {:42}|'.format(color))
        print('| Precio base [$]: {:32}|'.format(str(precioBase)))
        print('| Marca: {:42}|'.format(marca))
        if isinstance(vEconomico,VehiculoNuevo):
            version = vEconomico.getVersion()
            print('| Condicion: {:38}|'.format('NUEVO'))
            print('| Version: {:40}|'.format(version))
        else:
            patente = vEconomico.getPatente()
            anio = vEconomico.getAnio()
            km = vEconomico.getKm()
            print('| Condicion: {:38}|'.format('USADO'))
            print('| Patente: {:40}|'.format(patente))
            print('| Año: {:44}|'.format(str(anio)))
            print('| Kilometraje: {:36}|'.format(str(km)))
        print(header)

    def showAllVehiculos(self):
        header = '+' + '-'*50 + '+'
        print(header)
        print('|{0:^50}|'.format('VEHICULOS DISPONIBLES'))
        print(header)
        for vehiculo in self.__vehiculos:
            importe = vehiculo.calcPrecioVenta()      
            #Muestro los datos
            modelo = vehiculo.getModelo()
            cantPuertas = vehiculo.getCantP()
            print('| Modelo: {:41}|'.format(modelo))
            print('| Cantidad de puertas: {:28}|'.format(str(cantPuertas)))
            print('| Importe de venta [$]: {0:27}|'.format(str(importe)))
            print(header)
        
    def toJSON(self):
        l = []
        for vehiculo in self.__vehiculos:
            l.append(vehiculo.toJSON())
        return l
