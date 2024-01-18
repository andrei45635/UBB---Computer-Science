from lab4_6.utils.verificari import verifica_zile
from lab4_6.utils.verificari import verifica_dest
from lab4_6.utils.verificari import verifica_pret
from lab4_6.utils.undo import clona_lista


def sterge_pret(l, user_input,undolist):
    # functie care sterge pachetele care au un pret mai mare decat user_input
    undolist.append(clona_lista(l))
    l[:] = [pachet for pachet in l if not (verifica_pret(pachet, user_input))]
    return l


def sterge_pachet_dest(l, user_input, undolist):
    # functie care sterge pachetele cu aceeasi destinatie ca si user_input
    undolist.append(clona_lista(l))
    l[:] = [pachet for pachet in l if not (verifica_dest(pachet, user_input))]
    return l


def sterge_zile(l, user_input, undolist):
    # functie care sterge pachetele cu acelasi numar de zile ca si user_input
    undolist.append(clona_lista(l))
    l[:] = [pachet for pachet in l if not (verifica_zile(pachet, user_input))]
    return l

