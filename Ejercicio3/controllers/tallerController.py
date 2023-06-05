from controllers.inscripcionController import InscripcionController
from controllers.personaController import PersonaController
from classes.persona import Persona
from classes.inscripcion import Inscripcion
from os.path import dirname,join
import csv

class TallerController:
    def __init__(self,list=[]):
        self.__list = list
        self.__inscripciones = InscripcionController()
        self.__personas = PersonaController()
    
    def __listaTalleres(self):
        for a in self.__list:
            print(a.getId(),' - ',a.getNombre())
    #Registrar a una persona
    def __registrarPersona(self):
        nombre = input('Ingresar nombre:\t')
        direccion = input('Ingresar direccion:\t')
        dni = int(input('Ingresar DNI:\t'))
        persona = Persona(nombre,direccion,dni)
        self.__personas.addPersona(persona)
        return persona
    #Inscribir una persona a un taller
    def inscripcion(self):
        self.__listaTalleres()
        codigo = int(input('Ingresar codigo de taller:\t'))
        if ((codigo-1) < len(self.__list)):
            if self.__list[codigo-1].consultarVacante():
                persona = self.__registrarPersona()
                inscripcion = Inscripcion('28/05/2023',False,persona,self.__list[codigo-1])
                self.__list[codigo-1].addInscripcion(inscripcion)
                self.__inscripciones.addInscripcion(inscripcion)
                print('\nInscripcion realizada')
            else: print('\nNo hay vacantes disponibles para este taller')
        else: print('\nEl codigo ingresado no pertenece a un taller')
    #Verificar el estado de inscripcion
    def estadoInscripcion(self):
        self.__inscripciones.verificarPagos()
    #Informacion de inscriptos a un taller
    def alumnosInscriptos(self):
        self.__listaTalleres()
        codigo = int(input('Ingresar codigo de taller:\t'))
        if ((codigo-1) < len(self.__list)):
            self.__list[codigo-1].inscripciones()
        else: print('El codigo ingresado no pertenece a un taller')
    #Registrar Pago
    def registrarPago(self):
        self.__inscripciones.pagarInscripcion()
    def guardarInscripciones(self):
        data = self.__inscripciones.getInscripciones()
        with open(join(dirname(__file__),'inscripciones.csv'),'w',newline='') as file:
            writer = csv.writer(file,delimiter=';')
            writer.writerows(data)
        file.close()