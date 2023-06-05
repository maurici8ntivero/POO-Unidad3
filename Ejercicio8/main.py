import csv
from claseManejadorEmpleados import ManejadorEmpleados
from claseLogin import Login
from claseMenu import Menu
from claseIGerente import IGerente
from claseITesorero import ITesorero

def leerArchivo(nomArchivo,manejador):
    archivo = open(nomArchivo)
    reader = csv.reader(archivo,delimiter=';')
    bandera = False
    for fila in reader:
        if not bandera:
            bandera = True
        else:
            if nomArchivo == 'planta.csv':
                manejador.crearEmpleadoPlanta(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5]) 
            elif nomArchivo == 'contratados.csv':
                manejador.crearEmpleadoContratado(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6])
            elif nomArchivo == 'externos.csv':
                manejador.crearEmpleadoExterno(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6],fila[7],fila[8],fila[9])                        
    archivo.close()

def tesorero(manejarTesorero):
    dni = input('Ingrese DNI de empleado: ')
    manejarTesorero.gastosSueldoPorEmpleado(dni)

def gerente(manejarGerente):
    menuGerente = Menu()
    menuGerente.define_menu('OPCIONES PARA GERENTE',[
        '[1]- Modificar sueldo básico emplado de planta',
        '[2]- Modificar pago por hora empleado contratado',
        '[3]- Modificar viatico de empleado externo',
        '[0]- Volver al menu principal'])
    menuGerente.showMenu()
    op2 = menuGerente.selectOption()
    while op2 != 0:
        if op2 == 1:
            dni = input('Ingrese DNI de empleado de planta: ')
            basico = input('Ingrese nuevo sueldo basico: ')
            manejarGerente.modificarBasicoEPlanta(dni,basico)
        elif op2 == 2:
            dni = input('Ingrese DNI de empleado contratado: ')
            valorHora = input('Ingrese nuevo valor por hora: ')
            manejarGerente.modificarValorEPorHora(dni,valorHora)         
        elif op2 == 3:
            dni = input('Ingrese DNI de empleado externo: ')
            viatico = input('Ingrese nuevo valor de viatico: ')
            manejarGerente.modificarViaticoEExterno(dni,viatico)  
        input('Presione ENTER para continuar...')
        menuGerente.showMenu()
        op2 = menuGerente.selectOption() 

if __name__ == '__main__':
    #Cantidad de los empleados en archivos: 45
    print('Iniciando sistema.')
    print('Ingrese cantidad TOTAL de empleados')
    print('Nota: Si la cantidad es inferior a los empleados cargados en archivos, se leeran todos los empleados')
    cant = input('--> ')
    while not cant.isdigit():
        print('Error: El numero debe ser entero. Reintente')
        cant = input('--> ')
    empleados = ManejadorEmpleados(int(cant))
    miLogin = Login()

    leerArchivo('planta.csv',empleados)
    leerArchivo('contratados.csv',empleados)
    leerArchivo('externos.csv',empleados)

    miMenu = Menu()
    miMenu.define_menu('Menu de opciones',[
            '[1]- Registrar horas',
            '[2]- Monto total de tarea',
            '[3]- Lista beneficiarios ayuda',
            '[4]- Calcular sueldos',
            '[5]- Funcionalidad para Tesorero',
            '[6]- Funcionalidades para Gerente',
            '[7]- Cambiar usuario',
            '[8]- Cerrar sesión',
            '[0]- Salir'])

    miMenu.showMenu('Usuario: {0}'.format(miLogin.getNivel().upper()))
    op = miMenu.selectOption() 
    while op != 0:          
        #Registrar horas:
        if op == 1:
            dni = input('Ingrese DNI de empleado contratado: ')
            empleados.cambiarHorasEmpC(dni)
            input('Presione ENTER para continuar...')
        #Total de tarea
        elif op == 2:
            empleados.totalTarea()
        #Ayuda
        elif op == 3:
            empleados.listBeneficiarios()
            input('Presione ENTER para continuar...')
        #Calcular sueldo
        elif op == 4:
            empleados.listarEmpleados()
            input('Presione ENTER para continuar...')
        
        #Opciones para gerente y tesorero
        elif op == 5:
            nivel = miLogin.getNivel()
            if nivel == 'tesorero':
                #Restriccion a métodos exclusivos de ITesorero
                tesorero(ITesorero(empleados))
            else:
                print('ACCESO DENEGADO.')
                print('Ejecutar esta funcionalidad requiere loguearse como TESORERO.')
            input('Presione ENTER para continuar...')
        elif op == 6:
            nivel = miLogin.getNivel()
            if nivel == 'gerente':
                #Restriccion a métodos exclusivos de IGerente
                gerente(IGerente(empleados))                                       
            else:
                print('ACCESO DENEGADO.')
                print('Ejecutar esta funcionalidad requiere loguearse como GERENTE.')
                input('Presione ENTER para continuar...')
        elif op == 7:
            #Cambio el usuario
            miLogin.login()
            input('Presione ENTER para continuar...')
        elif op == 8:
            #Cierro sesion con el usuario actual
            miLogin.cerrarSesion()
            input('Presione ENTER para continuar...')
     
        miMenu.showMenu('Usuario: {0}'.format(miLogin.getNivel().upper()))
        op = miMenu.selectOption() 




