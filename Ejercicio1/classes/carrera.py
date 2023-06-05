class Carrera:
    def __init__(self,codigo='',nombre='',titulo='',duracion='',grado=''):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__titulo = titulo
        self.__duracion = duracion
        self.__grado = grado
    #GET - Codigo
    def getCodigo(self): return self.__codigo
    #GET - Nombre
    def getNombre(self): return self.__nombre
    #GET - Grado
    def getGrado(self): return self.__grado
    #GET - Duracion
    def getDuracion(self): return self.__duracion
    #GET - Titulo
    def getTitulo(self): return self.__titulo
