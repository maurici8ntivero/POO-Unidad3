class Taller:
    def __init__(self,id=0,nombre='',vacantes=0,montoInscripcion=0):
        self.__id = id
        self.__nombre = nombre
        self.__vacantes = vacantes
        self.__montoInscripcion = montoInscripcion
        self.__inscripciones = []
    #GET - Id
    def getId(self): return self.__id
    #GET - Nombre
    def getNombre(self): return self.__nombre
    #GET - Vacantes
    def getVacantes(self): return self.__vacantes
    #GET - Monto
    def getMonto(self): return self.__montoInscripcion
    #Inscribir
    def addInscripcion(self,inscripcion):
        if len(self.__inscripciones) < self.__vacantes:
            self.__inscripciones.append(inscripcion)
        else: print("Ya no se pueden inscribir mas personas a este taller")
    #Vacantes
    def consultarVacante(self):
        if len(self.__inscripciones) < self.__vacantes:
            return True
        else: return False
    #Consultar inscriptos
    def inscripciones(self):
        if len(self.__inscripciones) == 0:
            print('\nNo hay inscripciones en este taller.')
        else:
            for i in self.__inscripciones:
                i.alumnoInscripcion()