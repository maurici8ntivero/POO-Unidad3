class Persona:
    def __init__(self,nombre='',direccion='',dni=0):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__dni = dni
    #GET - Nombre
    def getNombre(self): return self.__nombre
    #GET - Direccion
    def getDireccion(self): return self.__direccion
    #GET - Dni
    def getDni(self): return self.__dni