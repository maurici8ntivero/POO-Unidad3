import csv
import numpy as np
from datetime import datetime,date
from os.path import dirname,join
from classes.empleado import Empleado
from classes.planta import EmpleadoPlanta
from classes.contrado import EmpleadoContratado
from classes.externo import EmpleadoExterno

class EmpleadoController:
    def __init__(self):
        self.__array = np.empty(9,dtype=Empleado)
        self.__index = 0
    def loadCsv(self,name):
        file = open(join(dirname(__file__), name))
        lista = csv.reader(file,delimiter=';')
        flag = True
        for row in lista:
            if flag: flag = False
            else:
                self.__loadRow(row,name)
        file.close()
    def __loadRow(self,row,name):
        empleado = None
        if name == 'utils/planta.csv':
            empleado = EmpleadoPlanta(int(row[0]),row[1],row[2],row[3],int(row[4]),int(row[5]))
        if name == 'utils/contratados.csv':
            empleado = EmpleadoContratado(int(row[0]),row[1],row[2],row[3],row[4],row[5],int(row[6]))
        if name == 'utils/externos.csv':
            empleado = EmpleadoExterno(int(row[0]),row[1],row[2],row[3],row[4],row[5],row[6],int(row[7]),int(row[8]),int(row[9]))
        self.__array[self.__index] = empleado
        self.__index += 1
        return
    #Registrar Horas a los Empleados Contratados
    def registrarHoras(self):
        dni = int(input('Ingresar DNI:\t'))
        i = 0
        found = False
        while i < len(self.__array):
            if self.__array[i].getDni() == dni:
                if type(self.__array[i]) == EmpleadoContratado:
                    print('Horas acumuladas: {}'.format(self.__array[i].getCantidadDeHoras()))
                    horas = int(input('Ingresar cantidad de horas:\t'))
                    self.__array[i].setCantidadDeHoras(horas)
                    print('Total: {}'.format(self.__array[i].getCantidadDeHoras()))
                else: print('\nEl empleado no es contratado. No se puede incrementar la cantidad de horas')
                found = True
                i = len(self.__array)
            i += 1
        if found == False: print('\nNOT FOUND...\tEmpleado no encontrado')
    #Monto de tarea
    def montoTarea(self):
        
        tarea = input('Ingresar el nombre de la tarea:\t')
        found = False
        acum = 0
        for empleado in self.__array:
            if type(empleado) is EmpleadoExterno:
                if empleado.getTarea() == tarea:
                    fecha = empleado.getFechaFin().split('-')
                    day = datetime.now().strftime('%d-%m-%Y').split('-')
                    currentDay = date(int(day[2]),int(day[1]),int(day[0]))
                    endDate = date(int(fecha[2]),int(fecha[1]),int(fecha[0]))
                    if endDate > currentDay:
                        acum += empleado.getSalario()
                    found = True
        if found: print('\nMonto a pagar $',acum)
        else: print('\nTarea no encontrada')
    #Ayuda Economica
    def ayudaEconomica(self):
        for empleado in self.__array:
            if empleado.getSalario() <= 150000:
                print('{} - {} - {}'.format(empleado.getNombre(),empleado.getDireccion(),empleado.getDni()))
    #Calcular sueldo de todos los empleados
    def calcularSueldo(self):
        for i in self.__array:
            print('{} - {} - ${}'.format(i.getNombre(),i.getTelefono(),i.getSalario()))