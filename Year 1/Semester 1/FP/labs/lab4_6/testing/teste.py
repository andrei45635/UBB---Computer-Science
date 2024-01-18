from datetime import datetime
import datetime
from lab4_6.domain.pachet import srv_adauga_pachet_in_lista
from lab4_6.domain.pachet import creeaza_pachet
from lab4_6.domain.pachet import adauga_pachet_in_lista
from lab4_6.domain.pachet import get_data_i
from lab4_6.domain.pachet import get_data_s
from lab4_6.domain.pachet import get_destinatie
from lab4_6.domain.pachet import get_pret
from lab4_6.domain.pachet import valideaza_pachet
from lab4_6.utils.undo import undo
from lab4_6.repo.stergeri import sterge_zile
from lab4_6.repo.stergeri import sterge_pret
from lab4_6.repo.stergeri import sterge_pachet_dest
from lab4_6.repo.rapoarte import medie_pret
from lab4_6.repo.filtrari import eliminare_pret_dest
from lab4_6.repo.cautari import cautare_pret_dest
from lab4_6.repo.cautari import filtrare_data_s
from lab4_6.repo.cautari import cautare_pachet_valid


def test_srv_adauga_pachet_in_lista():
    l = []
    assert (len(l) == 0)
    srv_adauga_pachet_in_lista(l, datetime.datetime.strptime('24/08/2021', "%d/%m/%Y"),
                               datetime.datetime.strptime('26/08/2021', "%d/%m/%Y"), "Galati", 9000.1)
    assert (len(l) == 1)
    try:
        srv_adauga_pachet_in_lista(l, datetime.datetime.strptime('24/08/2021', "%d/%m/%Y"),
                                   datetime.datetime.strptime('22/08/2021', "%d/%m/%Y"), " ", 9000.1)
        assert False
    except Exception as ex:
        assert (str(ex) == "date gresite!\ndestinatie gresita!\n")


def test_modifica_date():
    l = []
    assert len(l) == 0
    pachet = creeaza_pachet(datetime.datetime.strptime('24/08/2021', "%d/%m/%Y"),
                            datetime.datetime.strptime('26/08/2021', "%d/%m/%Y"),
                            "Galati", 9000.1)
    adauga_pachet_in_lista(l, pachet)
    assert len(l) == 1
    pachet_2 = creeaza_pachet(datetime.datetime.strptime('24/08/2021', "%d/%m/%Y"),
                              datetime.datetime.strptime('26/08/2021', "%d/%m/%Y"),
                              "Galati", 9040.1)
    adauga_pachet_in_lista(l, pachet_2)
    assert len(l) == 2


def test_adauga_pachet_in_lista():
    l = []
    assert (len(l) == 0)
    pachet = creeaza_pachet(datetime.datetime.strptime('24/08/2021', "%d/%m/%Y"),
                            datetime.datetime.strptime('26/08/2021', "%d/%m/%Y"),
                            "Galati", 9000.1)
    adauga_pachet_in_lista(l, pachet)
    assert (len(l) == 1)
    assert (get_data_i(pachet) == get_data_i(l[0]))
    assert (get_data_s(pachet) == get_data_s(l[0]))
    assert (get_destinatie(pachet) == get_destinatie(l[0]))
    assert (abs(get_pret(pachet) - get_pret(l[0]) < 0.0001))
    alt_pachet = creeaza_pachet(datetime.datetime.strptime('24/08/2021', "%d/%m/%Y"),
                                datetime.datetime.strptime('26/08/2021', "%d/%m/%Y"), "Galati", 9000.1)
    try:
        adauga_pachet_in_lista(l, alt_pachet)
        assert False
    except Exception as ex:
        assert (str(ex) == "pachet cu aceleasi date introduse!\n")


