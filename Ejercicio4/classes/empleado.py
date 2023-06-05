class Empleado:
    def __init__(self,dni=0,nombre='',direccion='',telefono=''):
        self.__dni = dni
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono
    #GET - Dni
    def getDni(self): return self.__dni
    #GET - Nombre
    def getNombre(self): return self.__nombre
    #GET - Direccion
    def getDireccion(self): return self.__direccion
    #GET - Telefono
    def getTelefono(self): return self.__telefono
    #GET - Salario
    def getSalario(self):
        pass