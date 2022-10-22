import praktik_filemanager_func as m
k=''
while k != 'end':
    k = input("Введите команду: ").split()
    if len(k)==0: print("Неверная команда! Введите: !H")
    elif k[0] == 'Cur_dir':
        m.current_dir()
    elif k[0] == '!H':
        m.help_list()
    elif k[0] == 'CRFl':
        m.create_folder(k[1])
    elif k[0] == 'DELFl':
        m.delete_folder(k[1])
    elif k[0] == 'Chg_dir':
        m.change_dir(k[1])
    elif k[0] == 'MKF':
        text = input('Введите данные или нажмите Enter: \n')
        if text == '': text = None
        m.create_write_file(k[1], text)
    elif k[0] == 'WRTF':
        data = input('Введите данные: \n')
        m.write_in_file(k[1], data+'\n')
    elif k[0] == 'RDF':
        m.read_file(k[1])
    elif k[0] == 'DELF':
        m.delete_file(k[1])
    elif k[0] == 'CPF':
        n = input("Куда копируем: ")
        m.copy_files(k[1], n)
    elif k[0] == 'MVF':
        n = input("Куда перемещаем: ")
        m.move_file(k[1], n)
    elif k[0] == 'REF':
        n = input("Новое название: ")
        m.rename_file(k[1], n)
    elif k[0] == 'Arch':
        m.create_archive(k[1])
    elif k[0] == 'UnAr':
        n = input('В какую папку:')
        m.open_archive(k[1], n)
    elif k[0] == 'end': break
    else: print("Неверная команда! Введите: !H")

