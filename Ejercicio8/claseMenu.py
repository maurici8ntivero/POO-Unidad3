import os
class Menu:
    __opciones = []
    __titulo = ''

    def __init__(self,opciones=[],titulo='MENU'):
        self.__opciones = opciones
        self.__titulo = titulo
  
    def define_menu(self,titulo,opciones):
        self.__titulo = titulo
        self.__opciones = opciones
  
    def selectOption(self):
        op = input('--> ')
        if op.isdigit():
            op = int(op)
            if op > len(self.__opciones) or op < 0:
                input('Opcion invalida, reintente')
                op = None         
        else:
            input('Error: Opcion invalida, debe ingresar un numero entero.')
            op = None
        os.system('cls')
        return op
    
    def showMenu(self,mensaje=''):
        os.system('cls')
        header = '+' + '-'*50 + '+'
        print(header)
        print('|{0:^50}|'.format(self.__titulo))
        print(header)
        if mensaje != '':
            print('| {0:49}|'.format(mensaje))
            print(header)
        for opcion in self.__opciones:
            print('| {0:49}|'.format(opcion))
        print(header)   

               
