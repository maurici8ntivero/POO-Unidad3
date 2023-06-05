import os
from colorama import Fore, Back, Style

def main_menu():
    print('*****************************************')
    print('*' + Fore.BLUE+Style.BRIGHT + '\tEjercicio 4' + Style.RESET_ALL + '\n*')
    print('*\t 1)Registrar horas (Empleados Contratados)')
    print('*\t 2)Total de tarea (Empleados Externos)')
    print('*\t 3)Ayuda economica')
    print('*\t 4)Ver sueldos')
    print('*\t 9)Salir\n*')
    print('*****************************************')

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)