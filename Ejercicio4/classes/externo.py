from classes.empleado import Empleado
class EmpleadoExterno(Empleado):
    def __init__(self,dni=0,nombre='',direccion='',telefono='',tarea='',fechaInicio='',fechaFin='',montoViatico=0,costoObra=0,montoSeguro=0):
        super().__init__(dni,nombre,direccion,telefono)
        self.__tarea = tarea
        self.__fechaInicio = fechaInicio
        self.__fechaFin = fechaFin
        self.__montoViatico = montoViatico
        self.__costoObra = costoObra
        self.__montoSeguro = montoSeguro
    #GET - Tarea
    def getTarea(self): return self.__tarea
    #GET - Fecha Inicio
    def getFechaInicio(self): return self.__fechaInicio
    #GET - Fecha Fin
    def getFechaFin(self): return self.__fechaFin
    #GET - Monto Viatico
    def getMontoViatico(self): return self.__montoViatico
    #GET - Costo de Obra
    def getCostoObra(self): return self.__costoObra
    #GET - Monto de Seguro de Vida
    def getMontoSeguro(self): return self.__montoSeguro
    #GET - Salario POLIMORFISMO
    def getSalario(self):
        salario = self.__costoObra - self.__montoViatico - self.__montoSeguro
        return salario