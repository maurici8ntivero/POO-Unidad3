from colorama import init,Fore
from menu import main_menu,clearConsole
from utils.csvReader import loadFileCSV
from controllers.tallerController import TallerController
init()
controller = TallerController(loadFileCSV())
option = None
flag = True
while flag:
    main_menu()
    option = int(input(Fore.LIGHTGREEN_EX+'\tSeleccionar una opcion:\t'+Fore.RESET))
    if option == 1: controller.inscripcion()
    if option == 2: controller.estadoInscripcion()
    if option == 3: controller.alumnosInscriptos()
    if option == 4: controller.registrarPago()
    if(option != 1 and option != 2 and option != 3 and option != 4 and option != 9):
        print(Fore.RED+'Ingresa una de las opciones disponibles.'+Fore.RESET)
        input()
        clearConsole()
    elif option == 9 :
        controller.guardarInscripciones()
        flag = False
        clearConsole()
    else: 
        input()
        clearConsole()