def test_valideaza_pachet():
    pachet = creeaza_pachet(datetime.datetime.strptime('24/08/2021', "%d/%m/%Y"),
                            datetime.datetime.strptime('26/08/2021', "%d/%m/%Y"),
                            "Galati", 9000.1)
    valideaza_pachet(pachet)
    pachet_gresit = creeaza_pachet(datetime.datetime.strptime('24/08/2021', "%d/%m/%Y"),
                                   datetime.datetime.strptime('22/08/2021', "%d/%m/%Y"), "Galati", 9000.1)
    try:
        valideaza_pachet(pachet_gresit)
    except Exception as ex:
        assert (str(ex) == "date gresite!\n")
    alt_pachet = creeaza_pachet(datetime.datetime.strptime('24/08/2021', "%d/%m/%Y"),
                                datetime.datetime.strptime('22/08/2021', "%d/%m/%Y"), " ", -904)
    try:
        valideaza_pachet(alt_pachet)
        assert False
    except Exception as ex:
        assert (str(ex) == "date gresite!\ndestinatie gresita!\npret gresit!\n")


def test_creeaza_pachet():
    data_i_string = '24/08/2021'
    data_i = datetime.datetime.strptime(data_i_string, "%d/%m/%Y")
    data_s_string = '26/08/2021'
    data_s = datetime.datetime.strptime(data_s_string, "%d/%m/%Y")
    dest = "Galati"
    pret = 9000.1
    pachet = creeaza_pachet(data_i, data_s, dest, pret)
    assert (get_data_i(pachet) == data_i)
    assert (get_data_s(pachet) == data_s)
    assert (get_destinatie(pachet) == dest)
    assert (abs(get_pret(pachet) - pret) < 0.0001)


def test_numar_oferte():
    l = []
    pachet_1 = creeaza_pachet(datetime.datetime.strptime('24/08/2021', "%d/%m/%Y"),
                              datetime.datetime.strptime('26/08/2021', "%d/%m/%Y"),
                              "Galati", 9000.1)
    pachet_2 = creeaza_pachet(datetime.datetime.strptime('23/08/2021', "%d/%m/%Y"),
                              datetime.datetime.strptime('24/08/2021', "%d/%m/%Y"),
                              "Galati", 9200.1)
    pachet_3 = creeaza_pachet(datetime.datetime.strptime('19/08/2021', "%d/%m/%Y"),
                              datetime.datetime.strptime('22/08/2021', "%d/%m/%Y"),
                              "Galati", 90040.1)
    pachet_4 = creeaza_pachet(datetime.datetime.strptime('24/08/2021', "%d/%m/%Y"),
                              datetime.datetime.strptime('26/08/2021', "%d/%m/%Y"),
                              "Braila", 9020.1)
    adauga_pachet_in_lista(l, pachet_1)
    adauga_pachet_in_lista(l, pachet_2)
    adauga_pachet_in_lista(l, pachet_3)
    adauga_pachet_in_lista(l, pachet_4)
    nr_oferte = 0
    for _pachet in l:
        if get_destinatie(_pachet) == "Galati":
            nr_oferte += 1
    assert nr_oferte == 3


def test_undo():
    l = []
    undolist = []
    assert len(l) == 0
    pachet_1 = creeaza_pachet(datetime.datetime.strptime('4/08/2021', "%d/%m/%Y"),
                              datetime.datetime.strptime('20/08/2021', "%d/%m/%Y"),
                              "Galati", 9000.1)
    pachet_2 = creeaza_pachet(datetime.datetime.strptime('24/08/2021', "%d/%m/%Y"),
                              datetime.datetime.strptime('29/08/2021', "%d/%m/%Y"),
                              "Galati", 9011)
    pachet_3 = creeaza_pachet(datetime.datetime.strptime('24/09/2021', "%d/%m/%Y"),
                              datetime.datetime.strptime('25/09/2021', "%d/%m/%Y"),
                              "Braila", 1224)
    adauga_pachet_in_lista(l, pachet_1)
    adauga_pachet_in_lista(l, pachet_2)
    adauga_pachet_in_lista(l, pachet_3)
    assert len(l) == 3
    sterge_pret(l,9000,undolist)
    assert len(l) == 1
    undo(undolist, l)
    assert len(l) == 3


