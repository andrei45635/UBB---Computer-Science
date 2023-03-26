from domain.pachet import get_data_i
from domain.pachet import get_data_s
from domain.pachet import to_str_pachet
from utils.verificari import verifica_pret
from utils.verificari import verifica_dest


def cautare_pret_dest(l, pret_input, dest_input, lst_n):
    # functie care care cauta pachetele din lista cu o destinatie data si cu pret mai mic decat input de la user
    lst = [pachet for pachet in l if not verifica_pret(pachet, pret_input) and verifica_dest(pachet, dest_input)]
    for _pachet in lst:
        lst_n.append(to_str_pachet(_pachet))


def filtrare_data_s(l, data_s_input,lst_n):
    # functie care afiseaza pachetul cu data de sfarsit introdusa de utilizator
    lst = [pachet for pachet in l if (get_data_s(pachet) == data_s_input)]
    for _pachet in lst:
        lst_n.append(to_str_pachet(_pachet))


def cautare_pachet_valid(l, data_i_user, data_s_user, lst_n):
    # functie care afiseaza pachetele a caror dată de început este aceeași sau după de data de început citită și data de sfârșit este înainte sau aceeași cu data de sfârșit introdusă de la tastatură
    lst = [pachet for pachet in l if (get_data_i(pachet) >= data_i_user and get_data_s(pachet) <= data_s_user)]
    for _pachet in lst:
        lst_n.append(to_str_pachet(_pachet))