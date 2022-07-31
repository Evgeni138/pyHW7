# Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.
# под форматами понимаем структуру файлов, например:в файле на одной строке хранится одна часть записи,
# пустая строка - разделитель
# Фамилия_1
# Имя_1
# Телефон_1
# Описание_1
# Фамилия_2
# Имя_2
# Телефон_2
# Описание_2
# и т.д.в файле на одной строке хранится все записи, символ разделитель - ;**
# Фамилия_1,Имя_1,Телефон_1,Описание_1
# Фамилия_2,Имя_2,Телефон_2,Описание_2
# и т.д.
# Предполагается возможность вывода всех контактов, поиска контакта по имени, добавления и удаления контакта


from write_note import do_note
from read_note import read_notes
from delete import del_note

def control():
    choose = ''
    value = ''
    while choose != 'n':
        print('Выберете формат: "1" это формат в одну строку\n'
              '"2" это формат, где все данные будут начинаться с новой строки\n'
              '"n" чтобы выйти из программы\n')
        choose = input('-> ', )
        if choose == 'n':
            print('exit')
            break

        elif choose == '1':
            while value != 'n':
                print('Введите "n", чтобы выйти из программы\n'
                      '"1" чтобы внести новую запись,\n'
                      '"2" чтобы выбрать нужный контакт\n'
                      '"3" чтобы удалить контакт\n'
                      '"4" чтобы посмотреть все контакты')
                value = input()
                if value == 'n':
                    print('exit')
                    break

                elif value == '1':
                    do_note()

                elif value == '2':
                    print('Введите через пробел Имя Фамилию контакта, который нужно вывести на экран')
                    name_print = input('-> ', )
                    lst_print = name_print.split()
                    lst = read_notes()
                    for i in lst:
                        if lst_print[0] in i and lst_print[1] in i:
                            print(i)
                    print()
                    continue

                elif value == '3':
                    del_note()

                elif value == '4':
                    lst = read_notes()
                    for i in lst:
                        print(i.strip())
                    print()

                else:
                    continue


        elif choose == '2':
            with open('notebook1.txt', 'w', encoding='utf-8') as file_ch2:
                lst = read_notes()
                for i in lst:
                    lst_st = i.split(', ')
                    for j in lst_st:
                        file_ch2.writelines(f'{j}\n')

            value2 = ''
            while value2 != 'n':
                print('Введите "n", чтобы выйти из программы\n'
                      '"1" чтобы внести новую запись,\n'
                      '"2" чтобы выбрать нужный контакт\n'
                      '"3" чтобы удалить контакт\n'
                      '"4" чтобы посмотреть все контакты')
                value2 = input('--> ')
                if value2 == 'n':
                    print('exit')
                    break

                elif value2 == '1':
                    do_note()

                elif value2 == '2':
                    print('Введите через пробел Имя Фамилию контакта, который нужно вывести на экран')
                    name_print = input('-> ', )
                    lst_print = name_print.split()
                    lst = read_notes()
                    for i in lst:
                        if lst_print[0] in i and lst_print[1] in i:
                            print_1 = i.split(', ')
                            for j in print_1:
                                print(j)
                    print()

                elif value2 == '3':
                    del_note()

                elif value2 == '4':
                    lst = read_notes()
                    for i in lst:
                        str_lst = i.split(', ')
                        for j in str_lst:
                            print(j)
                    print()
                else:
                    continue
            else:
                continue