def test_sterge_zile():
    l = []
    undolist = []
    assert len(l) == 0
    pachet_1 = creeaza_pachet(datetime.datetime.strptime('24/08/2021', "%d/%m/%Y"),
                              datetime.datetime.strptime('26/08/2021', "%d/%m/%Y"),
                              "Galati", 9000.1)
    pachet_2 = creeaza_pachet(datetime.datetime.strptime('23/08/2021', "%d/%m/%Y"),
                              datetime.datetime.strptime('24/08/2021', "%d/%m/%Y"),
                              "Galati", 9200.1)
    pachet_3 = creeaza_pachet(datetime.datetime.strptime('19/08/2021', "%d/%m/%Y"),
                              datetime.datetime.strptime('25/08/2021', "%d/%m/%Y"),
                              "Galati", 90040.1)
    pachet_4 = creeaza_pachet(datetime.datetime.strptime('24/08/2021', "%d/%m/%Y"),
                              datetime.datetime.strptime('29/08/2021', "%d/%m/%Y"),
                              "Braila", 9020.1)
    adauga_pachet_in_lista(l, pachet_1)
    adauga_pachet_in_lista(l, pachet_2)
    adauga_pachet_in_lista(l, pachet_3)
    adauga_pachet_in_lista(l, pachet_4)
    assert len(l) == 4
    sterge_zile(l, 3,undolist)
    assert len(l) == 2


def test_medie_pret():
    l = []
    pachet_1 = creeaza_pachet(datetime.datetime.strptime('24/08/2021', "%d/%m/%Y"),
                              datetime.datetime.strptime('26/08/2021', "%d/%m/%Y"),
                              "Galati", 9000.1)
    pachet_2 = creeaza_pachet(datetime.datetime.strptime('24/08/2021', "%d/%m/%Y"),
                              datetime.datetime.strptime('26/08/2021', "%d/%m/%Y"),
                              "Galati", 9011)
    pachet_3 = creeaza_pachet(datetime.datetime.strptime('24/08/2021', "%d/%m/%Y"),
                              datetime.datetime.strptime('26/08/2021', "%d/%m/%Y"),
                              "Galati", 9211.2)
    adauga_pachet_in_lista(l, pachet_1)
    adauga_pachet_in_lista(l, pachet_2)
    adauga_pachet_in_lista(l, pachet_3)
    for _pachet in l:
        try:
            medie_pret(l, "Galati")
        except ZeroDivisionError:
            assert medie_pret(l, "Galati") == "Media pretului este ", 9074.1


def test_sterge_pret():
    l = []
    undolist = []
    assert len(l) == 0
    pachet_1 = creeaza_pachet(datetime.datetime.strptime('24/08/2021', "%d/%m/%Y"),
                              datetime.datetime.strptime('26/08/2021', "%d/%m/%Y"),
                              "Galati", 9000.1)
    pachet_2 = creeaza_pachet(datetime.datetime.strptime('24/08/2021', "%d/%m/%Y"),
                              datetime.datetime.strptime('26/08/2021', "%d/%m/%Y"),
                              "Galati", 9011)
    pachet_3 = creeaza_pachet(datetime.datetime.strptime('24/08/2021', "%d/%m/%Y"),
                              datetime.datetime.strptime('26/08/2021', "%d/%m/%Y"),
                              "Galati", 2211.2)
    adauga_pachet_in_lista(l, pachet_1)
    adauga_pachet_in_lista(l, pachet_2)
    adauga_pachet_in_lista(l, pachet_3)
    assert len(l) == 3
    sterge_pret(l, 5000,undolist)
    assert len(l) == 1


