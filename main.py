# - создать папку;
# - удалить (файл/папку);
# - копировать (файл/папку);
# - просмотр содержимого рабочей директории;
# - посмотреть только папки;
# - посмотреть только файлы;
# - просмотр информации об операционной системе;
# - создатель программы;
# - играть в викторину;
# - мой банковский счет;
# - смена рабочей директории (*необязательный пункт);
# - выход.

import os, sys, shutil

while True:
    print('1. создать папку')
    print('2. удалить (файл/папку)')
    print('3. копировать (файл/папку)')
    print('4. просмотр содержимого рабочей директории')
    print('5. посмотреть только папки')
    print('6. посмотреть только файлы')
    print('7. просмотр информации об операционной системе')
    print('8. создатель программы')
    print('9. играть в викторину')
    print('10. мой банковский счёт')
    print('11. смена рабочей директории')
    print('12. выход')

    choice = input('Выберите пункт меню: ')
    if choice == '1':
        os.mkdir(input('Введите имя папки:'))
    elif choice == '2':
        os.remove(input('Введите имя файла/папки:'))
    elif choice == '3':
        shutil.copyfile(input('Введите имя исходного файла/папки:') , input('Введите имя целевого файла/папки:') )
    elif choice == '4':
        # lst = os.listdir('.')
        # for i in range(len(lst)): print(lst[i])
        with os.scandir('.') as files:
            dir = [file.name for file in files]
            for i in range(len(dir)): print(dir[i])
    elif choice == '5':
        with os.scandir('.') as files:
            dir = [file.name for file in files if file.is_dir()]
            for i in range(len(dir)): print(dir[i])
    elif choice == '6':
        with os.scandir('.') as files:
            dir = [file.name for file in files if file.is_file()]
            for i in range(len(dir)): print(dir[i])
    elif choice == '7':
        pass
    elif choice == '8':
        pass
    elif choice == '9':
        pass
    elif choice == '10':
        pass
    elif choice == '11':
        pass
    elif choice == '12':
        break
    else:
        print('Неверный пункт меню')