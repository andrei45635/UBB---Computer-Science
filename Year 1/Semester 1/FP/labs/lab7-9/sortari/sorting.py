def insertion_sort(lista, key=lambda x: x, reverse=False, *, cmp=lambda a, b, r: a > b if r == False else a < b):
    """
    functie care sorteaza o lista utilizand metoda Insertion Sort discutata la curs
    se parcurg elementele
    se inserează elementul curent pe poziția corectă în subsecvența deja sortată.
    În sub-secvența ce conține elementele deja sortate se țin
        elementele sortate pe tot parcursul algoritmului, astfel după ce
        parcurgem toate elementele secvența este sortată în întregime
    :param lista: lista care trebuie sortata
    :param key: cheia dupa care se sorteaza
    :param cmp: functia care sorteaza 2 elemente
    :param reverse: False = crescator, True = descrescator
    :return:lista sortata
    """
    ok = True
    for i in range(1, len(lista)):
        if reverse is False:
            ind = i - 1
            while ind >= 0 and cmp(key(lista[i]),key(lista[ind]),False):
                lista[ind + 1] = lista[ind]
                ind = ind - 1
            lista[ind + 1] = lista[i]
            ok = False
        if reverse is True:
            ind = i - 1
            while ind >= 0 and cmp(key(lista[i]),key(lista[ind]),True):
                lista[ind + 1] = lista[ind]
                ind = ind - 1
            lista[ind + 1] = lista[i]
            ok = False
    if ok is True:
        return lista


def comb_sort(lista, key=lambda x: x, reverse=False, *, cmp=lambda a, b: a < b):
    """
    metoda care sorteaza o lista utilizand metoda Comb Sort
    comb sort este o varianta a bubble sort, doar ca in loc ca gap-ul sa fie 1, acesta este 1.3
    :param lista: lista care trebuie sortata
    :param key: cheia dupa care se sorteaza
    :param cmp: functia care sorteaza 2 elemente
    :param reverse: False = crescator, True = descrescator
    :return:lista sortata
    """
    gap = len(lista)
    swaps = True
    while gap > 1 or swaps:
        gap = max(1, int(gap / 1.3))  # minimum gap is 1
        swaps = False
        for i in range(len(lista) - gap):
            j = i + gap
            if reverse is False:
                if cmp(key(lista[i]), key(lista[j])):
                    lista[i], lista[j] = lista[j], lista[i]
                    swaps = True
            if reverse is True:
                if cmp(key(lista[i]), key(lista[j])):
                    lista[i], lista[j] = lista[j], lista[i]
                    swaps = True
    if swaps is True:
        return lista


def mycmp(x,y):
    if x > y:
        return 1
    elif x < y:
        return -1
    elif x == y:
        return 0
