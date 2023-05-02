from utils.file_manager import FileManager

def main():
    file_manager = FileManager('users.json')
    file_manager.save({ 'nombre': 'test' })
    print(file_manager.get_registers())
    
main()