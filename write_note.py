def do_note():
    with open('notebook.txt', 'a', encoding= 'utf-8') as file:
        print('Введите фамилию, имя, телефон, описание через "-"')

        st = input('->', )
        st_list = st.split('-')
        while len(st_list) != 4:
            print('Ввели не корректные данные, введите снова')
            st = input('-> ', )
            st_list = st.split('-')
        file.writelines(f'Фамилия - {st_list[0]}, Имя - {st_list[1]}, Телефон - {st_list[2]}, Описание - {st_list[3]}\n')

if __name__ == "__main__":

    do_note()

