import os
import shutil
import sys
import pr_filemngr_path as path
import pandas as pd

opsys = sys.platform
path.create_path()
print("Текущая деректория:", os.getcwd())
top = os.getcwd()

def current_dir():
    print("Текущая деректория:", os.getcwd())

def walk_dir():
    a = []
    for root, dirs, files in os.walk(top):
        for filename in files:
            a.append(filename)
        for d in dirs:
            a.append(d)
    return a

def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print('Папка с таким названием уже есть!')

def delete_folder(name):
    try:
        os.rmdir(name)
    except FileNotFoundError:
        print('Такой папки не существует!')

def change_dir(name):
    try:
        if name == "Обратно":
            if os.getcwd() == top:
                print('Нельзя выходить за пределы рабочей папки')
            else:
                os.chdir("..")
                print(os.getcwd())
        else:
            if name in walk_dir():
                a = os.getcwd()
                if opsys == 'darwin':
                    os.chdir(a+'/'+name)
                elif opsys == 'cygwin' or opsys == 'win32':
                    os.chdir(a+'\\'+name)
                print(os.getcwd())
            else:
                print('Нельзя выходить за пределы рабочей папки')
    except FileNotFoundError:
        if name in walk_dir():
            print('К этой папке нельзя спуститься сразу!')
        else: print('Такой папки не существует!')

def create_write_file(name, text=None):
    with open(name, 'w') as f:
        if text:
            f.write(text)

def write_in_file(name, text):
    try:
        with open(name, 'a') as f:
            f.write(text)
    except FileNotFoundError:
        print('Такого файла не существует!')

def read_file(name):
    try:
        with open(name, 'r') as f:
            data = f.read()
        print(data)
    except FileNotFoundError:
        print('Такого файла не существует!')

def delete_file(name):
    try:
        os.remove(name)
    except FileNotFoundError or PermissionError:
        print('Такого файла не существует!')

def copy_files(file, destination):
    try:
        shutil.copy(file, destination)
    except FileNotFoundError:
        print('Такого файла не существует!')

def move_file(name, name2):
    try:
        shutil.move(name, name2)
    except FileNotFoundError:
        print('Такого файла не существует!')

def rename_file(name, new_name):
    try:
        os.rename(name, new_name)
    except FileNotFoundError:
        print('Такого файла не существует!')

def create_archive(name):
    try:
        shutil.make_archive(f'{name}(archive)', 'zip', name)
    except FileNotFoundError or NotADirectoryError:
        print('Такого папки не существует!')

def open_archive(name,name2):
    try:
        shutil.unpack_archive(name, name2, 'zip')
    except FileNotFoundError:
        print('Такого папки не существует!')

def help_list():
    h = pd.Series({'!H':'help_list', 'Cur_dir': 'current_dir', 'CRFl': 'create_folder', 'DELFl': 'delete_folder', 'Chg_dir': 'change_dir', 'MKF': 'create_write_file',
          'WRTF': 'write_in_file', 'RDF': 'read_file', 'DELF': 'delite_file', 'CPF': 'copy_files', 'MVF': 'move_file',
          'REF': 'rename_file', 'Arch':'create_archive','UnAr':'open_archive'})
    help_list = pd.DataFrame({'Список команд': h})
    print(help_list)
help_list()



