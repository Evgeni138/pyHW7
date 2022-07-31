from read_note import read_notes

def del_note():
    print('Введите через пробел Фамилию Имя контакта, который нужно удалить')
    name_delete = input('-> ', )
    lst_delete = name_delete.split()
    lst = read_notes()
    n = len(lst)
    i = 0
    while i < n:
        if lst_delete[0] in lst[i] and lst_delete[1] in lst[i]:
            lst.pop(i)
            n -= 1
            with open('notebook.txt', 'w', encoding='utf-8') as file1:
                for j in lst:
                    file1.write(j)
            with open('notebook1.txt', 'w', encoding='utf-8') as file_ch2:
                lst = read_notes()
                for i in range(len(lst)):
                    st_lst = lst[i]
                    lst_st = st_lst.split(', ')
                    for j in lst_st:
                        file_ch2.writelines(f'{j}\n')
        i += 1
