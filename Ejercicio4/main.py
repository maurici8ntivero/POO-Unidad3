from colorama import init,Fore
from menu import main_menu,clearConsole
from controllers.empleadoController import EmpleadoController

controller = EmpleadoController()
controller.loadCsv('utils/planta.csv')
controller.loadCsv('utils/contratados.csv')
controller.loadCsv('utils/externos.csv')
option = None
flag = True

while flag:
    main_menu()
    option = int(input(Fore.LIGHTGREEN_EX+'\tSeleccionar una opcion:\t'+Fore.RESET))
    if option == 1: controller.registrarHoras()
    if option == 2: controller.montoTarea()
    if option == 3: controller.ayudaEconomica()
    if option == 4: controller.calcularSueldo()
    if(option != 1 and option != 2 and option != 3 and option != 4 and option != 9):
        print(Fore.RED+'Ingresa una de las opciones disponibles.'+Fore.RESET)
        input()
        clearConsole()
    elif option == 9 :
        flag = False
        clearConsole()
    else: 
        input()
        clearConsole()