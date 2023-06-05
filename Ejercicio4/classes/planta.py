from classes.empleado import Empleado
class EmpleadoPlanta(Empleado):
    def __init__(self,dni=0,nombre='',direccion='',telefono='',sueldo=0,antiguedad=0):
        super().__init__(dni,nombre,direccion,telefono)
        self.__sueldo = sueldo
        self.__antiguedad = antiguedad
    #GET - Sueldo
    def getSueldo(self): return self.__sueldo
    #GET - Antiguedad
    def getAntiguedad(self): return self.__antiguedad
    #GET - Salario POLIMORFISMO
    def getSalario(self):
        salario = self.__sueldo + (self.__antiguedad * (self.__sueldo * 0.1))
        return salario