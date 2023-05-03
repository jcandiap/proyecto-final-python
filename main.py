import time
from classes.user import UserView
from utils.file_manager import FileManager
import utils.shell_util as shell_util

def cargar_accion(option_selected):
    shell_util.clear_screen()
    if option_selected == 1:
        UserView.register_user()
    elif option_selected == 2:
        UserView.login()
    elif option_selected == 3:
        UserView.list_users()
    return option_selected

def print_options_menu():
    option_selected = 0
    while option_selected != 4:
        shell_util.clear_screen()
        print('*************************************')
        print('        Seleccione una opción:')
        print('*************************************\n')
        print('1.- Registrar usuario')
        print('2.- Logear usuario')
        print('3.- Listar Usuarios')
        print('4.- Salir')
        try:
            option_selected = int(input('\nOpcion:\n'))
            if option_selected > 0 or option_selected <= 3:
                option_selected = cargar_accion(option_selected)
        except:
            print('Debe elegir una opcion valida!')
            time.sleep(3)
    return option_selected

def main():
    option_selected = print_options_menu()
    
main()