from exceptions.erori import ValidError
from exceptions.erori import RepoError
from business.service_studenti import srv_adauga_lista
from domain.student import to_str_stud


def ui_adauga_stud(l):
    id_stud = int(input("id stud: "))
    nume = input("nume: ")
    val = float(input("valoare: "))
    srv_adauga_lista(l,id_stud,nume,val)

def ui_print_studs(l):
    if len(l) == 0:
        print("lista de studenti goala")
    for stud in l:
        print(to_str_stud(stud))


def run():
    l = []
    while True:
        cmd = input(">>>")
        if cmd == "exit":
            return
        if cmd == "":
            continue
        if cmd == "add_stud":
            try:
                ui_adauga_stud(l)
            except ValueError:
                print("valoare numerica invalida!\n")
            except ValidError as ve:
                print("valid error: " + str(ve))
            except RepoError as re:
                print("repo error: " + str(re))
        if cmd == "print_stud":
            ui_print_studs(l)
        else:
            print("comanda invalida!\n")