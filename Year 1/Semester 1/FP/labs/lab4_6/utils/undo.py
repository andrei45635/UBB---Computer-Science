def clona_lista(l):
    #functie care cloneaza lista pentru a o folosi in undo()
    ll = []
    for x in l:
        nx = x[:]
        ll.append(nx)
    return ll


def undo(undolist, l):
    #functie prin care lista de oferte revine la ce exista inainte de ultima operatie care a modificat lista
    if len(l) == 0:
        print("nu")
    try:
        l[:] = undolist.pop()
    except Exception as ex:
        print(ex)
    return l
