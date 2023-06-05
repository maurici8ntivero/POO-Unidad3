import csv
from os.path import dirname,join
from classes.facultad import Facultad
def loadFileCSV():
    list = []
    file = open(join(dirname(__file__),'facultades.csv'))
    lista = csv.reader(file,delimiter=',')
    i = -1
    for row in lista:
        if len(row) == 5:
            list.append(Facultad(row[0],row[1],row[2],row[3],row[4]))
            i += 1
        else:
            list[i].addCarrera(row[1],row[2],row[3],row[4],row[5])
    file.close
    return list