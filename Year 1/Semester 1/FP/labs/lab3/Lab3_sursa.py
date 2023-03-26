def lista_egale(lst1):
    """
       Primeste o lista de numere pentru care returneaza
       cea mai lunga secventa de numere egale
    """
    lmax = -1
    numar = 0
    if len(lst1) < 3:
        return False
    for curent in lst1:
        if lst1.count(curent) > lmax:
            lmax = lst1.count(curent)
            numar = curent
    return ' '.join([str(numar)] * lmax)

def test_egale():
    """
    functie test pt lista_egale
    """
    assert lista_egale([1, 2, 2, 2, 4, 5, 6]) == '2 2 2'
    assert lista_egale([2,1]) == False
    assert lista_egale([1, 1, 1, 1, 1, 2, 2, 2, 2]) == '1 1 1 1 1'
    assert lista_egale([-1, -1, -1, -1, -1, 2, 4, 2, 2, 4, 5, 2]) == '-1 -1 -1 -1 -1'

def test_munte():
    """
    functie test pt lista_munte
    """
    assert lista_munte([2, 3, 4, 3, 2]) == True
    assert lista_munte([1,2]) == False
    assert lista_munte([1, 2, 3, 4, 5, 6, 7, 2, 4, 5, 3]) == False
    assert lista_munte([-4,-3,-2,-1,0,-1,-2,-3,-4]) == True

def lista_munte(lst1):
    """
    Primeste o lista de numere pentru care returneaza
    cea mai lunga secventa de tip munte
    """
    if len(lst1) < 3:
        return False
    curent = 1
    while curent < len(lst1) and lst1[curent] > lst1[curent-1]:
        curent += 1
    if curent == 1 or curent == len(lst1):
        return False
    while curent < len(lst1) and lst1[curent] < lst1[curent-1]:
        curent += 1
    return curent == len(lst1)

def afiseaza_meniu():
    print("Aplicatie cu liste")
    print("1. Introduceti lista")
    print("2. Verificati daca lista are o secventa maxima cu numere egale si afisati-o")
    print("3. Verificati daca lista este de tip munte si afisati-o")
    print("4. exit")


def ui_citire_lista():
     input_lista = input("Introduceti numerele ")
     return input_lista.split()

def run():
    global lst1
    lst1 = []
    afiseaza_meniu()
    while True:
        cmd = input(">>>")
        if cmd == "4":
            return
        if cmd == "1":
            lst1 = ui_citire_lista()
        elif cmd == "2":
            print(lista_egale(lst1))
        elif cmd == "3":
            print(lista_munte(lst1))
        else:
            print("comanda invalida")

def main():
    run()
    test_egale()
    test_munte()

main()