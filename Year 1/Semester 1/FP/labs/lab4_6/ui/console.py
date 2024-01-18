from lab4_6.ui.interface import *
from lab4_6.utils.undo import undo


def afiseaza_meniu():
    print("Aplicatie pentru o agentie de turism\n")
    print("1) adauga pachet in lista")
    print("2) modifica pachetul din lista")
    print("3) afiseaza pachetele din lista")
    print("4) sterge pachetele care au o destinatie data de user")
    print("5) sterge pachetele care au un numar de zile mai mic decat introduce utilizatorul")
    print("6) sterge pachetele care au un pret mai mare decat user input")
    print("7) printeaza numarul de oferte pentru o destinatie anume")
    print("8) printeaza media de pret pentru o destinatie data")
    print("9) filtreaza pachetele care contin luna pe care userul o inputeaza")
    print("10) tipareste pachetele cu o anumita data de sfarsit")
    print("11) tipareste pachetele cu o destinatie data si cu un pret mai mic decat o suma data")
    print("12) filtreaza pachetele cu o destinatie diferita de cea data si cu un pret mai mare decat o suma data ")
    print("13) tipareste pachetele care se incadreaza intr-un sejur introdus de utilizator")
    print(
        "14) tipareste pachetele in ordinea crescatoare a pretului disponibile intr-o anumita perioada citita de la "
        "utilizator")
    print("//: undo")
    print("exit: iesire din aplicatie\n")


def run():
    l = []
    lst_n = []
    lst_m = []
    undolist = []
    lst_nou =[]
    while True:
        afiseaza_meniu()
        cmd = input(">>>")
        if cmd == "exit":
            return
        if cmd == " ":
            continue
        if cmd == "1":
            try:
                ui_adauga_pachet(l)
            except Exception as ex:
                print(ex)
        elif cmd == "2":
            try:
                ui_modifica_date(l)
            except ValueError:
                print("date numerice invalide!")
        elif cmd == "3":
            ui_print_pachet(l)
        elif cmd == "4":
            ui_sterge_pachet_dest(l, undolist)
        elif cmd == "5":
            ui_sterge_zile(l,undolist)
        elif cmd == "6":
            ui_sterge_pret(l,undolist)
        elif cmd == "7":
            ui_numar_oferte(l)
        elif cmd == "8":
            ui_medie_pret(l)
        elif cmd == "9":
            ui_eliminare_luna(l,lst_m)
        elif cmd == "10":
            ui_tiparire_data_s(l,lst_n)
        elif cmd == "11":
            ui_cauatare_pret_dest(l, lst_n)
        elif cmd == "12":
            ui_eliminare_pret_dest(l, lst_m)
        elif cmd == "13":
            ui_cautare_valid(l, lst_n)
        elif cmd == "14":
            ui_tiparire_pachete_perioada_pret(l,lst_nou)
        elif cmd == "//":
            undo(undolist, l)
        else:
            print("comanda invalida!")
