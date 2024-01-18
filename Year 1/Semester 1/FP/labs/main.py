import rezolvari

suma = []


def citire(v):
    print("Introduceti un numar natural nenul: ")
    n = int(input())
    if n < 1:
        print("Introdu un numar natural nenul!!")
        exit()
    print("Introduceti un sir de numere: ")
    for i in range(0, n):
        x = int(input())
        v.append(x)
    sume_partiale(v)


def sume_partiale(v):
    s = 0
    n = len(v)
    for i in range(0, n):
        s = s + v[i]
        suma.append(s)


def run():
    v = []
    commands = {
        "1": citire,
        "2": rezolvari.lista_egale,
        "3": rezolvari.P13,
        "4": rezolvari.P16
    }
    while True:
        print("")
        print("Intoduceti un numar din lista de mai jos")
        print("1. Citire")
        print("2. Secventa de lungime egala")
        print("3. Secventa maxima de suma 5")
        print("4. Secventa cu aceleasi cifre in baza 10")
        print("5. Iesire")
        print("")
        cmd = input()
        if cmd == "5":
            exit()
        if cmd in commands:
            commands[cmd](v)
        else:
            print("Comanda invalida!")


def main():
    run()
    rezolvari.test_egale()
    rezolvari.test_suma_elem_cinci()
    rezolvari.test_baza_zece()


main()
