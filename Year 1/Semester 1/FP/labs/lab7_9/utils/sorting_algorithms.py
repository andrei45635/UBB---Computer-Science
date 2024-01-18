def bubble_sort(grades, key=lambda x: x, reverse=False, *, cmp=lambda a, b, r: a > b if r == False else a < b):
    """
    Simple bubble sort implementation
    :param lista: lista care trebuie sortata
    :param key: cheia dupa care se sorteaza
    :param cmp: functia care sorteaza 2 elemente
    :param reverse: False = crescator, True = descrescator
    :return:lista sortata
    """
    for i in range(0, len(grades) - 1):
        for j in range(0, len(grades) - i - 1):
            if cmp(key(grades[j]), key(grades[j + 1]), reverse):
                grades[j], grades[j + 1] = grades[j + 1], grades[j]
    return grades


def shell_sort(lista, key=lambda x: x, reverse=False, *, cmp=lambda a, b: a < b):
    """
    Shell Sort Algorithm - improves the efficiency of insertion sort by comparing elements that are far apart and then progressively reducing the gap between elements to be compared
    :param lista: lista care trebuie sortata
    :param key: cheia dupa care se sorteaza
    :param cmp: functia care sorteaza 2 elemente
    :param reverse: False = crescator, True = descrescator
    :return:lista sortata
    """
    gap = len(lista) // 2
    while gap > 0:
        for i in range(gap, len(lista)):
            temp = lista[i]
            j = i
            while j >= gap and cmp(key(lista[j - gap]), key(temp), reverse):
                lista[j] = lista[j - gap]
                j -= gap
            lista[j] = temp
        gap //= 2
    return lista


def mycmp(x, y):
    if x > y:
        return 1
    elif x < y:
        return -1
    elif x == y:
        return 0
