def e_prim(x):
    #functie care verifica daca numarul intreg x este prim sau nu 
    #Input: x - integer
    #Output: rez - True, daca numarul x este prin 
    #              False, altfel
    if x < 2: 
        return False
    if x == 2:
        return True
    if x % 2 == 0: 
        return False
    d = 3
    while d * d <= x: 
        if x % d ==0:
            return False
        d += 2
    return True

def test_e_prim():
    assert(e_prim(-7)==False)
    assert(e_prim(0)==False)
    assert(e_prim(1)==False)
    assert(e_prim(2))
    assert(e_prim(6)==False)
    assert(e_prim(7))
    assert(e_prim(27)==False)
    assert(e_prim(25)==False)

def afiseaza_meniu():
    print("Aplicatie cu numere prime")
    print("1. Introducere numere naturale in lista")
    print("2. Afisare numere prime din lista")
    print("Pentru a iesi din aplicatie, introduceti comanda exit")

def ui_citire_lista(l):
    while True:
        try:
            nr = int(input(""))
            if nr == -1:
                return
            l.append(nr)
        except ValueError:
            print("valoare numerica invalida!")
        print(type(nr))

def numere_prime(l):
    prime = []
    for x in l:
        if e_prim(x):
            prime.append(x)
    return prime

def ui_afisare_prime(l):
    print("Intrat afisare prime")
    prime = numere_prime(l)
    s = " "
    for x in prime:
        s += str(x) + " "
    print(s)

def run():
    l = []
    while True:
        afiseaza_meniu()
        cmd = input(">>>")
        if cmd == "exit":
            return  
        if cmd == "1":
            ui_citire_lista(l)
        elif cmd == "2":
            ui_afisare_prime(l)
        else:
            print("comanda invalida!")

def main():
    test_e_prim()
main()
