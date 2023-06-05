from datetime import date

from claseVehiculo import Vehiculo

class VehiculoUsado(Vehiculo):
    __patente = ''
    __anio = 0
    __kilometraje= 0

    def __init__(self, modelo, cantP, color, precioB, marca, patente,anio,kilometraje):
        super().__init__(modelo, cantP, color, precioB, marca)
        self.__patente = patente
        self.__anio = anio
        self.__kilometraje = kilometraje
    
    def getPatente(self):
        return self.__patente
    def getAnio(self):
        return self.__anio
    def getKm(self):
        return self.__kilometraje
    
    def calcPrecioVenta(self):
        anioActual = date.today().year
        antiguedad = anioActual - self.__anio
        precioBase = super().getPbase()
        importe = precioBase * (1 - 0.01*antiguedad)
        if self.__kilometraje > 100000:
            importe -= 0.02*precioBase
        return round(importe,1)
    
    def toJSON(self):
        d = dict(
            __class__= self.__class__.__name__,
            __atributos__ = None)
        #Atributos de la clase padre
        dPadre = super().toJSON()
        #Agrego los atributos de la clase hijo
        dPadre['patente'] = self.__patente
        dPadre['anio'] = self.__anio
        dPadre['kilometraje'] = self.__kilometraje
        d['__atributos__'] = dPadre
        return d