def back_rec(sol, dim):
    """
    Generare sub-secvente
    :param sol: lista=(lista0,lista1,...,lista2n+1)
    :param dim: 2n+1
    :return: sol
    """
    def valid(lista):
        if lista[-1] != "0" and len(lista) == 2*dim+1:
            return False
        for el in range(0, len(lista)-1):
            if lista[el] == lista[el+1]:
                return False
            if lista[0] != "0":
                return False
        return True

    domeniu = "0", "1", "-1"
    sol.append(0)
    for el in domeniu:
        sol[-1] = el
        if valid(sol):
            if len(sol) == 2*dim+1:
                print('[' + ", ".join(el for el in sol) + ']')
            elif len(sol) < 2*dim+1:
                back_rec(sol, dim)
    sol.pop(-1)