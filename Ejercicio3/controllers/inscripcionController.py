class InscripcionController():
    def __init__(self,list=[]):
        self.__list = list
    def addInscripcion(self,inscripcion):
        self.__list.append(inscripcion)
    def verificarPagos(self):
        dni = int(input('Ingresar DNI:\t'))
        j = 0
        while j < len(self.__list):
            response = self.__list[j].verificarInscripcionPorDNI(dni)
            if response:
                j = len(self.__list)
            j += 1
    def pagarInscripcion(self):
        dni = int(input('Ingresar DNI:\t'))
        j = 0
        while j < len(self.__list):
            if self.__list[j].registrarPago(dni):
                j = len(self.__list)
            j += 1
    def getInscripciones(self):
        iList = []
        for i in self.__list:
            iList.append(i.getInfoInscripcion())
        return iList