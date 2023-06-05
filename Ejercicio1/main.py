from colorama import init,Fore
from menu import main_menu,clearConsole
from utils.csvReader import loadFileCSV
from controllers.facultadController import ManejaFacultades

init()
controller = ManejaFacultades(loadFileCSV())
flag = True
option = None
while flag:
    main_menu()
    option = int(input(Fore.LIGHTGREEN_EX+'\tSeleccionar una opcion:\t'+Fore.RESET))
    if option == 1: controller.informacionFacultad()
    if option == 2: controller.informacionCarrera()
    if(option != 1 and option != 2 and option != 9):
        print('Ingresa una de las opciones disponibles.')
        input()
        clearConsole()
    elif option == 9 : 
        flag = False
        clearConsole()
    else: 
        input()
        clearConsole()
