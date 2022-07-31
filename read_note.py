def read_notes():
    with open('notebook.txt', 'r', encoding= 'utf-8') as file:
        lst = []
        f = file.readlines()
        for i in f:
            lst.append(i)
    return lst


if __name__ == "__main__":

    read_notes()