def test_sterge_pachet_dest():
    l = []
    undolist = []
    assert len(l) == 0
    pachet_1 = creeaza_pachet(datetime.datetime.strptime('24/08/2021', "%d/%m/%Y"),
                              datetime.datetime.strptime('26/08/2021', "%d/%m/%Y"),
                              "Galati", 9000.1)
    pachet_2 = creeaza_pachet(datetime.datetime.strptime('24/08/2021', "%d/%m/%Y"),
                              datetime.datetime.strptime('26/08/2021', "%d/%m/%Y"),
                              "Galati", 9011)
    pachet_3 = creeaza_pachet(datetime.datetime.strptime('24/08/2021', "%d/%m/%Y"),
                              datetime.datetime.strptime('26/08/2021', "%d/%m/%Y"),
                              "Braila", 2211.2)
    adauga_pachet_in_lista(l, pachet_1)
    adauga_pachet_in_lista(l, pachet_2)
    adauga_pachet_in_lista(l, pachet_3)
    assert len(l) == 3
    sterge_pachet_dest(l, "Galati", undolist)
    assert len(l) == 1


def test_filtrare_data_s():
    l = []
    lst = []
    assert len(l) == 0
    assert len(lst) == 0
    pachet_1 = creeaza_pachet(datetime.datetime.strptime('4/08/2021', "%d/%m/%Y"),
                              datetime.datetime.strptime('20/08/2021', "%d/%m/%Y"),
                              "Galati", 9000.1)
    pachet_2 = creeaza_pachet(datetime.datetime.strptime('24/08/2021', "%d/%m/%Y"),
                              datetime.datetime.strptime('29/08/2021', "%d/%m/%Y"),
                              "Galati", 9011)
    pachet_3 = creeaza_pachet(datetime.datetime.strptime('24/09/2021', "%d/%m/%Y"),
                              datetime.datetime.strptime('25/09/2021', "%d/%m/%Y"),
                              "Braila", 2211.2)
    adauga_pachet_in_lista(l, pachet_1)
    adauga_pachet_in_lista(l, pachet_2)
    adauga_pachet_in_lista(l, pachet_3)
    assert len(l) == 3
    lst = [pachet for pachet in l if (get_data_s(pachet) == datetime.datetime.strptime('25/09/2021', "%d/%m/%Y"))]
    assert len(lst) == 1


def test_eliminare_pret_dest():
    l = []
    lst_m = []
    assert len(l) == 0
    assert len(lst_m) == 0
    pachet_1 = creeaza_pachet(datetime.datetime.strptime('4/08/2021', "%d/%m/%Y"),
                              datetime.datetime.strptime('20/08/2021', "%d/%m/%Y"),
                              "Galati", 9000.1)
    pachet_2 = creeaza_pachet(datetime.datetime.strptime('24/08/2021', "%d/%m/%Y"),
                              datetime.datetime.strptime('29/08/2021', "%d/%m/%Y"),
                              "Galati", 9011)
    pachet_3 = creeaza_pachet(datetime.datetime.strptime('24/09/2021', "%d/%m/%Y"),
                              datetime.datetime.strptime('25/09/2021', "%d/%m/%Y"),
                              "Braila", 1224)
    adauga_pachet_in_lista(l, pachet_1)
    adauga_pachet_in_lista(l, pachet_2)
    adauga_pachet_in_lista(l, pachet_3)
    assert len(l) == 3
    eliminare_pret_dest(l, "Braila", 1200, lst_m)
    assert len(lst_m) == 1


def test_cautare_pret_dst():
    l = []
    lst_m = []
    assert len(l) == 0
    assert len(lst_m) == 0
    pachet_1 = creeaza_pachet(datetime.datetime.strptime('4/08/2021', "%d/%m/%Y"),
                              datetime.datetime.strptime('20/08/2021', "%d/%m/%Y"),
                              "Galati", 9000.1)
    pachet_2 = creeaza_pachet(datetime.datetime.strptime('24/08/2021', "%d/%m/%Y"),
                              datetime.datetime.strptime('29/08/2021', "%d/%m/%Y"),
                              "Galati", 9011)
    pachet_3 = creeaza_pachet(datetime.datetime.strptime('24/09/2021', "%d/%m/%Y"),
                              datetime.datetime.strptime('25/09/2021', "%d/%m/%Y"),
                              "Braila", 1224)
    adauga_pachet_in_lista(l, pachet_1)
    adauga_pachet_in_lista(l, pachet_2)
    adauga_pachet_in_lista(l, pachet_3)
    assert len(l) == 3
    cautare_pret_dest(l, 10000, "Galati", lst_m)
    assert len(lst_m) == 2


