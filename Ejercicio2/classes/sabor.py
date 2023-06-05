class Sabor:
    def __init__(self,id=0,nombre='',ingredientes=''):
        self.__id = id
        self.__nombre = nombre
        self.__ingredientes = ingredientes
    #GET - id
    def getId(self): return self.__id
    #GET - Nombre
    def getNombre(self): return self.__nombre
    #GET - Ingredientes
    def getIngredientes(self): return self.__ingredientes