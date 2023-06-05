class Inscripcion:
    def __init__(self,fecha='',pago=False,persona=object,taller=object):
        self.__fecha = fecha
        self.__pago = pago
        self.__persona = persona
        self.__taller = taller
    #GET - Fecha
    def getFecha(self): return self.__fecha
    #GET - Pago
    def getPago(self): return self.__pago
    #GET - Persona
    def getPersona(self): return self.__persona
    #GET - Taller
    def getTaller(self): return self.__taller
    #Consulta de estado de inscripcion
    def verificarInscripcionPorDNI(self,dni):
        if self.__persona.getDni() == dni:
            print('\nTaller: ',self.__taller.getNombre())
            if self.__pago: print('La inscripcion se encuentra paga')
            else: print('Monto adeudado: $',self.__taller.getMonto())
            return True
        else: return False
    #Informacion de alumnos inscriptos a un taller
    def alumnoInscripcion(self):
        print('{} {}'.format(self.__persona.getNombre(),self.__persona.getDni()))
    #Registrar pago
    def registrarPago(self,dni):
        if self.__persona.getDni() == dni:
            print('\nSUCCESS...\tPago Realizado')
            self.__pago = True
            return True
        else: return False
    #GET - Inscripcion
    def getInfoInscripcion(self):
        dni = self.__persona.getDni()
        idTaller = self.__taller.getId()
        fechaInscripcion = self.__fecha
        pago = self.__pago
        return [dni,idTaller,fechaInscripcion,pago]