def print_lst_nou(lst_nou):
    for _pachet in lst_nou:
        print(lst_nou)


def print_lst_n(lst_n):
    for entry in lst_n:
        attributes = entry.split('\n')
        for attribute in attributes:
            name, value = attribute.split(': ')
            print(f"{name}: {value}")
    #for _ in lst_n:
        #print(lst_n)


def print_lst_m(lst_m):
    for _ in lst_m:
        print(lst_m)
