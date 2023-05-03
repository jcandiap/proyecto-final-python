import os
from pathlib import Path
import time
import json

class FileManager:
    def __init__(self, file_name):
        self.file_name = file_name
        
    def __get_base_dir(self):
        if 'COLAB_GPU' in os.environ:
            return Path(os.getcwd())
        else:
            return Path(__file__).resolve().parent.parent / 'db'
            
    def save(self, object):
        try:
            full_path = str(self.__get_base_dir()) + '/' + self.file_name
            if os.path.exists(full_path):
                with open(full_path, 'r', encoding='UTF-8') as file:
                    registers = json.load(file)
            else:
                registers = []
            
            registers.append(object)
            
            with open(full_path, 'w') as file:
                json.dump(registers, file)
            
        except Exception as e:
            print(f'Error al abrir el archivo [{ e }]')
            time.sleep(3)
            
    def get_registers(self, is_print_exception = False):
        try:
            full_path = self.__get_base_dir() + self.file_name
            with open(full_path, 'r', encoding='UTF-8') as file:
                return json.load(file)
        except Exception as e:
            if is_print_exception:
                print('No hay registros...')
            return []