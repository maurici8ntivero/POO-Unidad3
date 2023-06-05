import csv
from os.path import dirname,join
from classes.taller import Taller

def loadFileCSV():
    list = []
    file = open(join(dirname(__file__),'talleres.csv'))
    lista = csv.reader(file,delimiter=';')
    flag = True
    for row in lista:
        if flag: flag = False
        else:
            list.append(Taller(int(row[0]),row[1],int(row[2]),int(row[3])))
    file.close
    return list