import numpy as np
class Helado:
    def __init__(self,gramos=0,precio=0):
        self.__gramos = gramos
        self.__precio = precio
        self.__sabores = []
    #Get gramos
    def getGramos(self): return self.__gramos
    #Get precio
    def getPrecio(self): return self.__precio
    #Add sabores
    def addSabor(self,sabor):
        self.__sabores.append(sabor)
    #Get sabores
    def getSabores(self):
        codigos = np.full(len(self.__sabores),0)
        i = 0
        for sabor in self.__sabores:
            codigos[i]= sabor.getId() - 1
            i += 1
        return codigos
    