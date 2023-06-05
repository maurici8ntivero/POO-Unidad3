from os.path import dirname,join
from classes.planta import EmpleadoPlanta
from classes.contrado import EmpleadoContratado
from classes.externo import EmpleadoExterno
import csv

def loadCsv(name):
    list = []
    file = open(join(dirname(__file__), name))
    lista = csv.reader(file,delimiter=';')
    flag = True
    for row in lista:
        if flag: flag = False
        else: loadRow()
    file.close()
    return list
def loadRow(list,row,name):
    print(row)
    empleado = None
    if name == 'planta.csv':
        empleado = EmpleadoPlanta(int(row[0]),row[1],row[2],row[3],int(row[4]),int(row[5]))
    if name == 'contrado.csv':
        empleado = EmpleadoContratado(int(row[0]),row[1],row[2],row[3],row[4],row[5],int(row[6]))
    if name == 'externo.csv':
        empleado = EmpleadoExterno(int(row[0]),row[1],row[2],row[3],row[4],row[5],row[6],int(row[7]),int(row[8]),int(row[9]))
    list.append(empleado)
    return list