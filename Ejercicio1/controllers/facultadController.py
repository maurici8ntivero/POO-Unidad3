class ManejaFacultades:
    __facultades = []
    def __init__(self,list = []):
        self.__facultades = list
    #Facultad Informacion
    def informacionFacultad(self):
        codigo = input('Ingresar codigo de facultad:\t')
        i = 0
        while i < len(self.__facultades):
            if self.__facultades[i].getCodigo() == codigo:
                print('\n{}\n'.format(self.__facultades[i].getNombre()))
                self.__facultades[i].getNameCarreras()
                i = len(self.__facultades)
            i += 1
    #Buscar Carrera
    def informacionCarrera(self):
        name = input('Ingresar nombre de la carrera:\t')
        i = 0
        flag = False
        while i < len(self.__facultades):
            flag = self.__facultades[i].searchCarrera(name)
            if flag: i = len(self.__facultades)
            i += 1
        if flag == False: print('Carrera no encontrada')