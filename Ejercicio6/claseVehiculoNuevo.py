from claseVehiculo import Vehiculo

class VehiculoNuevo(Vehiculo):
    __version = ''

    def __init__(self,modelo, cantP, color, precioB, marca, version):
        super().__init__(modelo, cantP, color, precioB, marca)
        self.__version = version

    def calcPrecioVenta(self):
        precioBase = super().getPbase()
        importe = precioBase*(1 + 0.1)
        if self.__version == 'full':
            importe += 0.02*precioBase
        return round(importe,1)
    
    def getVersion(self):
        return self.__version
    
    def toJSON(self):
        d = dict(
            __class__= self.__class__.__name__,
            __atributos__ = None)
        #Atributos de la clase padre
        dPadre = super().toJSON()
        #Agrego los atributos de la clase hijo
        dPadre['version'] = self.__version
        d['__atributos__'] = dPadre
        return d