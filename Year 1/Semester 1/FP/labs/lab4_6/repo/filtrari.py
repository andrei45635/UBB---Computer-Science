from lab4_6.utils.verificari import verifica_luna
from lab4_6.utils.verificari import verifica_pret
from lab4_6.utils.verificari import verifica_dest
from lab4_6.domain.pachet import to_str_pachet, get_data_i


def eliminare_pret_dest(l, dest_input, pret_input, lst_m):
    # functie care care cauta pachetele din lista cu o destinatie diferita de cea data si cu pret mai mare decat
    # input de la user
    lst = [pachet for pachet in l if verifica_pret(pachet, pret_input) and not verifica_dest(pachet, dest_input)]
    for _pachet in lst:
        lst_m.append(_pachet)


def sterge_luna(l, user_input,lst_m):
    # functie care sterge pachetele cu aceeasi luna ca si luna_user_i
    lst = [pachet for pachet in l if get_data_i(pachet).month == user_input]
    # lst = [pachet for pachet in l if not verifica_luna(pachet, user_input)]
    print(lst)
    for _pachet in lst:
        lst_m.append(to_str_pachet(_pachet))