def test_cautare_pachet_valid():
    l = []
    lst_m = []
    assert len(l) == 0
    assert len(lst_m) == 0
    pachet_1 = creeaza_pachet(datetime.datetime.strptime('4/08/2021', "%d/%m/%Y"),
                              datetime.datetime.strptime('20/08/2021', "%d/%m/%Y"),
                              "Galati", 9000.1)
    pachet_2 = creeaza_pachet(datetime.datetime.strptime('24/08/2021', "%d/%m/%Y"),
                              datetime.datetime.strptime('29/08/2021', "%d/%m/%Y"),
                              "Galati", 9011)
    pachet_3 = creeaza_pachet(datetime.datetime.strptime('24/09/2021', "%d/%m/%Y"),
                              datetime.datetime.strptime('25/09/2021', "%d/%m/%Y"),
                              "Braila", 1224)
    adauga_pachet_in_lista(l, pachet_1)
    adauga_pachet_in_lista(l, pachet_2)
    adauga_pachet_in_lista(l, pachet_3)
    assert len(l) == 3
    cautare_pachet_valid(l, datetime.datetime.strptime('1/08/2021', "%d/%m/%Y"), datetime.datetime.strptime('25/09/2021', "%d/%m/%Y"), lst_m)
    assert len(lst_m) == 3


def test_cautare_valid_si_print_lst_m():
    l = []
    lst_m = []
    test_list = []
    assert len(l) == 0
    assert len(lst_m) == 0
    pachet_1 = creeaza_pachet(datetime.datetime.strptime('4/08/2021', "%d/%m/%Y"),
                              datetime.datetime.strptime('20/08/2021', "%d/%m/%Y"),
                              "Galati", 9000.1)
    pachet_2 = creeaza_pachet(datetime.datetime.strptime('24/08/2021', "%d/%m/%Y"),
                              datetime.datetime.strptime('29/08/2021', "%d/%m/%Y"),
                              "Galati", 9011)
    pachet_3 = creeaza_pachet(datetime.datetime.strptime('24/09/2021', "%d/%m/%Y"),
                              datetime.datetime.strptime('25/09/2021', "%d/%m/%Y"),
                              "Braila", 1224)
    adauga_pachet_in_lista(l, pachet_1)
    adauga_pachet_in_lista(l, pachet_2)
    adauga_pachet_in_lista(l, pachet_3)
    assert len(l) == 3
    # eliminare_pret_dest(l, "Braila", 12400, lst_m) assert print_lst_m(lst_m) == [[datetime.date(2021, 08, 04),
    # datetime.date(2022, 08, 20), 'Galati', 9000.1],[datetime.date(2021, 08, 24), datetime.date(2022, 08, 29),
    # 'Galati', 9011.0]]
    try:
        eliminare_pret_dest(l, "Braila", 12400, lst_m)
        assert True
    except KeyError:
        assert False


def run_teste():
    test_creeaza_pachet()
    test_valideaza_pachet()
    test_adauga_pachet_in_lista()
    test_srv_adauga_pachet_in_lista()
    test_numar_oferte()
    test_medie_pret()
    test_sterge_pret()
    test_sterge_zile()
    test_sterge_pachet_dest()
    test_filtrare_data_s()
    test_undo()
    test_cautare_valid_si_print_lst_m()
    test_cautare_pret_dst()
    test_cautare_pachet_valid()
