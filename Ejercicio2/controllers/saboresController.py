import csv
from os.path import dirname,join
from classes.sabor import Sabor

class ManejadorSabor:
    def __init__(self):
        self.__list = []
    def loadFileCSV(self):
        file = open(join(dirname(__file__),'sabores.csv'))
        lista = csv.reader(file,delimiter=',')
        for row in lista:
            self.__list.append(Sabor(int(row[0]),row[1],row[2]))
        file.close
    #Mostrar
    def mostrar(self):
        print('SABORES Disponibles...')
        for row in self.__list: 
            print('{} - {}'.format(row.getId(),row.getNombre()))
    #Get Sabor
    def getSabor(self,id):
        return self.__list[id]
    def getNameSabor(self,id):
        return self.__list[id].getNombre()
    def cantidadDeSabores(self):
        return len(self.__list)