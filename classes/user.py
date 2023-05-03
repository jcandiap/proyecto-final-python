import getpass
import time
from utils.file_manager import FileManager

class UserModel:
    def __init__(self, name:str, last_name:str, email:str, password:str):
        self.name = name
        self.last_name = last_name
        self.email = email
        self.password = password
        
    def to_dict(self):
        return {
            "name": self.name,
            "last_name": self.last_name,
            "email": self.email,
            "password": self.password
        }

class UserController:
    user_list: list[UserModel] = []
    
    def __init__(self):
        self.model = UserModel
        self.file_manager = FileManager('users.json')
        
    def get_users(self):
        returned_list = self.file_manager.get_registers(is_print_exception=True)
        UserController.user_list = returned_list;
        
    def save_user(self, name:str, last_name:str, email:str, password:str):
        new_user = self.model(name, last_name, email, password)
        self.file_manager.save(new_user.to_dict())
        
    def login(self, email:str, password:str) -> UserModel | None:
        UserController().get_users()
        for user in UserController().user_list:
            if user['email'] == email and user['password'] == password:
                return user
        return None
    
class UserView:
    def register_user():
        print('*************************************')
        print('        Ingreso de usuario:')
        print('*************************************\n')
        try:
            name = input('Ingrese el nombre de usuario:')
            last_name =  input('Ingrese su apellido:')
            email = input('Ingrese su correo electronico:')
            password = input('Ingrese su contraseña:')
            UserController().save_user(name, last_name, email, password)
            print(f'\nUsuario ${ name } registrado con exito!')
            time.sleep(5)
        except Exception as e:
            print(f'Error al registar usuario: [{ e }]')
            time.sleep(3)
            
    def list_users():
        try:
            print('*************************************')
            print('        Usuarios registrados:')
            print('*************************************\n')
            UserController().get_users()
            for index, user in enumerate(UserController().user_list):
                print(f'{ index + 1 }.- USUARIO [{ user["name"] }] / PASSWORD [{ user["password"] }]')
            input('\nPresione la tecla [ENTER] para continuar...')
        except Exception as e:
            print('No hay usuarios registrados..')
            time.sleep(3)
            
    def login():
        try:
            print('*************************************')
            print('               Login:')
            print('*************************************\n')
            user_email = input('Ingrese el email: ')
            user_password = input('Ingrese la contraseña: ')
            user:UserModel = UserController().login(user_email, user_password)
            if user == None:
                print('\nCredenciales no validas!')
                time.sleep(3)
                return
            print(f"\nUsuario logeado con exito! Bienvenido [{ user['name'] } { user['last_name'] }]")
            time.sleep(3)
        except Exception as e:
            print(f'Error en login [{ e }]')
            time.sleep(3)