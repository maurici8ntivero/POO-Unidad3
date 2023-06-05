from colorama import init,Fore
from menu import main_menu,clearConsole
from controllers.heladoController import ManejadorHelados

init()
controller = ManejadorHelados()
controller.loadInfoSabor()
option = None
flag = True
while flag:
    main_menu()
    option = int(input(Fore.LIGHTGREEN_EX+'\tSeleccionar una opcion:\t'+Fore.RESET))
    if option == 1: controller.registrarVenta()
    if option == 2: controller.saboresMasPedidos()
    if option == 3: controller.gramosVendidos()
    if option == 4: controller.saboresVendidosPorTipoDeHelado()
    if option == 5: controller.importeRecaudadoPorTipoDeHelado()
    if(option != 1 and option != 2 and option != 3 and option != 4 and option != 5 and option != 9):
        print(Fore.RED+'Ingresa una de las opciones disponibles.'+Fore.RESET)
        input()
        clearConsole()
    elif option == 9 :
        flag = False
        clearConsole()
    else: 
        input()
        clearConsole()