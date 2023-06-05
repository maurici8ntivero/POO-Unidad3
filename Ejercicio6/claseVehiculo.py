import abc
from abc import ABC
class Vehiculo(ABC):
    __modelo = ''
    __cantPuertas = 0
    __color = ''
    __precioBase = 0
    __marca = ''

    def __init__(self,modelo,cantP,color,precioB,marca):
        self.__modelo = modelo
        self.__cantPuertas = cantP
        self.__color = color
        self.__precioBase = precioB
        self.__marca = marca
       
    def getModelo(self):
        return self.__modelo
    def getCantP(self):
        return self.__cantPuertas
    def getColor(self):
        return self.__color
    def getPbase(self):
        return self.__precioBase
    def getMarca(self):
        return self.__marca

    def modificarPrecioBase(self,newBase):
        try:
            newBase = int(newBase)
            header = '+' + '-'*50 + '+'
            print(header)
            print('|{0:^50}|'.format('MODIFICAR PRECIO BASE'))
            print(header)
            print('| Actual: {0:41}|'.format(self.__precioBase))
            print('| Nuevo: {0:42}|'.format(newBase))
            print(header)
            op = input('Confirme actualizacion de precio [S][N]: ')
            while op.lower() != 's' and op.lower() != 'n':
                print('Opcion invalida, reintente.')
                op = input('Confirme actualizacion de precio [S][N]: ')
            if op.lower() == 's':
                self.__precioBase = newBase
                print('Actualizacion realizada.')
            else:
                print('No se actualizo el precio.')
        except ValueError:
            print('Error: El precio base debe ser un entero')
    
    @abc.abstractmethod
    def calcPrecioVenta(self):
        pass

    def toJSON(self):
        d=dict(
            modelo = self.__modelo,
            cantP = self.__cantPuertas,
            color = self.__color,
            precioB = self.__precioBase,
            marca = self.__marca)
        return d