def creeaza_pachet(data_i, data_s, dest, pret):
    # functie care creeaza un pachet de calatorie cu data de inceput data_i de tip data, data de sfarsit de tip data,
    # dest o destinatie string si pret de tip float > 0
    # input: data_i = data de inceput - data
    #       data_s = data de sfarsit - data
    #       dest = destinatie - string
    #       pret = pret - float > 0
    return [data_i, data_s, dest, pret]


def adauga_pachet_in_lista(l, pachet):
    # functie care adauga un pachet intr-o lista
    # input: l - lista
    #       pachet - pachet
    # output: l' - lista cu pachetul
    #       raises Exception cu mesajul
    #               "pachet cu aceleasi date introduse!\n"
    #       daca aceleasi date au fost introduse din nou
    for _pachet in l:
        if egale_pret(_pachet, pachet) and egale_dest(_pachet, pachet) and egale_data_i(_pachet,
                                                                                        pachet) and egale_data_s(
            _pachet, pachet):
            raise Exception("pachet cu aceleasi date introduse!\n")
    l.append(pachet)


def srv_adauga_pachet_in_lista(l, data_i, data_s, dest, pret):
    # functie care creeaza un pachet si incearca sa il introduca in lista l
    # input: l - lista
    #       pachet - pachet
    # output: -, daca totul e ok
    #        raises Exception cu mesajele din functiile anterioare
    pachet = creeaza_pachet(data_i, data_s, dest, pret)
    valideaza_pachet(pachet)
    adauga_pachet_in_lista(l, pachet)


def valideaza_pachet(pachet):
    # functie care valideaza daca un pachet pachet este introdus corect sau nu
    # input : pachet - pachet
    # output: -, daca pachetul a fost introdus corect
    #       raises Exception cu mesajul
    #                       "date gresite!"
    #                       "destinatie gresita!"
    #                       "pret gresit!"
    err = ""
    if get_data_i(pachet) > get_data_s(pachet):
        err += "date gresite!\n"
    if get_destinatie(pachet) == " ":
        err += "destinatie gresita!\n"
    if get_pret(pachet) <= 0:
        err += "pret gresit!\n"
    if len(err) > 0:
        raise Exception(err)


def get_data_i(pachet):
    # functie care returneaza data de inceput a pachetului pachet
    # input: pachet - un pachet
    # output: data - o data
    return pachet[0]


def get_data_s(pachet):
    # functie care returneaza data data de sfarsit a pachetului pachet
    # input: pachet - un pachet
    # output: data - o data
    return pachet[1]


def get_destinatie(pachet):
    # functie care returneaza destinatia string a pachetului pachet
    # input: pachet - un pachet
    # output: destinatia string a pachetului
    return pachet[2]


def get_pret(pachet):
    # functie care returneaza pretul float a pachetului pachet
    # input: pachet - un pachet
    # output: pretul float > 0 al pachetului
    return pachet[3]


def to_str_pachet(pachet):
    return str(
        "Data de inceput: " + str(pachet[0]) + "\n" + "Data de sfarsit: " + str(
            pachet[1]) + "\n" + "Destinatia: " +
        pachet[2] + "\n" + "Pretul: " + str((pachet[3])))


def to_int_data_i(pachet):
    # functie care returneaza int-ul din data de inceput
    # e.g. daca avem data de inceput data_i = 25-10-2021, functia va returna 20211025
    return 10000 * get_data_i(pachet).year + 100 * get_data_i(pachet).month + get_data_i(pachet).day


def to_int_data_s(pachet):
    # functie care returneaza int-ul din data de sfarsit
    # e.g. daca avem data de sfarsit data_i = 25-10-2021, functia va returna 20211025
    return 10000 * get_data_s(pachet).year + 100 * get_data_s(pachet).month + get_data_s(pachet).day


def egale_pret(p0, p1):
    return get_pret(p0) == get_pret(p1)


def egale_dest(p0, p1):
    return get_destinatie(p0) == get_destinatie(p1)


def egale_data_i(p0, p1):
    return get_data_i(p0) == get_data_i(p1)


def egale_data_s(p0, p1):
    return get_data_s(p0) == get_data_s(p1)
