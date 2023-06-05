from classes.carrera import Carrera
class Facultad:
    def __init__(self,codigo='',nombre='',direccion='',localidad='',telefono=''):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__direccion = direccion
        self.__localidad = localidad
        self.__telefono = telefono
        self.__carreras = []
    #GET - Codigo
    def getCodigo(self): return self.__codigo
    #GET - Nombre
    def getNombre(self): return self.__nombre
    #GET - Direccion
    def getDireccion(self): return self.__direccion
    #GET - Localidad
    def getLocalidad(self): return self.__localidad
    #GET - Telefono
    def getTelefono(self): return self.__telefono
    #Add Carrera
    def addCarrera(self,codigo,nombre,titulo,duracion,grado):
        self.__carreras.append(Carrera(codigo,nombre,titulo,duracion,grado))
    #Get Carreras
    def getNameCarreras(self):
        for carrera in self.__carreras:
                    print(carrera.getCodigo(),carrera.getNombre(),carrera.getTitulo(),carrera.getDuracion(),carrera.getGrado())
    #Search Carreras
    def searchCarrera(self,name):
        i = 0
        found = False
        while i < len(self.__carreras):
            if self.__carreras[i].getNombre() == name:
                print('\nCodigo facultad: {} Codigo Carrera: {}\t{} Localidad: {}'.format(self.__codigo,self.__carreras[i].getCodigo(),self.__nombre,self.__localidad))
                found = True
                i = len(self.__carreras)
            i += 1
        return found