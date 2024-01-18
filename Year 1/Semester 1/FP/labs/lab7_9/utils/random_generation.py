import string
import random

from lab7_9.domain.subject import Subject


def generare_aleator_string(lungime):
    """
    Genereaza string-uri aleatoare de o anumita lungime
    :param lungime: int
    :return:
    """
    chars = string.ascii_uppercase
    return ''.join(random.choice(chars) for _ in range(lungime))


def generare_aleator_int(lungime):
    """
    Genereaza int-uri aleatoare de o anumita lungime
    :param lungime:
    :return:
    """
    intg = string.digits
    return ''.join(random.choice(intg) for _ in range(lungime))
