from domain.pachet import get_data_i
from domain.pachet import get_data_s
from domain.pachet import get_destinatie
from domain.pachet import get_pret
from domain.pachet import to_int_data_i
from domain.pachet import to_int_data_s


def verifica_pret(pachet, user_input):
    return get_pret(pachet) > user_input


def verifica_dest(pachet, user_input):
    return get_destinatie(pachet) == user_input


def verifica_zile(pachet, user_input):
    return verifica_zile_int(pachet) <= user_input


def verifica_luna(pachet, luna_user_i):
    return get_data_i(pachet).month == luna_user_i and get_data_i(pachet).month == luna_user_i or get_data_s(
        pachet).month == luna_user_i and get_data_s(pachet) == luna_user_i


def verifica_zile_int(pachet):
    # functie care verifica numarul de zile pt 2 date de de inceput si de sfarsit
    return to_int_data_s(pachet) - to_int_data_i(pachet)