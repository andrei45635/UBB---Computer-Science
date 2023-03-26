from datetime import datetime
import datetime
from domain.pachet import srv_adauga_pachet_in_lista
from domain.pachet import to_str_pachet
from repo.stergeri import sterge_pret
from repo.stergeri import sterge_zile
from repo.stergeri import sterge_pachet_dest
from repo.rapoarte import numar_oferte
from repo.rapoarte import medie_pret
from repo.rapoarte import tiparire_pachete_perioada_pret
from repo.cautari import cautare_pret_dest
from repo.cautari import cautare_pachet_valid
from repo.cautari import filtrare_data_s
from repo.filtrari import sterge_luna
from repo.filtrari import eliminare_pret_dest
from utils.printing import print_lst_m
from utils.printing import print_lst_n
from utils.printing import print_lst_nou


def ui_eliminare_pret_dest(l, lst_m):
    dest_input = str(input("Introduceti destinatia: "))
    try:
        pret_input = float(input("Introduceti pretul aici: "))
    except ValueError:
        print("pret introdus gresit!")
        return
    eliminare_pret_dest(l, dest_input, pret_input, lst_m)
    print_lst_m(lst_m)


def ui_cauatare_pret_dest(l, lst_n):
    dest_input = str(input("Introduceti destinatia: "))
    try:
        pret_input = float(input("Introduceti pretul aici: "))
    except ValueError:
        print("pret introdus gresit!")
        return
    cautare_pret_dest(l, pret_input, dest_input, lst_n)
    print_lst_n(lst_n)


def ui_cautare_valid(l, lst_n):
    try:
        data_i_user = input("Introduceti data de inceput in formatul dd-mm-yyyy: ")
        data_i_user = datetime.datetime.strptime(data_i_user, "%d-%m-%Y").date()
        data_s_user = input("Introduceti data de sfarsit in formatul dd-mm-yyyy: ")
        data_s_user = datetime.datetime.strptime(data_s_user, "%d-%m-%Y").date()
    except ValueError:
        print("date numerice invalide!")
        return
    cautare_pachet_valid(l, data_i_user, data_s_user, lst_n)
    print_lst_n(lst_n)


def ui_adauga_pachet(l):
    try:
        data_i = input("Introduceti data de inceput in formatul dd-mm-yyyy: ")
        data_i = datetime.datetime.strptime(data_i, "%d-%m-%Y").date()
        data_s = input("Introduceti data de sfarsit in formatul dd-mm-yyyy: ")
        data_s = datetime.datetime.strptime(data_s, "%d-%m-%Y").date()
    except ValueError:
        print("date numerice invalide!")
        return
    dest = input("Introduceti destinatia aici: ")
    try:
        pret = float(input("Introduceti pretul aici: "))
    except ValueError:
        print("pret invalid!")
        return
    srv_adauga_pachet_in_lista(l, data_i, data_s, dest, pret)


def ui_print_pachet(l):
    for pachet in l:
        print(to_str_pachet(pachet))
    if len(l) == 0:
        print("comanda invalida!")


def ui_modifica_date(l):
    print("Pachete introduse pana acum: ")
    for el, pachet in enumerate(l, start=1):
        print(f"{el}.{pachet}")
    alegere_mod = int(input("alegeti ce pachet vreti sa modificati: "))
    print("Se va modifica pachetul: ", alegere_mod, l[alegere_mod - 1])
    l.remove(l[alegere_mod - 1])
    ui_adauga_pachet(l)


def ui_sterge_pachet_dest(l, undolist):
    if len(l) == 0:
        print("nu exista niciun pachet de sters")
    else:
        user_input = str(input("Introduceti destinatia pachetului pe care vreti sa il stergeti: "))
        print("Se vor sterge pachetele cu destinatia: ", user_input)
        sterge_pachet_dest(l, user_input, undolist)


def ui_sterge_zile(l,undolist):
    if len(l) == 0:
        print("nu exista niciun pachet de sters")
    else:
        user_input = int(input("Introduceti zilele pachetului pe care vreti sa il stergeti: "))
        print("Se vor sterge pachetele cu numarul de zile mai mic decat : ", user_input)
        sterge_zile(l, user_input,undolist)


def ui_sterge_pret(l,undolist):
    if len(l) == 0:
        print("nu exista niciun pachet de sters")
    else:
        user_input = float(input("Introduceti pretul pachetului pe care vreti sa il stergeti: "))
        print("Se vor sterge pachetele care au pretul mai mare decat: ", user_input)
        sterge_pret(l, user_input,undolist)
        print("Lista pachetelor care nu au fost sterse este", l)


def ui_numar_oferte(l):
    if len(l) == 0:
        print("Nu a fost introdus niciun pachet!")
    else:
        numar_oferte(l)


def ui_medie_pret(l):
    if len(l) == 0:
        print("Nu a fost introdus niciun pachet!")
    else:
        dest_user_i = str(input("Introduceti destinatia pe care vreti sa o cautati aici: "))
        print("Media pretului este ", medie_pret(l, dest_user_i))


def ui_eliminare_luna(l,lst_m):
    if len(l) == 0:
        print("Nu a fost introdus niciun pachet!")
    else:
        user_input = int(input("Introduceti luna pachetelor pe care vreti sa le stergeti: "))
        sterge_luna(l, user_input,lst_m)
        print_lst_m(lst_m)
        print("Au fost sters(e) pachetele")


def ui_tiparire_data_s(l,lst_n):
    if len(l) == 0:
        print("Nu a fost introdus niciun pachet!")
    else:
        user_input = input("Introduceti data de final pe care ati vrea sa o stergeti in formatul DD-MM-YYYY: ")
        data_s_input = datetime.datetime.strptime(user_input, "%d-%m-%Y").date()
        filtrare_data_s(l, data_s_input,lst_n)
        print_lst_n(lst_n)


def ui_tiparire_pachete_perioada_pret(l,lst_nou):
    if len(l) == 0:
        print("Nu a fost introdus niciun pachet!")
    else:
        try:
            data_i_user = input("Introduceti data de inceput in formatul DD-MM-YYYY: ")
            data_i_user = datetime.datetime.strptime(data_i_user, "%d-%m-%Y").date()
            data_s_user = input("Introduceti data de sfarsit in formatul DD-MM-YYYY: ")
            data_s_user = datetime.datetime.strptime(data_s_user, "%d-%m-%Y").date()
        except ValueError:
            print("date numerice invalide!")
            return
    tiparire_pachete_perioada_pret(l, data_i_user, data_s_user,lst_nou)
    print_lst_nou(lst_nou)

