import numpy as np
from menu import clearConsole
from controllers.saboresController import ManejadorSabor
from classes.helado import Helado

class ManejadorHelados:
    def __init__(self):
        self.__sabor = ManejadorSabor()
        self.__sabor.loadFileCSV()
        self.__list = []
        self.__infoSabor = []
    #Carga info sabor: [id,nombre,cantidad de veces vendido,gramos vendidos]
    def loadInfoSabor(self):
        i = 0
        while i < self.__sabor.cantidadDeSabores():
            name = self.__sabor.getNameSabor(i)
            self.__infoSabor.append([i,name,0,0])
            i+=1
    #Eleccion de tipo de helado
    def __seleccionTipoHelado(self):
        clearConsole()
        gramos = [100,150,250,500,1000]
        precios = [150,250,500,800,1400]
        print('\nTipo de helados:\n1)100 gramos $150\t2)150 gramos $250\t3)250 gramos $500\t4)500 gramos $800\t5)1 Kilo $1400')
        opcionGramos = int(input('\nSelecciona una opcion:\t'))
        return [gramos[opcionGramos - 1],precios[opcionGramos - 1]]
    #Eleccion de sabores
    def __seleccionSabores(self):
        clearConsole()
        sabores = np.empty(4,dtype=int)
        self.__sabor.mostrar()
        print('\nElige 4 sabores...\n')
        i = 0
        while i< len(sabores):
            opcionSabor = int(input('SABOR {}\tCodigo:\t'.format(i+1)))
            sabores[i] = opcionSabor - 1
            i += 1
        return sabores
    #Registrar una venta - Agregacion
    def registrarVenta(self):
        values = self.__seleccionTipoHelado()
        sabores = self.__seleccionSabores()
        gramos = values[0] / 4
        self.__list.append(Helado(values[0], values[1]))
        i = 0
        while i < len(sabores):
            self.__list[len(self.__list) - 1].addSabor(self.__sabor.getSabor(sabores[i]))
            self.__infoSabor[sabores[i]][2] += 1
            self.__infoSabor[sabores[i]][3] += gramos
            i += 1
        print('Venta Registrada...')
    #Top 5 de sabores pedidos
    def saboresMasPedidos(self):
        self.__infoSabor.sort(key=lambda x: x[2],reverse=True)
        i = 0
        while i < 5:
            if self.__infoSabor[i][2] > 0:
                print(self.__infoSabor[i][1])
            i+=1
        self.__infoSabor.sort(key=lambda x: x[0])
    #Gramos vendidos por helado
    def gramosVendidos(self):
        self.__sabor.mostrar()
        codigo = int(input('Ingresar numero de sabor:\t'))
        print('{} - {}'.format(self.__infoSabor[codigo-1][1],self.__infoSabor[codigo-1][3]))
    #Sabores vendidos por tipo de helado
    def saboresVendidosPorTipoDeHelado(self):
        codigos = np.full(len(self.__infoSabor),0)
        values = self.__seleccionTipoHelado()
        for h in self.__list:
            if h.getGramos() == values[0]:
                sabores = h.getSabores()
                for s in sabores:
                    codigos[s]+=1
        i = 0
        while i < len(codigos):
            if codigos[i] > 0:
                print(self.__infoSabor[i][1])
            i+=1
    #Importe por tipo de helado
    def importeRecaudadoPorTipoDeHelado(self):
        importe = 0
        values = self.__seleccionTipoHelado()
        for h in self.__list:
            if h.getGramos() == values[0]:
                importe += h.getPrecio()
        print('\nTotal recaudado para el tipo de helado de {} gramos\n\tTotal = ${}'.format(values[0],importe))