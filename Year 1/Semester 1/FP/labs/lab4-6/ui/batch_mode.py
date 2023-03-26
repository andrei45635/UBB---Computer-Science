from domain.pachet import srv_adauga_pachet_in_lista
from repo.stergeri import sterge_zile
from ui.interface import ui_print_pachet
from utils.undo import undo
from datetime import datetime
import datetime


def ui_add_pachet_batch(l, listp):
    if len(listp) != 5:
        print("comanda invalida!")
    else:
        try:
            data_i = listp[1]
            data_i = datetime.datetime.strptime(data_i, "%d-%m-%Y").date()
            data_s = listp[2]
            data_s = datetime.datetime.strptime(data_s, "%d-%m-%Y").date()
        except ValueError:
            print("invalid")
            return
        dest = listp[3]
        try:
            pret = float(listp[4])
        except ValueError:
            print("invalid")
            return
        srv_adauga_pachet_in_lista(l, data_i, data_s, dest, pret)


def ui_sterge_zile_pachet_batch(l, listp, undolist):
    if len(listp) != 2:
        print("comanda invalida")
    else:
        try:
            zile = int(listp[1])
            sterge_zile(l, zile, undolist)
        except ValueError:
            print("invalid")
            return


def run():
    l = []
    undolist = []
    while True:
        cmd = input(">>>")
        if cmd == " ":
            continue
        listc = cmd.split(";")
        for comenzi in listc:
            listp = comenzi.split(" ")
            if listp[0] == "add":
                if len(listp) == 5:
                    try:
                        ui_add_pachet_batch(l, listp)
                    except Exception as ex:
                        print(ex)
            if listp[0] == "stergere":
                if len(listp) == 2:
                    try:
                        ui_sterge_zile_pachet_batch(l, listp, undolist)
                    except Exception as ex:
                        print(ex)
            if listp[0] == "print":
                ui_print_pachet(l)
            if listp[0] == "undo":
                undo(undolist, l)
            if listp[0] == "exit":
                return
