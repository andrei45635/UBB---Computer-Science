# backtracking recursiv
# Generați toate sub-secvențele de lungime 2n+1, formate din 0, -1 și 1, astfel încât a1 = 0, ...,
# a2n+1 = 0 și |a(i+1) - ai| = 1 sau 2, pentru orice i, 1 <= i <= 2n.


def consistent(lista):
    # verify if the subset starts and ends with 0
    for i in range(0, len(lista)):
        if (abs(lista[i] - lista[i - 1]) == 1 or abs(lista[i] - lista[i - 1])) == 2:
            return True
    return False


def consistent2(sublista):
    for i in range(0, len(sublista) - 1):
        if sublista[i] == sublista[i + 1]:
            return False
    return True


def consistent_last(sublista):
    for i in range(len(sublista)):
        if sublista[0] != 0 or sublista[-1] != 0:
            return False
    return True


def solution(lista):
    if len(lista) % 2 != 0 and len(lista) > 1:
        return True


def solutionFound(result_lista):
    print(result_lista)


def BackRec(lista, index, sublista):
    """
    Generare sub-secvente
    :param lista: lista = (lista0,lista1,...,lista2n+1)
    :param index: index = 0
    :param sublista: sublista
    :return:
    """
    if index == len(lista):
        for i in range(len(lista)//10):
            if consistent(lista) and consistent2(sublista) and consistent_last(sublista) and solution(sublista):
                solutionFound(sublista)
    else:
        BackRec(lista, index + 1, sublista)
        BackRec(lista, index + 1, sublista + [lista[index]])
