from classes.empleado import Empleado
class EmpleadoContratado(Empleado):
    __valorHora=3000
    def __init__(self,dni=0,nombre='',direccion='',telefono='',fechaInicio='',fechaFin='',cantidadHoras=0):
        super().__init__(dni,nombre,direccion,telefono)
        self.__fechaInicio = fechaInicio
        self.__fechaFin = fechaFin
        self.__cantidadHoras = cantidadHoras
    #GET - Fecha Inicio
    def getFechaInicio(self): return self.__fechaInicio
    #GET - Fecha Fin
    def getFechaFin(self): return self.__fechaFin
    #GET & SET - Cantidad de Horas
    def getCantidadDeHoras(self): return self.__cantidadHoras
    def setCantidadDeHoras(self,horas): self.__cantidadHoras += horas
    #GET - Valor por Hora
    @classmethod
    def getValorHora(cls): return cls.__valorHora
    #GET - Salario POLIMORFISMO
    def getSalario(self):
        return self.__cantidadHoras * self.__valorHora