class Login():
    __nivel = ''
    def __init__(self,nivel='comun'):
        self.__nivel = nivel

    def login(self):
        header = '+' + '-' * 50 + '+' 
        print(header)
        print('|{0:^50}|'.format('AUTENTICAR USUARIO'))
        print(header)
        user = input('Usuario: ')
        passwd = input('Contraseña: ')
        if user.lower() == 'uTesorero'.lower() and passwd == 'ag@74ck':
            self.__nivel = 'tesorero'

            print('Se ha logueado como {0}'.format(self.__nivel.upper()))
        elif user.lower() == 'uGerente'.lower() and passwd == 'ufC77#!1':
            self.__nivel = 'gerente'
            print('Se ha logueado como {0}'.format(self.__nivel.upper()))
        else:
            print('Usuario y/o contraseña no reconocidos.')
            print('Continua logueado como {0}'.format(self.__nivel.upper()))
        
    def cerrarSesion(self):
        if self.__nivel != 'comun':
            print('Ha cerrado sesion con el usuario {0}'.format(self.__nivel.upper()))
            self.__nivel = 'comun'
        else:
            print('Ya ha cerrado sesion.')

        return self.__nivel
    
    def getNivel(self):
        return self.__nivel