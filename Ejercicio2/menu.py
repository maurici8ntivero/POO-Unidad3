import os
from colorama import Fore, Back, Style

def main_menu():
    print('*****************************************')
    print('*' + Fore.BLUE+Style.BRIGHT + '\tEjercicio 2 - Heladeria El Conito' + Style.RESET_ALL + '\n*')
    print('*\t 1)Registrar Venta')
    print('*\t 2)Sabores mas pedidos')
    print('*\t 3)Gramos vendidos de un sabor')
    print('*\t 4)Sabores mas vendidos por tipo de helado')
    print('*\t 5)Importe total recaudado por tipo de helado')
    print('*\t 9)Salir\n*')
    print('*****************************************')

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)