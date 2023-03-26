def back_iter(sol, dim):
    """
    Generare sub-secvente
    :param sol: lista=(lista0,lista1,...,lista2n+1)
    :param dim: 2n+1
    :return: sol
    """
    def valid(lista, dom):
        try:
            lista = [dom[el] for el in lista]
        except IndexError:
            return False
        if lista[-1] != "0" and len(lista) == 2*dim+1:
            return False
        for el in range(0, len(lista)-1):
            if lista[el] == lista[el+1]:
                return False
            if lista[0] != "0":
                return False
        return True

    domeniu = "0", "1", "-1"
    sol.append(-1)
    while len(sol) > 0:
        chosen = False
        while not chosen and sol[-1] < 3:
            sol[-1] = sol[-1] + 1
            chosen = valid(sol, domeniu)

        if chosen:
            if len(sol) == 2*dim+1:
                print('[' + ", ".join(domeniu[el] for el in sol) + ']')
            else:
                sol.append(-1)
        else:
            sol = sol[:-1]