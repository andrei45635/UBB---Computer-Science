from domain.pachet import get_destinatie
from domain.pachet import get_pret
from domain.pachet import get_data_i
from domain.pachet import get_data_s


def medie_pret(l, dest_user_i):
    # functie ce returneaza media de pret pentru o destinatie data
    suma_pret = 0
    nr_dest = 0
    for _pachet in l:
        if get_destinatie(_pachet) == dest_user_i:
            suma_pret += get_pret(_pachet)
            nr_dest += 1
        if nr_dest == 0:
            return get_pret(_pachet)
    try:
        return float(suma_pret / nr_dest)
    except ZeroDivisionError:
        print("Date introduse gresit!\n")


def numar_oferte(l):
    # functie care calculeaza numarul de oferte pentru o locatie data
    nr_oferte = 0
    dest_input = str(input("Introduceti destinatia pe care vreti o sa cautati aici: "))
    for _pachet in l:
        if get_destinatie(_pachet) == dest_input:
            nr_oferte += 1
    print("Numarul de oferte pentru destinatia ", dest_input, "este ", nr_oferte)


def tiparire_pachete_perioada_pret(l, data_i_user, data_s_user, lst_nou):
    # functie care returneaza pachetele disponibile intr-o anumita perioada citita de la tastatura in ordinea
    # crescatoare a pretului
    lst = [pachet for pachet in l if (get_data_i(pachet) >= data_i_user and get_data_s(pachet) <= data_s_user)]
    lst_nou.append(sorted(lst, key=lambda x: x[3]))