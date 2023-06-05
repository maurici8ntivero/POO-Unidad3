import os
from colorama import Fore, Back, Style

def main_menu():
    print('*****************************************')
    print('*' + Fore.BLUE+Style.BRIGHT + '\tEjercicio 3 - Clase asociacion' + Style.RESET_ALL + '\n*')
    print('*\t 1)Inscribirse en un taller')
    print('*\t 2)Consultar Inscripcion')
    print('*\t 3)Consultar Inscriptos en un taller')
    print('*\t 4)Registrar Pago')
    print('*\t 9)Salir\n*')
    print('*****************************************')

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)