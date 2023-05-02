from IPython.display import clear_output
import sys, subprocess, os

def clear_screen():
    operating_system = sys.platform
    if 'COLAB_GPU' in os.environ:
      clear_output(wait=True)
    elif operating_system == 'linux':
      subprocess.run('clear', shell = True)
    elif operating_system == 'win32' or operating_system == 'cywin':
        subprocess.run('cls', shell = True)
    elif operating_system == 'darwin':
        subprocess.run('clear', shell = True)